from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_options)
#ouvrir la page python
driver.get("https://www.python.org/")
time.sleep(1)
# URL actuelle
current_url = driver.current_url
# Vérification de l'URL actuelle
assert current_url == 'https://www.python.org/', f"URL actuelle: {current_url}, URL attendue: https://www.python.org/"
time.sleep(2)
download_list=driver.find_element(By.CSS_SELECTOR, f"a[href='/downloads/']")
# Passer la souris sur l'élément pour afficher la liste déroulante
actions = ActionChains(driver)
actions.move_to_element(download_list).perform()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, f"a[href='/downloads/windows/']").click()
time.sleep(2)
current_url = driver.current_url
# Vérification de l'URL actuelle
assert current_url == 'https://www.python.org/downloads/windows/', f"URL actuelle: {current_url}, URL attendue: https://www.python.org/downloads/windows/"
#fermer le navigateur
driver.quit()