from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options=Options()
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
#chrome_options.add_argument("--headless")  # Mode headless
driver = webdriver.Chrome(service = service, options=chrome_options)
wait = WebDriverWait(driver, 60)

# aller sur le site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Vérification de l'URL actuelle
current_url_orange = driver.current_url
# Titre actuel
current_title_orange =driver.title
# Vérification de l'URL actuelle
assert current_url_orange == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', f"URL actuelle: {current_url_orange}, URL attendue: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# Vérification du Titre actuel
assert  current_title_orange == 'OrangeHRM',f"Titre actuel: {current_title_orange}, OrangeHRM"

# username et pwd
wait.until(EC.visibility_of_element_located((By.NAME,'username')))
driver.find_element(By.NAME,'username').send_keys("Admin")
wait.until(EC.visibility_of_element_located((By.NAME,'password')))
driver.find_element(By.NAME,'password').send_keys("admin123")

# login
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# aller sur pmi
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]')))
driver.find_element(By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]').click()

# add employe
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[class="oxd-button oxd-button--medium oxd-button--secondary"]')))
driver.find_element(By.CSS_SELECTOR,'button[class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

# entrer nom et prenom 
wait.until(EC.visibility_of_element_located((By.NAME,"firstName")))
driver.find_element(By.NAME,"firstName").send_keys("Sylvie")

wait.until(EC.visibility_of_element_located((By.NAME,"lastName")))
driver.find_element(By.NAME,"lastName").send_keys("THACKER")

# cliquer sur add
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').submit()

# Vérifier l'enregistrement du nouvel employé
wait.until(EC.visibility_of_element_located((By.XPATH,'//h6[@class="oxd-text oxd-text--h6 --strong"]')))
employeeName=driver.find_element(By.XPATH,'//h6[@class="oxd-text oxd-text--h6 --strong"]').text
print(employeeName)
 
# revenir sur pmi
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[href="/web/index.php/pim/viewPimModule"]')))
driver.find_element(By.CSS_SELECTOR,'a[href="/web/index.php/pim/viewPimModule"]').click()

# filtre ( chercher par nom  "Sylvie")
wait.until(EC.visibility_of_element_located((By.XPATH,'//div/div[1]/div/div[2]/div/div/input')))
driver.find_element(By.XPATH,'//div/div[1]/div/div[2]/div/div/input').send_keys("Sylvie")

# cliquer sur search 
wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@type="submit"]')))
driver.find_element(By.XPATH,'//button[@type="submit"]').click()

# vérifier si cest coché pour un INPUT utiliser 'presence_of_element_located'
wait.until(EC.presence_of_element_located((By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/input')))
element_list = driver.find_element(By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/input')
wait.until(EC.visibility_of_element_located((By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/span')))

element_list_to_click=driver.find_element(By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/span')

if element_list.is_selected:

    element_list_to_click.click()

# supprimer la liste cochée
wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin"]')))
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin"]').click()

# confirmer la supp
wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')))
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()

# Vérifier qu'il n'existe plus d'employé nommé 'Sylvie THACKER'
# filtre ( chercher par nom  "Sylvie")
wait.until(EC.visibility_of_element_located((By.XPATH,'//div/div[1]/div/div[2]/div/div/input')))
driver.find_element(By.XPATH,'//div/div[1]/div/div[2]/div/div/input').send_keys("Sylvie")

# Message No RecordS Found = 
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[2]/div/span")))
msg = driver.find_element(By.XPATH,"//div[2]/div/span").text
print(msg)

# Fermerle navigateur
driver.quit()