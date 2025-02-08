# Store sensitive data as environment variables
import os

SKP_URL = "https://skp.airports.com.mk/en-EN/flights/arrival-flights"
WTRANSPORTER_URL = "https://www.wtransporter.com/#timetable"
OWM_API_KEY = os.getenv("OWM_API_KEY")  # Set in Airflow UI
MYSQL_CONN_ID = "mysql_conn"            # Airflow connection ID
