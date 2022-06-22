from bs4 import BeautifulSoup

class ScrapingNavsSecundarios:
    def getUrlsDivImagenes(self, divImagenesDivSecundarios):
        urlsImagenes = []

        print("Length divImagenesDivSecundarios: " + str(len(divImagenesDivSecundarios)))

        for divImageneDivSecundarios in divImagenesDivSecundarios:
            textdivImagenesDivSecundarios = divImageneDivSecundarios.get_attribute('innerHTML')
            soupdivImagenesDivSecundarios = BeautifulSoup(textdivImagenesDivSecundarios, 'html.parser')
            url = soupdivImagenesDivSecundarios.findAll("a", {"class": "wXeWr islib nfEiy"})
            href = url[0].get('href')
            urlsImagenes.append(href)
        return urlsImagenes