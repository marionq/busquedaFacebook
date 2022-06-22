import requests
import configparser

class MailSenderService:

    def simpleMail(self, requestSimpleMail):
        # Config File (configFile.ini)
        config = configparser.ConfigParser()
        config.read('./config/configFile.ini')

        url = config["MailSenderService"]["url"]
        x = requests.post(url, json = requestSimpleMail)
        return "Envio exitoso"