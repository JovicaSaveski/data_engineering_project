# Project Title: Taxi Demand Prediction Pipeline for SKP Airport

## Objective:
Build a pipeline to identify time windows with insufficient bus coverage at SKP Airport, combining flight arrivals, WTransporter schedules, and weather data to predict optimal taxi dispatch times.
## Data Sources

### Flight Arrivals:
Source: SKP Airport Arrivals Page

Data: Flight times, airline, origin, status (dynamic HTML)

### Bus Schedules:
Source: WTransporter Timetable

Data: Winter 2024/25 schedule (08:00–20:00 daily)

### Weather API:
Source: OpenWeatherMap

Data: Temperature, precipitation, wind speed


## Pipeline Architecture

```python
scrape_flights → scrape_bus_schedule → fetch_weather → detect_coverage_gaps → load_mysql → alert_taxi_dispatch
```

## Key Components
1. Scraping Logic
Flights (Python + Selenium):
```python
def scrape_skp_flights():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(SKP_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flight-row")))
    # Extract flight times, status, origin
    ...
```

Bus Schedule (Static Scrape):

```python
def scrape_wtransporter():
    response = requests.get(WTRANSPORTER_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract timetable (assumes static winter schedule)
    return [{"departure_time": "08:00", "interval": "30min"}, ...]
```

2. Weather Integration

```python
def fetch_weather(api_key):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Skopje&appid={api_key}").json()
```
```python
import requests
def fetch_weather(api_key):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Skopje&appid={api_key}")
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None  # Or raise the exception if you want the DAG to fail
```

3. Gap Detection Logic

```python
def detect_gaps(flights, buses):
    gaps = []
    for flight in flights:
        flight_time = parse(flight['arrival_time'])
        # Check if any bus departs within 30min post-arrival
        has_coverage = any(
            abs((bus_time - flight_time).total_seconds()) <= 1800 
            for bus_time in buses
        )
        if not has_coverage:
            gaps.append(flight_time)
    return gaps
```

4. Storage (MySQL)
Tables:

```sql
CREATE TABLE taxi_demand (
    gap_start DATETIME,
    gap_end DATETIME,
    precipitation DECIMAL(5,2),
    temperature DECIMAL(5,2),
    flights_affected INT
);
```
```sql
CREATE TABLE taxi_demand (
    gap_start DATETIME,
    gap_end DATETIME,
    precipitation DECIMAL(5,2),
    temperature DECIMAL(5,2),
    flights_affected INT,
    flight_number VARCHAR(20),
    origin_city VARCHAR(100)
);
```

Airflow DAG

```python
with DAG('taxi_demand', schedule_interval='@hourly') as dag:
    t1 = PythonOperator(task_id='scrape_flights', python_callable=scrape_skp_flights)
    t2 = PythonOperator(task_id='scrape_buses', python_callable=scrape_wtransporter)
    t3 = PythonOperator(task_id='get_weather', python_callable=fetch_weather)
    t4 = PythonOperator(task_id='find_gaps', python_callable=detect_gaps, 
                        op_args=[t1.output, t2.output])
    t5 = PythonOperator(task_id='load_data', python_callable=load_to_mysql)
    t1 >> t3 >> t4 >> t5
    t2 >> t4
```
```python
with DAG('taxi_demand', schedule_interval='@hourly') as dag:
    t1 = PythonOperator(task_id='scrape_flights', python_callable=scrape_skp_flights)
    t2 = PythonOperator(task_id='scrape_buses', python_callable=scrape_wtransporter)
    t3 = PythonOperator(task_id='get_weather', python_callable=fetch_weather)
    t4 = PythonOperator(task_id='find_gaps', python_callable=detect_gaps,
                        op_args=[t1.output, t2.output, t3.output]) # Pass weather data to find_gaps
    t5 = PythonOperator(task_id='load_data', python_callable=load_to_mysql)

    # Define dependencies
    t1 >> t4
    t2 >> t4
    t3 >> t4
    t4 >> t5
```

## Key Features
* Dynamic vs. Static Scraping:
    * Flights: Real-time updates with Selenium
    * Buses: Daily scrape (static winter schedule)
* Gap Logic: Flags flights without bus coverage 30min pre/post arrival
* * * Weather Impact: Rain/snow increases predicted taxi demand by 40% (heuristic)

## Documentation Outline

* Project Overview:
    * Problem: Manual taxi dispatch leads to missed revenue during bus gaps.
    * Solution: Automatically identify coverage gaps using multi-source data.
* Architecture:
    * Diagram of Airflow → Scrapers → MySQL → Taxi Dispatch API
* Data Validation:
    * Ensure no overlapping bus coverage for flagged gaps
    * Handle timezone-aware datetime parsing (CET → UTC)
    * Check for missing values in flight arrival data
    * Validate weather data against historical ranges
    * Verify that bus departure times are within the operating hours (08:00-20:00)
* Results:
    * Sample output: "2025-02-08 22:15: No buses. Predicted taxis needed: 12 * (rain)"

## Ethical Considerations
    * Avoid scraping SKP/WTransporter during peak hours
    * Cache bus schedule to minimize requests
    * Use OpenWeatherMap’s free tier responsibly
    * using multiple sources (web + API), transformations (gap detection), and orchestration (Airflow). 