# Clase hija de Contacto para contactos profesionales
from Contacto import Contacto


class ContactoProfesional(Contacto):
    def __init__(self,id,nombre, telefono, empresa, cargo, edad, correo, whatsapp, facebook, instagram):
        super().__init__(id, nombre, telefono, empresa, cargo)
        self._edad = edad
        self._correo = correo
        self._whatsapp = whatsapp
        self._facebook = facebook
        self._instagram = instagram


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Edad:", self._edad)
        print("Correo:", self._correo)
        print("whatsapp:", self._whatsapp)
        print("facebook:", self._facebook)
        print("instagram:", self._instagram)

    def contactar(self):
        print("Contactando a", self._nombre)
        if self._whatsapp:
            print("WhatsApp:", self._whatsapp)
        if self._facebook:
            print("Facebook:", self._facebook)
        if self._instagram:
            print("Instagram:", self._instagram)
        if self._telefono:
            print("Teléfono:", self._telefono)

    @property
    def getedad(self):
        return self._edad

    @getedad.setter
    def set_edad(self, edad):
        self._edad = edad

    @property
    def getcorreo(self):
        return self._correo

    @getcorreo.setter
    def set_id(self, correo):
        self._correo = correo

    @property
    def getwhatsapp(self):
        return self._whatsapp

    @getcorreo.setter
    def set_whatsapp(self, whatsapp):
        self._whatsapp = whatsapp

    @property
    def getfacebook(self):
        return self._facebook

    @getcorreo.setter
    def set_facebook(self, facebook):
        self._facebook = facebook

    @property
    def getcorreo(self):
        return self._correo

    @getcorreo.setter
    def set_instagram(self, instagram):
        self._instagram = instagram


