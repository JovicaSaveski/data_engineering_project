import pandas as pd
from datetime import datetime, timedelta
from airflow.providers.mysql.hooks.mysql import MySqlHook

def process_and_detect_gaps(**context):
    """
    Process flight, bus, and weather data to detect time windows with insufficient bus coverage
    
    Returns:
        pd.DataFrame: Processed data with gap detection results
    """

    ti = context['task_instance']
    flights_df = ti.xcom_pull(task_ids='scrape_flight_arrivals')
    bus_df = ti.xcom_pull(task_ids='scrape_bus_schedule')
    weather_df = ti.xcom_pull(task_ids='fetch_weather_data')
    
    flights_df = pd.DataFrame(flights_df) if isinstance(flights_df, dict) else flights_df
    bus_df = pd.DataFrame(bus_df) if isinstance(bus_df, dict) else bus_df
    weather_df = pd.DataFrame(weather_df) if isinstance(weather_df, dict) else weather_df
    
    results = []
    
    current_time = datetime.now()
    for hour in range(24):
        time_window = current_time.replace(hour=hour, minute=0, second=0)
        
        flights_in_window = len(flights_df[
            (flights_df['arrival_time'] >= time_window) &
            (flights_df['arrival_time'] < time_window + timedelta(hours=1))
        ]) if not flights_df.empty else 0
        
        bus_available = any(
            pd.to_datetime(bus_df['departure_time']).dt.hour == hour
        ) if not bus_df.empty else False
        
        weather_conditions = weather_df.iloc[0].to_dict() if not weather_df.empty else {}
        
        taxi_demand = calculate_taxi_demand(
            flights_in_window,
            bus_available,
            weather_conditions.get('weather_condition', 'Unknown')
        )
        
        results.append({
            'timestamp': time_window,
            'flights_count': flights_in_window,
            'bus_available': bus_available,
            'weather_condition': weather_conditions.get('weather_condition', 'Unknown'),
            'predicted_taxi_demand': taxi_demand
        })
    
    return pd.DataFrame(results)

def calculate_taxi_demand(flights_count, bus_available, weather_condition):
    """
    Calculate predicted taxi demand based on flights, bus availability and weather
    """
    base_demand = flights_count * 0.3  # Assuming 30% of passengers need taxis
    
    if not bus_available:
        base_demand *= 1.5
    
    weather_multipliers = {
        'Rain': 1.3,
        'Snow': 1.4,
        'Thunderstorm': 1.5,
        'Clear': 1.0
    }
    
    weather_multiplier = weather_multipliers.get(weather_condition, 1.0)
    final_demand = base_demand * weather_multiplier
    
    return round(final_demand)

def load_data(**context):
    """
    Load processed data into MySQL database
    """
    ti = context['task_instance']
    df = ti.xcom_pull(task_ids='process_data')
    
    if df is None or df.empty:
        print("No data to load")
        return
    
    records = df.to_dict('records')
    
    mysql_hook = MySqlHook(mysql_conn_id='mysql_default')
    
    insert_sql = """
        INSERT INTO taxi_demand (
            timestamp, flights_count, bus_available, 
            weather_condition, predicted_taxi_demand
        ) VALUES (
            %(timestamp)s, %(flights_count)s, %(bus_available)s,
            %(weather_condition)s, %(predicted_taxi_demand)s
        )
    """
    
    try:
        mysql_hook.insert_rows(
            table='taxi_demand',
            rows=records,
            target_fields=[
                'timestamp', 'flights_count', 'bus_available',
                'weather_condition', 'predicted_taxi_demand'
            ]
        )
        print(f"Successfully loaded {len(records)} records")
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        raise