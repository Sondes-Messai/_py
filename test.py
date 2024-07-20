from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

#Initialisation du Service ChromeDriver
service = Service(ChromeDriverManager().install())

#Initialisation du navigateur avec les options et le service
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.python.org/")
time.sleep(5)
driver.get("https://www.gasq.org/fr-FR/cftl.html")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
driver.extecute_script("$(window.open(''))")
for handle in driver.window_handles():
    driver.switch_to.window(handle)
    

time.sleep(2)
driver.quit()
