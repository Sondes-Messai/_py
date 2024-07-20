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

#cliquer sur le nom d'utilisateur pour ouvrir la liste
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()

#cliquer sur le bouton login
#pour choisir comment localiser le login: par class n'est pas le bon choix car il est dupliqué, par href est le bon choix
driver.find_element(By.CSS_SELECTOR, f"a[href='/web/index.php/auth/logout']").click()

time.sleep(2)
current_url_orange_after_logout = driver.current_url
time.sleep(2)
# Vérification de l'URL actuelle
assert current_url_orange_after_logout == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', f"URL actuelle: {current_url_orange_after_login}, URL attendue: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

#fermer le navigateur
driver.quit() 