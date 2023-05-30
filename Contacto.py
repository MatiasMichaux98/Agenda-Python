# Clase Padre para contactos (Herencia)
import py as py


class Contacto:
    def __init__(self, id, nombre, telefono, empresa, cargo, whatsapp=None, facebook=None, instagram=None):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._empresa = empresa
        self._cargo = cargo
        self._whatsapp = whatsapp
        self._facebook = facebook
        self._instagram = instagram

    def mostrar_informacion(self):
        print("ID:", self._id)
        print("nombre:", self._nombre)
        print("telefono:", self._telefono)
        print("empresa:", self._empresa)
        print("cargo:", self._cargo)
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




# Getters y
    @property
    def getid(self):
        return self._id

    @getid.setter
    def set_id(self, id):
       self._id = id
    @property
    def getnombre(self):
      return self._nombre

    @getnombre.setter
    def setnombre(self, nombre):
       self._nombre = nombre

    @property
    def gettelefono(self):
     return self._telefono

     @gettelefono.setter
     def set_telefono(self, telefono):
        self._telefono = telefono

    @property
    def getempresa(self):
     return self._empresa

    @getempresa.setter
    def set_empresa(self, empresa):
     self._empresa = empresa

    @property
    def getcargo(self):
     return self._cargo

    @getcargo.setter
    def set_cargo(self, cargo):
       self._cargo = cargo


    @property
    def getwhatsapp(self):
     return self._whatsapp

    @getwhatsapp.setter
    def set_whatsapp(self, whatsapp):
     self._whatsapp = whatsapp

    @property
    def getfacebook(self):
      return self._facebook

    @getfacebook.setter
    def set_facebook(self, facebook):
      self._facebook = facebook

    @property
    def getinstagram(self):
      return self._instagram

    @getinstagram.setter
    def set_instagram(self, instagram):
      self._instagram = instagram

