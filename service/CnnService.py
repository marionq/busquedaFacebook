import requests
import configparser

class CnnService:

    def serviceCNN(self, urlImage):
        # Config File (configFile.ini)
        config = configparser.ConfigParser()
        config.read('./config/configFile.ini')
        requestBody = {'image_url': urlImage}

        url = config["CnnService"]["url"]
        x = requests.post(url, json = requestBody)
        return x.json()