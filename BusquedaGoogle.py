from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#Opciones para la navegación
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Inciar en segunda pantalla
driver.set_window_position(3000,0)
driver.maximize_window()
time.sleep(1)

#Pagina Inicial
driver.get('https://www.google.com.mx/')

#Busqueda por "Promociones MX"
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gLFyf.gsfi'))).send_keys('promociones mx facebook')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gLFyf.gsfi'))).send_keys(Keys.RETURN)

time.sleep(1)
divPrincipals = driver.find_element(By.CSS_SELECTOR, 'div.v7W49e')

#print("Length div: " + str(len(divPrincipals)))
#text = divPrincipals[0].get_attribute('innerHTML')

text = divPrincipals.get_attribute('innerHTML')
soup = BeautifulSoup(text, 'html.parser')
print("Length soup: " + str(len(soup)))
print("soup: " + str(soup))

urls = soup.findAll("a")
print("Length urls: " + str(len(urls)))

c = 0
stringForA = []
for url in urls:
    c += 1
    stringFind = str(url.get('href'))
    if 'facebook.com' in stringFind:
        x = stringFind.split('/')
        stringFor = ""
        limit = 3
        cc = 0
        for xC in x:
            cc += 1
            stringFor += xC
            if cc > 4:
                break
            stringFor += "/"
        if 'search' not in stringFor:
            stringForA.append(stringFor)
            print("URL" + str(c) + ":" + stringFor)

stringForASet = set(stringForA)
ccc = 0
for item in stringForASet:
    ccc += 1
    driver.get(item)
    time.sleep(1)
    divPrincipals = driver.find_elements(By.CSS_SELECTOR,'span.hrs1iv20.pq6dq46d')
    print("verificación: " + str(len(divPrincipals)))
    print("URL" + str(ccc) + ":" + item)

#urllib.request.urlretrieve("https://scontent.fmex36-1.fna.fbcdn.net/v/t39.30808-1/271593546_10158884688344163_4205614859100983586_n.png?stp=dst-png_p200x200&_nc_cat=1&ccb=1-6&_nc_sid=1eb0c7&_nc_ohc=65MNgi47dxEAX8GZXhr&_nc_ht=scontent.fmex36-1.fna&oh=00_AT9pCO1JtjyMfDJJVw1ZeY2y4_8rndVOU45P5avwO3HkuQ&oe=6284591D","HEB_MEXICO.png")

time.sleep(10000)