from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from Images import Images
from scraping.VerTodos import VerTodos
from scraping.ScrapingNavsSecundarios import ScrapingNavsSecundarios

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

busqueda = 'icono santander'
# Se recupera la URL de la etiqueta ver todos
verTodos = VerTodos()
# Se despliega la url de la etiqueta ver todos con la busqueda
driver.get(verTodos.getUrl(busqueda))

# Se ejecuta scroll hacia abajo
for c in range(1, 20):
    time.sleep(1)
    bajar = f'window.scrollTo(0,{c}000)'
    driver.execute_script(bajar)

"""
Div Principal
"""
#Busqueda de div principal, el cual contien las imagenes a guardar
time.sleep(1)
divImagenesInicio = driver.find_elements(By.CLASS_NAME, 'bRMDJf.islir')
for divImageneInicio in divImagenesInicio:
    divImageneInicio.click()
divImagenesInicio = driver.find_elements(By.CLASS_NAME, 'bRMDJf.islir')
print("Length divPrincipals: " + str(len(divImagenesInicio)))

# Guarda las imagenes del Div que se le pasa por parámetro
getData = Images()
response = getData.divPrincipalSaveImage(divImagenesInicio)
print(response)

"""
Divs secundarios
"""
# Recupera el array con todos los div/urls para la busqueda de imagenes
time.sleep(1)
# Recorrer con click div para carga correcta de atiqueta <a>
divImagenesDivSecundarios = driver.find_elements(By.CLASS_NAME, 'isv-r.PNCib.MSM1fd.BUooTd')

divImagenesDivSecundarios = driver.find_elements(By.CLASS_NAME, 'isv-r.PNCib.MSM1fd.BUooTd')

urlGoogle = 'https://www.google.com.mx'

getUrlsSec = ScrapingNavsSecundarios()
urlsSec = getUrlsSec.getUrlsDivImagenes(divImagenesDivSecundarios)

for urlSec in urlsSec:
    # Se navega a nueva página
    driver.get(urlGoogle + urlSec)
    time.sleep(1)

    # Busqueda de div secundario, el cual contien las imagenes a guardar
    time.sleep(1)
    divImagenesInicio = driver.find_elements(By.CLASS_NAME, 'bRMDJf.islir')
    print("Length divPrincipals: " + str(len(divImagenesInicio)))

    # Guarda las imagenes del Div que se le pasa por parámetro
    getData = Images()
    response = getData.divPrincipalSaveImage(divImagenesInicio)
    print(response)

time.sleep(10000)