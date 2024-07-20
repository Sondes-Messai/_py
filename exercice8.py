from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def handle_simple_alert(driver):
    driver.find_element(By.ID, "alertButton").click()
    time.sleep(2)
    alert = Alert(driver)
    print("Alert text:", alert.text)
    alert.accept()

def handle_confirm_alert(driver):
    driver.find_element(By.ID, "confirmButton").click()
    time.sleep(2)
    alert = Alert(driver)
    print("Confirm text:", alert.text)
    alert.dismiss()

def handle_prompt_alert(driver):
    driver.find_element(By.ID, "promtButton").click()
    time.sleep(2)
    alert = Alert(driver)
    print("Prompt text:", alert.text)
    alert.send_keys("You can do it Girls WOMEN POWER ")
    alert.accept()

def tear_down(driver):
    driver.quit()


# Initialisation du service ChromeDriver
chrome_options=Options()
chrome_options.add_argument("--start-maximized")

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_options)
# Ouvrir une page web
driver.get("https://demoqa.com/alerts")
time.sleep(5)
handle_simple_alert(driver)
time.sleep(3)
handle_confirm_alert(driver)
time.sleep(3)
handle_prompt_alert(driver)
time.sleep(1000)
tear_down(driver)