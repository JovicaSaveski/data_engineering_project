from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime

def scrape_bus_schedule():
    """
    Scrapes bus schedule data from WTransporter website.
    Returns a DataFrame with bus times and other relevant information.
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get('https://wtransporter.com/schedule')
        
        
        schedule_data = []
        schedule_elements = driver.find_elements(By.CLASS_NAME, 'schedule-row')
        
        for element in schedule_elements:
            time = element.find_element(By.CLASS_NAME, 'departure-time').text
            schedule_data.append({
                'departure_time': time,
                'scrape_date': datetime.now().strftime('%Y-%m-%d')
            })
            
        driver.quit()
        
        return pd.DataFrame(schedule_data)
        
    except Exception as e:
        print(f"Error scraping bus schedule: {str(e)}")
        return pd.DataFrame()  # Return empty DataFrame on error
    
    finally:
        if 'driver' in locals():
            driver.quit()