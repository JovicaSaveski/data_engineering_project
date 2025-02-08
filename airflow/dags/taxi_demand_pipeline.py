from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
from scripts.skp_scraper import scrape_flights
from scripts.wtransporter_scraper import scrape_bus_schedule
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.weather_api import get_weather_data
from scripts.data_processing import process_and_detect_gaps, load_data
import pandas as pd

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG('taxi_demand_prediction',
        default_args=default_args,
        schedule_interval='@hourly',
        start_date=datetime(2025, 2, 8)) as dag:

    t1 = PythonOperator(
        task_id='scrape_flight_arrivals',
        python_callable=scrape_flights
    )

    t2 = PythonOperator(
        task_id='scrape_bus_schedule',
        python_callable=scrape_bus_schedule
    )

    t3 = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=get_weather_data,
        op_kwargs={'api_key': '{{ var.value.OWM_API_KEY }}'}
    )

    t4 = PythonOperator(
        task_id='process_data',
        python_callable=process_and_detect_gaps,
        provide_context=True
    )

    t5 = PythonOperator(
        task_id='load_to_mysql',
        python_callable=load_data,
        provide_context=True
    )

    t1 >> t3 >> t4
    t2 >> t4
    t4 >> t5
