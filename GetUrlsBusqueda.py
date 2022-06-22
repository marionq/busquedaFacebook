from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import configparser

#Opciones para la navegación
from webdriver_manager.chrome import ChromeDriverManager

class GetUrlsBusqueda:

    def get_url_facebook(self, busqueda):
        # Config File (configFile.ini)
        config = configparser.ConfigParser()
        config.read('./configFile.ini')
        # Config File - [Facebook]
        usuario = config["Facebook"]["usuario"]
        password = config["Facebook"]["password"]

        stringForA = []

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://www.facebook.com/')

        # Loggin
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["inputUser"]))).send_keys(usuario)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["inputPassword"]))).send_keys(password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["butonIniSesion"]))).click()

        time.sleep(2)

        # Busqueda de Promociones MX
        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.hzawbc8m.ijkhr0an.pvl4gcvk.sgqwj88q.b1f16np4.hdh3q7d8.dwo3fsh8.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.br7hx15l.h2jyy9rg.n3ddgdk9.owxd89k7.rq0escxv.oo9gr5id.mg4g778l.buofh1pr.g5gj957u.ihxqhq3m.jq4qci2q.hpfvmrgz.lzcic4wl.l9j0dhe7.iu8raji3.l60d2q6s.dflh9lhu.hwnh5xvq.scb9dxdr.qypqp5cg.aj8hi1zk.kd8v7px7.r4fl40cc.m07ooulj.mzan44vs'))).send_keys(busqueda)
        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.hzawbc8m.ijkhr0an.pvl4gcvk.sgqwj88q.b1f16np4.hdh3q7d8.dwo3fsh8.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.br7hx15l.h2jyy9rg.n3ddgdk9.owxd89k7.rq0escxv.oo9gr5id.mg4g778l.buofh1pr.g5gj957u.ihxqhq3m.jq4qci2q.hpfvmrgz.lzcic4wl.l9j0dhe7.iu8raji3.l60d2q6s.dflh9lhu.hwnh5xvq.scb9dxdr.qypqp5cg.aj8hi1zk.kd8v7px7.r4fl40cc.m07ooulj.mzan44vs'))).send_keys(Keys.RETURN)

        urlInfGral = 'https://www.facebook.com/search/pages/?q='
        arrBusqueda = busqueda.split(' ')
        for arBusqueda in arrBusqueda:
            urlInfGral += arBusqueda + "%20"
        print(urlInfGral)
        time.sleep(2)
        driver.get(urlInfGral)

        # Se ejecuta scroll hacia abajo
        for c in range(1, 1):
            time.sleep(1)
            bajar = f'window.scrollTo(0,{c}000)'
            driver.execute_script(bajar)

        time.sleep(1)
        divsPaginas = driver.find_elements(By.CLASS_NAME, 'sjgh65i0')
        for divPaginas in divsPaginas:
            textDivPaginas = divPaginas.get_attribute('innerHTML')
            soupDivPaginas = BeautifulSoup(textDivPaginas, 'html.parser')
            urls = soupDivPaginas.findAll("a")
            for url in urls:
                href = url.get('href')

                if 'https://' in href and '[' not in href:
                    x = href.split('/')
                    stringFor = ""
                    limit = 2
                    cc = 0
                    for xC in x:
                        cc += 1
                        stringFor += xC
                        if cc > 3:
                            break
                        stringFor += "/"
                    if 'search' not in stringFor:
                        stringForA.append(stringFor)

        stringForASet = list(set(stringForA))
        driver.close()
        driver.quit()
        return stringForASet