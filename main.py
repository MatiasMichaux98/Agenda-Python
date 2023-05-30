import psycopg2
import colorama
from colorama import Fore, Style, Back  # cambia el menu de color
from contactoPersonal import *
from ContactoProfesional import *

# Inicializar colorama

colorama.init()

# Conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    user='postgres',
    host="127.0.0.1",
    port="5432",
    database="agenda.db",
    password="admin"
)

cursor = conexion.cursor()

conexion.commit()


# Función para agregar un contacto a la base de datos
def agregar_contacto(contacto):
    cursor.execute('''
        INSERT INTO contactos (nombre, telefono, empresa, cargo,  whatsapp, facebook, instagram)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    ''', (contacto.getnombre, contacto.gettelefono, contacto.getempresa, contacto.getcargo, contacto.getwhatsapp
        , contacto.getfacebook,contacto.getwhatsapp))
    contacto.id = cursor.fetchone()[0]
    conexion.commit()
    print("Contacto agregado exitosamente.")

def agregar_contacto2(Contacto2):
    cursor.execute('''
        INSERT INTO contactop (nombre, telefono, empresa, cargo,edad,correo,  whatsapp, facebook, instagram)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    ''', (Contacto2.getnombre, Contacto2.gettelefono,Contacto2.getempresa, Contacto2.getcargo,Contacto2.getedad,
          Contacto2.getcorreo, Contacto2.getwhatsapp, Contacto2.getfacebook,Contacto2.getwhatsapp))
    ContactoProfesional.id = cursor.fetchone()[0]
    conexion.commit()
    print("Contacto agregado exitosamente.")


# Función para eliminar un contacto de la base de datos
def eliminar_contacto(contacto_id):
    cursor.execute('DELETE FROM contactos WHERE id = %s', (contacto_id,))
    conexion.commit()
    print("Contacto eliminado exitosamente.")


# Función para modificar un contacto en la base de datos
def modificar_contacto(contacto_id, nombre, telefono, empresa, cargo, whatsapp, facebook, instagram):
    cursor.execute('''
        UPDATE contactos
        SET nombre = %s, telefono = %s, empresa = %s, cargo = %s,  whatsapp = %s, facebook = %s, instagram = %s
        WHERE id = %s
    ''', (nombre, telefono, empresa, cargo,  whatsapp, facebook, instagram, contacto_id))
    conexion.commit()
    print("Contacto modificado exitosamente.")


# Función para agregar un evento a la base de datos
def agregar_evento(fecha, descripcion, contacto_id):
    cursor.execute('''
        INSERT INTO eventos (fecha, descripcion, contacto_id)
        VALUES (%s, %s, %s)
    ''', (fecha, descripcion, contacto_id))
    conexion.commit()
    print("Evento agregado exitosamente.")


# Función para visualizar eventos en una fecha determinada
def visualizar_eventos(fecha):
    cursor.execute('''
        SELECT contactos.nombre, eventos.descripcion
        FROM eventos
        INNER JOIN contactos ON eventos.contacto_id = contactos.id
        WHERE eventos.fecha = %s
    ''', (fecha,))
    eventos = cursor.fetchall()

    if len(eventos) > 0:
        print("Eventos para la fecha", fecha)
        for evento in eventos:
            print("Contacto:", evento[0])
            print("Descripción:", evento[1])
            print("---")
    else:
        print("No hay eventos para la fecha", fecha)

#funcion para borrar evento
def eliminar_evento_por_fecha(fecha):
    cursor.execute(" DELETE FROM eventos WHERE fecha = %s", (fecha,))
    conexion.commit()
    print("Evento eliminado exitosamente.")


