from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time






chrome_options=Options()

chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
chrome_options.add_argument("--headless")  # Mode headless
driver = webdriver.Chrome(service = service, options=chrome_options)

# aller sur le site

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)




# username et pwd

texte = driver.find_element(By.NAME,"username")

texte.send_keys("admin")




mdp = driver.find_element(By.NAME,"password")

mdp.send_keys("admin123")

time.sleep(2)

# login

driver.find_element(By.XPATH,'//button[@type ="submit"]').click()

time.sleep(3)
# aller sur pmi

driver.find_element(By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]').click()

time.sleep(3)
# add employe

driver.find_element(By.CSS_SELECTOR,'button[class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

time.sleep(3)
# entrer nom et prenom 

driver.find_element(By.NAME,"firstName").send_keys("Sara")

time.sleep(2)

driver.find_element(By.NAME,"lastName").send_keys(" Benh")

time.sleep(2)

# cliquer sur add

driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').submit()

time.sleep(5)

# #To check that we added our employee we found the element conaining the text:
# employee_name_element=driver.find_element(By.XPATH,'//h6[@class="oxd-text oxd-text--h6 --strong"]')
# employee_name=employee_name_element.text
# print(employee_name)
# assert employee_name == "FirstName16 LastName1", "Error Name"
 
suite 
 # revenir sur pmi

driver.find_element(By.CSS_SELECTOR,'a[class="oxd-main-menu-item active"]').click()

time.sleep(5)

# filtre ( chercher par nom  "sara")

driver.find_element(By.XPATH,'//div/div[1]/div/div[2]/div/div/input').send_keys("Sara")

time.sleep(3)
# cliquer sur search 

driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)


# verifier si cest coché , 

element_list = driver.find_element(By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/input')

element_list_to_click=driver.find_element(By.XPATH,'//div[2]/div[1]/div/div[1]/div/div/label/span')


if element_list.is_selected:

    element_list_to_click.click()

time.sleep(3)


# supprimer la liste cochée

driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin"]').click()

time.sleep(5)

# confirmer la supp

driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()

time.sleep(3)