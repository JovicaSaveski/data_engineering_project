-- Create database
CREATE DATABASE IF NOT EXISTS taxi_demand_db;

-- Use the database
USE taxi_demand_db;

-- Create table for taxi demand predictions
CREATE TABLE IF NOT EXISTS taxi_demand_gaps (
    gap_start DATETIME PRIMARY KEY,
    gap_end DATETIME,
    flight_count INT,
    temperature DECIMAL(5,2),
    precipitation DECIMAL(5,2),
    bus_coverage BOOLEAN
);

CREATE TABLE IF NOT EXISTS taxi_demand (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    flights_count INT,
    bus_available BOOLEAN,
    weather_condition VARCHAR(50),
    predicted_taxi_demand INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM taxi_demand ORDER BY timestamp;
SELECT * FROM taxi_demand_gaps ORDER BY gap_start;