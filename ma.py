from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from elements_manager import *
from datetime import datetime



# Specify the path to the ChromeDriver executable
# driver_path = './chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_argument('--log-level=3')  # Suppress logging


# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# URL of the attendance system
url = 'https://app.hrone.cloud/login'  # Replace with the actual URL

# def any_of(*conditions):
#     def _predicate(driver):
#         for condition in conditions:
#             try:
#                 if condition(driver):
#                     return True
#             except Exception:
#                 pass
#         return False
#     return _predicate

try:
    # Navigate to the login page
    driver.get(url)

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, 'hrone-username'))  # Replace with the actual ID
    )

    # enter mobile number
    mobile_number_field = driver.find_element(By.ID, 'hrone-username')  # Replace with the actual ID
    mobile_number_field.send_keys('9100761197')  # Replace with your mobile number

    #click next
    next_button = driver.find_element(By.CSS_SELECTOR, '.loginform.ladda-button')  # Replace with the actual ID
    next_button.click()

    password_field = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.ID, 'hrone-password'))
    )
    password_field.send_keys('Qwertyuiop@123')
    # print(driver.page_source)

    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load and find the first button (e.g., Check-in button)
    # WebDriverWait(driver, 30).until(
    #     any_of(
    #           EC.presence_of_element_located((By.CLASS_NAME, "btnclose")),
    #           EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.w-100", "Mark attendance")),
    #         )
    # )

    cls_button = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.CLASS_NAME, 'btnclose'))
    )

    # cls_button = driver.find_element(By.ID, 'btnclose')
    if cls_button.is_displayed():
        cls_button.click()
    mark1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.w-100'))
    )
    mark1.click()
    # Wait for popup and final mark attendace btn 
    mark2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-success.font-13.ma-action.font-bold.ladda-button'))
    )
    mark2.click()
        
    time.sleep(5)
  
    print("Marked attendace!!!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
finally:
    # Close the browser
    driver.quit()

