from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
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
# Titre actuel
current_title =driver.title
# Vérification de l'URL actuelle
assert current_url == 'https://www.python.org/', f"URL actuelle: {current_url}, URL attendue: https://www.python.org/"
# Vérification du Titre actuel
assert  current_title == 'Welcome to Python.org',f"Titre actuel: {current_title}, Titre attendu: Welcome to Python.org"
#Ouvrir un onglet
driver.execute_script("$(window.open(''))")
#Pointer sur l'onglet ouvert
driver.switch_to.window(driver.window_handles[1])
#ouvrir la page orange
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)
# Vérification de l'URL actuelle
current_url_orange = driver.current_url
# Titre actuel
current_title_orange =driver.title
# Vérification de l'URL actuelle
assert current_url_orange == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', f"URL actuelle: {current_url_orange}, URL attendue: https://www.python.org/"
# Vérification du Titre actuel
assert  current_title_orange == 'OrangeHRM',f"Titre actuel: {current_title_orange}, OrangeHRM"
driver.get("https://opensource-demo.orangehrmlive.com")
driver.findElement(By.idElement(Byid("")))
time.sleep(2) 
