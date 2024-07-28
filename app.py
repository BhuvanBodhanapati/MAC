from flask import Flask
# from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import logging
import os

# Setup logging
# logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
# scheduler = BackgroundScheduler()

def mark_attendance():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    chrome_options.add_argument('--log-level=3')  # Suppress logging

    chrome_binary_path = os.path.expanduser('~/chrome/opt/google/chrome/google-chrome')
    chrome_options.binary_location = chrome_binary_path


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    url = 'https://app.hrone.cloud/login'  # Replace with the actual URL

    try:
        driver.get(url)

        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, 'hrone-username'))  # Replace with the actual ID
        )

        mobile_number_field = driver.find_element(By.ID, 'hrone-username')  # Replace with the actual ID
        mobile_number_field.send_keys('9100761197')  # Replace with your mobile number

        next_button = driver.find_element(By.CSS_SELECTOR, '.loginform.ladda-button')  # Replace with the actual ID
        next_button.click()

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'hrone-password'))
        )
        password_field.send_keys('Qwertyuiop@123')
        password_field.send_keys(Keys.RETURN)

        cls_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btnclose'))
        )

        if cls_button.is_displayed():
            cls_button.click()

        mark1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.w-100'))
        )
        mark1.click()

        mark2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-success.font-13.ma-action.font-bold.ladda-button'))
        )
        mark2.click()

        time.sleep(5)

        logging.info("Marked attendance!!! %s", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
    finally:
        driver.quit()

# Schedule the attendance marking function
# scheduler.add_job(mark_attendance, 'cron', hour=9, minute=30)
# scheduler.add_job(mark_attendance, 'cron', hour=18, minute=0)
# scheduler.add_job(mark_attendance, 'cron', hour=21, minute=15)
# scheduler.add_job(mark_attendance, 'cron', hour=23, minute=50)
# scheduler.start()

@app.route('/')
def index():
    mark_attendance()
    msg = 'Attendance marked ' + datetime.now().strftime("%B %d, %Y, %I:%M %p")
    print(msg)
    return  msg

if __name__ == "__main__":
    app.run()
