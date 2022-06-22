"""
Regresa la URL del div ver todos para la extracción de todas las imagenes
"""

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

class VerTodos:

    def getUrl(self, busqueda):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #Inciar en segunda pantalla
        driver.set_window_position(3000,0)
        driver.maximize_window()
        time.sleep(1)

        url = 'https://www.google.com.mx'

        #Pagina Inicial
        driver.get(url)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gLFyf.gsfi'))).send_keys(busqueda)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gLFyf.gsfi'))).send_keys(Keys.RETURN)

        time.sleep(1)
        #div /html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/g-section-with-header/div[4]
        aVerTodos = driver.find_elements(By.CLASS_NAME, 'wFKnCb.GTERze')
        print("Length divPrincipals: " + str(len(aVerTodos)))
        aVerTodosText = aVerTodos[0].get_attribute('innerHTML')
        print(f'aVerTodosText: {aVerTodosText}')
        aVerTodosSoup = BeautifulSoup(aVerTodosText, 'html.parser')
        aVerTodos = aVerTodosSoup.findAll("a")
        stringFindHref = str(aVerTodos[0].get('href'))

        inicioVerTodos = url + stringFindHref

        return inicioVerTodos