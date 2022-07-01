from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime

import time
import configparser

from CnnService import CnnService
from AnnService import AnnService
from MailSenderService import MailSenderService

# Opciones para la navegación
from webdriver_manager.chrome import ChromeDriverManager


class GetInfBusqueda:

    def get_inf_facebook(self, stringForASet):
        # Config File (configFile.ini)
        config = configparser.ConfigParser()
        config.read('configFile.ini')
        # Config File - [Facebook]
        usuario = config["Facebook"]["usuario"]
        password = config["Facebook"]["password"]
        responseNn = []

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get(config["Facebook"]["url"])

        # Loggin
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["inputUser"]))).send_keys(usuario)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["inputPassword"]))).send_keys(password)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config["PaginaInicial"]["butonIniSesion"]))).click()

        print("stringForASet: " + str(len(stringForASet)))
        time.sleep(2)

        ccc = 0
        for item in stringForASet:
            ccc += 1
            driver.get(item)
            time.sleep(2)
            # Verificación Facebook
            divPrincipals = driver.find_elements(By.CSS_SELECTOR, config["GetInfBusqueda"]["divPVerify"])
            print("divPrincipals: " + str(len(divPrincipals)))
            print("URL" + str(ccc) + ":" + item)
            print("verificación: " + str(len(divPrincipals)))
            verifyFacebook = len(divPrincipals)
            # Busqueda de URL Imagen
            time.sleep(1)
            divPrincipals = driver.find_elements(By.CLASS_NAME, config["GetInfBusqueda"]["divImage"])
            if len(divPrincipals) > 0:
                text = divPrincipals[0].get_attribute('innerHTML')
                soup = BeautifulSoup(text, 'html.parser')
                urls = soup.findAll("image")
                stringFind = str(urls[0].get('xlink:href'))
                print("URL IMAGEN: " + stringFind)
                # urllib.request.urlretrieve(stringFind,"santander_0001.png")
                urlImage = stringFind
                # Imagen base64
                # img64 = base64.b64encode(urlopen(stringFind).read())
                # print("IMAGEN base46: " + str(img64))
                # time.sleep(1000)

                # Busqueda Información General
                driver.get(item + '/about/?ref=page_internal')
                time.sleep(1)
                infsGral = driver.find_elements(By.CLASS_NAME, config["GetInfBusqueda"]["divInfGral"])
                # Validación divs de información general
                if len(infsGral) > 0:
                    textInfGral = infsGral[0].get_attribute('innerHTML')
                    soupInfGral = BeautifulSoup(textInfGral, 'html.parser')
                    spanInfGral = soupInfGral.findAll("span", class_=config["GetInfBusqueda"]["spanInfGral"])
                    cadenaDiv = str(spanInfGral[0].string)
                    likes = cadenaDiv[(cadenaDiv.find('A ') + 1):(cadenaDiv.find('persona'))]
                    likes = likes.replace(u'\xa0', u' ')
                    likes = likes.replace(" ", "")
                    # Trasfrmación en case de que número 1 de likes se encuentre en letra
                    if likes == "una":
                        likes = 1
                        print("Likes: " + str(likes))
                    else:
                        print("Likes: " + str(likes))
                    # Validar si existe span de follower, si no, se asume que es cero
                    if len(spanInfGral) > 1:
                        cadenaDiv = str(spanInfGral[2].string)
                        followers = cadenaDiv[0:(cadenaDiv.find('persona'))]
                        followers = followers.replace(u'\xa0', u' ')
                        followers = followers.replace(" ", "")
                        print("Followers: " + followers)
                        print("\n")
                    else:
                        followers = 0
                        print("Followers: " + str(followers))
                        print("\n")
                else:
                    likes = 0
                    print("Likes: " + str(likes))
                    followers = 0
                    print("Followers: " + str(followers))
                    print("\n")
            today = datetime.now()

            serviceCnn = CnnService()
            validateImage = serviceCnn.serviceCNN(urlImage)
            print(f'validateImage: {validateImage}')

            requestAnn = [{#'urlPagFacebook': item,
                             'verifyFacebook': int(verifyFacebook),
                             'likes': int(likes),
                             'followers': int(followers),
                             #'urlImage': urlImage,
                             'classImage': validateImage["className"],
                             # 'imageBase64':str(img64),
                             # 'urlSitio':'',
                             #'fecha': str(today.strftime("%d/%m/%Y %H:%M:%S"))
                }]

            serviceAnn = AnnService()
            validatePage = serviceAnn.serviceANN(requestAnn)

            if validatePage["apocrifa"] == True:
                responseNn.append({
                    'urlPagFacebook': item,
                    'apocrifa': validatePage["apocrifa"],
                    'fecha': str(today.strftime("%d/%m/%Y %H:%M:%S"))
                })

        driver.save_screenshot('django.png')
        driver.close()
        driver.quit()

        if responseNn:
            requestSimpleMail = {
                "to": ["mario.n.q@hotmail.com"],
                "subject": "Páginas Apocrifas",
                "content": responseNn[0]['urlPagFacebook']
            }

            serviceMailSender = MailSenderService()
            validatePage = serviceMailSender.simpleMail(requestSimpleMail)
            print(f'Servico Mail Sender: {validatePage}')

        return responseNn
