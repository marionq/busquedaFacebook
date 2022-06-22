class PaginaEntity:
    def __init__(self, url_facebook, verificacion_facebook, likes, seguidores, imagen, url_sitio,fecha):
        self._url_facebook = url_facebook
        self._verificacion_facebook = verificacion_facebook
        self._likes = likes
        self._seguidores = seguidores
        self._imagen = imagen
        self._url_sitio = url_sitio
        self._fecha = fecha

    ##Getters
    @property
    def url_facebook(self):
        return self._url_facebook

    @property
    def verificacion_facebook(self):
        return self._verificacion_facebook

    @property
    def likes(self):
        return self._likes

    @property
    def seguidores(self):
        return self._seguidores

    @property
    def imagen(self):
        return self._imagen

    @property
    def url_sitio(self):
        return self._url_sitio

    @property
    def fecha(self):
        return self._fecha

    ##Setters
    @url_facebook.setter
    def url_facebook(self, url_facebook):
        self._url_facebook = url_facebook

    @verificacion_facebook.setter
    def verificacion_facebook(self, verificacion_facebook):
        self._verificacion_facebook = verificacion_facebook

    @likes.setter
    def likes(self, likes):
        self._likes = likes

    @seguidores.setter
    def seguidores(self, seguidores):
        self._seguidores = seguidores

    @imagen.setter
    def imagen(self, imagen):
        self._imagen = imagen

    @url_sitio.setter
    def url_sitio(self, url_sitio):
        self._url_sitio = url_sitio

    @fecha.setter
    def url_sitio(self, fecha):
        self._fecha = fecha