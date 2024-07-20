from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

service = Service (ChromeDriverManager().install())
driver = webdriver.Chrome(service= service, options=chrome_options)


driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

text_field=driver.find_element(By.NAME,"username")
text_field.clear()
text_field.send_keys("Admin")

text_field=driver.find_element(By.NAME,"password")
text_field.clear()
text_field.send_keys("admin123")

login_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
login_button.click()

time.sleep(2)
current_url = driver.current_url
assert current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', f"URL actuelle: {current_url},URL attendue:https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"