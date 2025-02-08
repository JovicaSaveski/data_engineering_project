from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_flights():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(SKP_URL)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "flight-row"))
        )
        
        flights = []
        for row in driver.find_elements(By.CLASS_NAME, "flight-row"):
            flight = {
                "time": row.find_element(By.CLASS_NAME, "time").text,
                "origin": row.find_element(By.CLASS_NAME, "origin").text,
                "status": row.find_element(By.CLASS_NAME, "status").text
            }
            flights.append(flight)
            
        return flights
    finally:
        driver.quit()
