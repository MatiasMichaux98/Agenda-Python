# Clase hija de Contacto para contactos profesionales
from Contacto import Contacto


class ContactoProfesional(Contacto):
    def __init__(self, nombre, telefono, empresa, cargo,edad,correo,whatsapp, facebook,instagram):
        super().__init__(nombre, telefono, empresa, cargo, whatsapp, facebook,instagram)
        self._edad = edad
        self._correo = correo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Edad:", self._edad)
        print("Correo:", self._correo)
        print("Tipo: Profesional")

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
