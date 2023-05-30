# Clase hija de Contacto para contactos personales
#nuevo comentario
from Contacto import Contacto


class ContactoPersonal(Contacto):
    def __init__(self, nombre, telefono, empresa, cargo, whatsapp=None, facebook=None, instagram=None):
        super().__init__(nombre, telefono, empresa, cargo, whatsapp, facebook, instagram)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Personal")