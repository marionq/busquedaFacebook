import base64
import urllib.request
from bs4 import BeautifulSoup
from datetime import date, time, datetime

class Images:

    def getTypeDataImage(self, stringBase64):
        split1 = stringBase64.split(",")
        split2 = split1[0].split("/")
        split3 = split2[1].split(";")
        tipoImage = split3[0]
        data = split1[1]
        return {'tipo': tipoImage, 'data': data}

    def saveImageBase64(self, nameImage, data):
        with open('./images/' + nameImage, 'wb') as f:
            f.write(base64.b64decode(data))
        return "Image saved"

    def saveImageUrl(self, nameImage, url):
        urllib.request.urlretrieve(url,'./images/' + nameImage)
        return "Image saved"

    def divPrincipalSaveImage(self, divImagenesInicio):
        cc = 1
        today = datetime.now()
        for divImagene in divImagenesInicio:
            divImageneText = divImagene.get_attribute('innerHTML')
            divImageneSoup = BeautifulSoup(divImageneText, 'html.parser')
            imgVerTodos = divImageneSoup.findAll("img")
            stringFindSrc = str(imgVerTodos[0].get('src'))
            if len(stringFindSrc) <= 4:
                stringFindSrc = str(imgVerTodos[0].get('data-src'))
                print(f'Imagen{cc} : {stringFindSrc}')
                cc += 1
            else:
                print(f'Imagen{cc} : {stringFindSrc}')
                if stringFindSrc[0:5] == 'data:':
                    imageL = self.getTypeDataImage(stringFindSrc)
                    fecha = str(today.strftime('%Y%m%d_%H%M%S'))
                    self.saveImageBase64(f'{cc}_{fecha}.{imageL["tipo"]}', imageL['data'])
                elif stringFindSrc[0:5] == 'https':
                    self.saveImageUrl(f'{cc}_{fecha}.png', stringFindSrc)
                cc += 1
        return f'Images saved'