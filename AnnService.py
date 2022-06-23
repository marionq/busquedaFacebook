import requests
import configparser

class AnnService:

    def serviceANN(self, body):
        # Config File (configFile.ini)
        config = configparser.ConfigParser()
        config.read('configFile.ini')

        url = config["AnnService"]["url"]
        x = requests.post(url, json = body)
        return x.json()