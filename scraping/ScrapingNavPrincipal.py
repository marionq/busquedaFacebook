from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import date
from Images import Images
from scraping.VerTodos import VerTodos


#Opciones para la navegación
from webdriver_manager.chrome import ChromeDriverManager

class ScrapingNavPrincipal:
    def getImageNavPrincipal(self, urlVerTodos):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Inciar en segunda pantalla
        driver.set_window_position(3000, 0)
        driver.maximize_window()
        time.sleep(1)

        busqueda = 'icono santander'
        # Se recupera la URL de la etiqueta ver todos
        verTodos = VerTodos()
        # Se despliega la url de la etiqueta ver todos
        driver.get(verTodos.getUrl(busqueda))

        # Se ejecuta scroll hacia abajo
        for c in range(1, 20):
            time.sleep(1)
            bajar = f'window.scrollTo(0,{c}000)'
            driver.execute_script(bajar)

        # div que contiene la atiqueta <img> con la imagen
        time.sleep(1)
        divImagenesInicio = driver.find_elements(By.CLASS_NAME, 'bRMDJf.islir')
        print("Length divPrincipals: " + str(len(divImagenesInicio)))

        # Guarda las imagenes del Div principal
        getData = Images()
        response = getData.divPrincipalSaveImage(divImagenesInicio)
        print(response)