# Función para buscar contactos por nombre
def buscar_contacto(nombre):
    cursor.execute("SELECT * FROM contactos WHERE nombre ILIKE %s", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if len(resultados) > 0:
        print("Resultados de búsqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron contactos con ese nombre.")


# Función para mostrar la lista de contactos
def mostrar_lista_contactos():
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    if len(contactos) > 0:
        print(Fore.YELLOW+Back.BLACK+"Lista de contactos PERSONAL:"+Style.RESET_ALL)
        for contacto in contactos:
            contacto_personal = ContactoPersonal(contacto[0],contacto[1], contacto[2], contacto[3], contacto[4], contacto[5], contacto[6])
            contacto_personal.mostrar_informacion()
            print("---")
    else:
        print("No hay contactos en la agenda.")
# Función para mostrar la lista de contactos de la otra clase
def mostrar_lista_contactos2():
    cursor.execute("SELECT * FROM contactop")
    contactop = cursor.fetchall()
    if len(contactop) > 0:
        print(Fore.YELLOW + Back.BLACK + "Lista de contactos PROFESIONAL:" + Style.RESET_ALL)
        for contacto in contactop:

            contacto_profesional = ContactoProfesional(contacto[0],contacto[1], contacto[2], contacto[3], contacto[4], contacto[5],contacto[6],contacto[7],contacto[8])
            contacto_profesional.mostrar_informacion()
            print("---")
    else:
        print("No hay contactos en la agenda.")


# Función para mostrar el menú principal

def mostrar_menu():
    print(Fore.MAGENTA+ Back.BLACK +"=== Agenda de Contactos ===" + Style.RESET_ALL)
    print(Fore.CYAN+"1. Agregar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"2. Eliminar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"3. Modificar contacto"+ Style.RESET_ALL)
    print(Fore.CYAN+"4. Agregar evento"+ Style.RESET_ALL)
    print(Fore.CYAN+"5. Visualizar eventos por fecha"+ Style.RESET_ALL)
    print(Fore.CYAN+"6. Eliminar evento" + Style.RESET_ALL)
    print(Fore.CYAN+"7. Buscar contacto por nombre"+ Style.RESET_ALL)
    print(Fore.CYAN+"8. Mostrar lista de contactos"+ Style.RESET_ALL)
    print(Fore.CYAN+"9. Salir"+ Style.RESET_ALL)


# Función para leer una opción del menú
def leer_opcion():
    while True:
        try:
            opcion = int(input(Fore.MAGENTA+ Back.BLACK +"Ingrese una opción: "+ Style.RESET_ALL))
            print("======================================")
            if opcion < 1 or opcion > 9:
                raise ValueError
            return opcion
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número del 1 al 9.")

# Función para leer una opción del segundo menú
def leer_opcion2():
    while True:
        try:
            OPC = int(input(Fore.MAGENTA+ Back.BLACK +"Ingrese una opción: "+ Style.RESET_ALL))
            print("======================================")
            if OPC < 1 or OPC > 4:
                raise ValueError
            return OPC
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
#Funcion para el segundo menu
def menu2 ():
    print(Fore.MAGENTA + Back.BLACK + "=====MENU_CONTACTO=====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Contacto Profesional" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Contacto Personal" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Volver al Menu Principal" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Salir" + Style.RESET_ALL)


# Función para capturar los datos de un contacto desde el usuario
def capturar_datos_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    empresa = input("Ingrese la empresa: ")
    cargo = input("Ingrese el cargo: ")
    whatsapp = input("Ingrese el número de WhatsApp: ")
    facebook = input("Ingrese el perfil de Facebook: ")
    instagram = input("Ingrese el perfil de Instagram: ")
    return nombre, telefono, empresa, cargo,  whatsapp, facebook, instagram
#Funcion para capturar los datos del segundo menu
def pedir_Datos_Contacto_Profesional():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    empresa = input("Ingrese la empresa: ")
    cargo = input("Ingrese el cargo: ")
    edad  = input("Ingrese su edad")
    correo = input("Ingrese su correo")
    whatsapp = input("Ingrese el número de WhatsApp: ")
    facebook = input("Ingrese el perfil de Facebook: ")
    instagram = input("Ingrese el perfil de Instagram: ")
    return nombre, telefono, empresa, cargo,edad,correo,whatsapp, facebook, instagram

# Función para capturar los datos de un evento desde el usuario
def capturar_datos_evento():
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    descripcion = input("Ingrese la descripción del evento: ")
    return fecha, descripcion


# Función para mostrar una alerta de evento
def mostrar_alerta_evento(fecha, descripcion):
    print("¡ALERTA DE EVENTO!")
    print("Fecha:", fecha)
    print("Descripción:", descripcion)
    print()

#Funcion para que al crear un contacto SE PUEDAD ELEJIR ENTRE CPROFESIONAL O PERSONAL
def datos_menu_dos():
    while True:
        menu2()
        OPC = leer_opcion2()

        if OPC == 1:
            nombre, telefono, empresa, cargo, edad, correo, whatsapp, facebook, instagram = pedir_Datos_Contacto_Profesional()
            contacto_profesional = ContactoProfesional(nombre, telefono, empresa, cargo, edad, correo, whatsapp,facebook, instagram)
            agregar_contacto2(contacto_profesional)
        elif OPC == 2:
            nombre, telefono, empresa, cargo, whatsapp, facebook, instagram = capturar_datos_contacto()
            contacto = ContactoPersonal(nombre, telefono, empresa, cargo, whatsapp, facebook, instagram)
            agregar_contacto(contacto)
        elif OPC == 3:
            ejecutar_agenda()
        elif OPC == 4:
            print("HA SALIDO DEL PROGRAMA!")
            print("HASTA LA PROXIMA AMIGO!")
            break
        else:
            print(Fore.RED+"LA OPCION QUE INGRESO ES INCORRECTA "+Style.RESET_ALL)
            print(Fore.RED+"Igrese nuevamente una opcion "+Style.RESET_ALL)

# Función para ejecutar la agenda
def ejecutar_agenda():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            datos_menu_dos()

        elif opcion == 2:
            contacto_id = int(input("Ingrese el ID del contacto a eliminar: "))
            eliminar_contacto(contacto_id)
        elif opcion == 3:

            contacto_id = int(input("Ingrese el ID del contacto a modificar: "))
            nombre, telefono, empresa, cargo, whatsapp, facebook, instagram = capturar_datos_contacto()
            modificar_contacto(contacto_id,nombre,telefono,empresa,cargo,whatsapp,facebook,instagram)
        elif opcion == 4:
            fecha, descripcion = capturar_datos_evento()
            cursor.execute('SELECT * FROM contactos')
            contactos = cursor.fetchall()
            if len(contactos) > 0:
                print("=== Contactos ===")
                for contacto in contactos:
                    print("ID:", contacto[0])
                    print("Nombre:", contacto[1])
                    print("---")
                contacto_id = int(input("Ingrese el ID del contacto asociado al evento: "))
                agregar_evento(fecha, descripcion, contacto_id)
            else:
                print("No hay contactos en la agenda. Por favor, agregue un contacto primero.")
        elif opcion == 5:
            fecha = input("Ingrese la fecha a visualizar (YYYY-MM-DD): ")
            visualizar_eventos(fecha)
        elif opcion == 6:
            fecha = (input("Digite la fecha (YYYY-MM-DD) del evento a ELIMINAR"))
            eliminar_evento_por_fecha(fecha)
        elif opcion == 7:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == 8:
            mostrar_lista_contactos()
            mostrar_lista_contactos2()
        elif opcion == 9:
            break

    conexion.close()
    print("¡Hasta la proxima!")


# Ejecutamos la agenda
ejecutar_agenda()
