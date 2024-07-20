from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
chrome_options=Options()
chrome_options.add_argument("--start-maximized")
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_options)
#ouvrir la page python
driver.get("https://www.python.org/")
# Trouver le champ de recherche
search_box = driver.find_element(By.ID, 'id-search-field')

# Cliquer dans le champ de recherche
search_box.click()

# Entrer le texte à rechercher
search_box.send_keys('selenium')

# Trouver le bouton "Go"
go_button = driver.find_element(By.ID, 'submit')

# Cliquer sur le bouton "Go"
go_button.click()


# sleep
time.sleep(5)

# Trouvee link   text
link = driver.find_element(By.LINK_TEXT, 'Revision automatica de despliegues web usando Selenium')

# Click on the link
link.click()


