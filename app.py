from flask import Flask, request
from GetUrlsBusqueda import GetUrlsBusqueda
from GetInfBusqueda import GetInfBusqueda
from flask import jsonify

from config import config

# app Flask
app = Flask(__name__)


@app.route('/busqueda-facebook', methods=['POST'])
def busquedaFacebook():
    # urls = ["https://www.facebook.com/Recompensa-MX-104904185515071", "https://www.facebook.com/losdel1al10","https://www.facebook.com/Recompensas-MX-114057707972213"]
    try:
        requestBusqueda = request.json
        findUrl = GetUrlsBusqueda()
        urls = findUrl.get_url_facebook(requestBusqueda['busqueda'])
        getInf = GetInfBusqueda()
        inf = getInf.get_inf_facebook(urls)

        return jsonify(inf)
    except Exception as ex:
        return ex


def pagina_no_encontrada(error):
    return "<h1>La página a la que intentas acceder no existe....</h1>", 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(port=5000)
    app.run(host='0.0.0.0', debug=True)
