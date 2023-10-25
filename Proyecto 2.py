#LIBRERIAS
import time

#DICCIONARIOS
users_clients = {}

#LLAMAR CLASES

#CLASES
class Inventory:
    def __init__(self):
        self.principal = []
        nmer.append(self.principal)

    def ingreso_de_datos(self):
        print("-" * 50)
        account = int(input("¿Cuantos Productos Ingresara?: "))
        print("-" * 50)

        for i in range(account):
            products = []
            print("Producto No.", i + 1)
            name_product = input("Ingrese el Nombre del Producto: ")
            idProduct = i + 1
            stock = input("Ingrese la cantidad exacta que tiene del producto: ")
            price = int(input("Ingrese el precio del producto: "))
            description = input("Ingrese la descripción del producto: ")
            print("-" * 50)
            products.append(idProduct)
            products.append(name_product)
            products.append(stock)
            products.append(price)
            products.append(description)
            self.principal.append(products)
            print("Información del producto No.", i + 1, "guardada correctamente")
            print("-" * 50)

    def ver_datos(self):
        print("-" * 100)
        titles = ["No.", "Nombre del Producto", "Cantidad", "Precio Q.", "Descripción"]
        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
        print("-" * 100)
        for product in self.principal:
            print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*product))
            print("-" * 100)

#FUNCIONES

#Funion Para el Registro de Clientes
def Registro_Clientes():
    while True:
        names = input("\nIngrese sus Nombres: ")
        last_name = input("Ingrese sus Apellidos: ")
        birth_date = input("Ingrese su Fecha de Nacimiento: ")
        email = input("Ingrese su Correo Electronico: ")
        phone = input("Ingrese su Número Telefonico: ")
        username = input("\nIngrese un Nombre de Usuario Unico: ")

        if username in users_clients:
            print("\nERROR!\nEl Nombre de Usuario ya Existe, Elija otro")
            continue

        password = input("Elige una Contraseña: ")
        confirmation = input("Confirma tu Contraseña: ")

        if password != confirmation:
            print("\nERROR!\nLas Contraseñas no Coinciden. Intente de Nuevo")
            continue

        users_clients[username] = {
            "nombres": names,
            "apellidos": last_name,
            "fecha_nacimiento": birth_date,
            "email": email,
            "no_telefonico": phone,
            "contraseña": password
        }
        print("\nRegistro Exitoso como Cliente!")
        break

#Funcion Para el Inicio de Sesion de Clientes
def Iniciar_Sesion_Cliente():
    username = input("Ingrese su Nombre de Usuario: ")
    password = input("Ingrese su Contraseña: ")

    if username in users_clients:
        usuario = users_clients[username]
        if usuario["contraseña"] == password:
            print("\nIniciando Sesión como Cliente:", usuario["nombres"], usuario["apellidos"])
        else:
            print("\nERROR!\nNombre de Usuario o Contraseña Incorrectos")
    else:
        print("\nERROR!\nNombre de Usuario no Encontrado.")

#Funcion para Mostrar la Informacion de los Clientes
def Administracion_Clientes():
    print("Datos Completos de Clientes Registrado")
    if not users_clients:
        print("No hay clientes Registrados")
    else:
        for username, info in users_clients.items():
            print("\nNombre de Usuario:", username)
            print("Nombres:", info["nombres"])
            print("Apellidos:", info["apellidos"])
            print("Fecha de Nacimiento:", info["fecha_nacimiento"])
            print("Correo Electrónico:", info["email"])
            print("Número Telefónico:", info["no_telefonico"])
            print("Contraseña:", info["contraseña"])

    while True:
        print("Oprime 0 para Regresar al Menú Princiapal")
        option = input("\nDesea Enviar Nuevas Promociones a los Clientes (S/N): ")

        if option.lower() == "s" or option.upper() == "S" or option.lower() == "si" or option.upper() == "SI":
            print("\nOPCIONES")
            print("1-. Por Medio de Número Telefonico")
            print("2-. Por Medio de Correo Electronico")
            print("3-. Regresar al Menú Principal")

            option = int(input("Ingrese el Número de la Opción que Desea: "))

            if option == 1:
                while True:
                    print("\nPor Medio de Número Telefonico")
                    header = input("Ingrese el Encabezado del Mensaje: ")
                    description = input("Ingrese la Descripcion de la Promocion: ")

                    print("\nEl Mensaje se vera Asi: ")
                    print(header)
                    print(description)

                    option2 = input("Confirmar Mensaje (S/N): ")

                    if option2.lower() == "s" or option2.upper() == "S" or option2.lower() == "si" or option2.upper() == "SI":
                        tiempo_espera = 5
                        for tiempo_restante in range(tiempo_espera, -1, -1):
                            print("\rLos Mensajes Seran Enviados en {} segundos".format(tiempo_restante), end='')
                            time.sleep(1)

                        print("\nTodos Los Mensajes han Sido Enviados con Exito")

                    elif option2.lower() == "n" or option2.upper() == "N" or option2.lower() == "no" or option2.upper() == "NO":
                        print("Ingrese Nuevamente el Mensaje\n")
                        break

                    else:
                        print("Opcion Invalida")
                        print("Intente de Nuevo")

            elif option == 2:
                while True:
                    print("\nPor Medio de Correo Electronico")
                    header = input("Ingrese el Encabezado del Correo: ")
                    description = input("Ingrese la Descripcion de la Promocion: ")

                    print("\nEl Correo Electronico se vera Asi: ")
                    print(header)
                    print(description)

                    option2 = input("Confirmar Correo Electronico (S/N): ")

                    if option2.lower() == "s" or option2.upper() == "S" or option2.lower() == "si" or option2.upper() == "SI":
                        tiempo_espera = 5
                        for tiempo_restante in range(tiempo_espera, -1, -1):
                            print("\rLos Correos Electronicos Seran Enviados en {} segundos".format(tiempo_restante), end='')
                            time.sleep(1)

                        print("\nTodos Los Mensajes han Sido Enviados con Exito")

                    elif option2.lower() == "n" or option2.upper() == "N" or option2.lower() == "no" or option2.upper() == "NO":
                        print("Ingrese Nuevamente el Mensaje\n")
                        break

                    else:
                        print("Opcion Invalida")
                        print("Intente de Nuevo")

        elif option == 3:
            break


predetermined = "FASTFOOD023"

while True:
    print("---------------------------------------")
    print("--------BIENVENIDOS A FASTFOOD---------")
    print("---------------------------------------")
    print("1-. Hacer Pedido")
    print("2-. Salir del Programa")
    print("-" * 50)
    position = int(input("Ingrese el Número de la Opción que Desee: "))
    print("-" * 50)

    if position == 0:
        #La contraseña administrativa es FASTFOOD023
        password = input("Ingrese Contraseña Administrativa: ")

        if password == predetermined:
            full_name = input("Ingrese su Nombre Completo: ")
            print("-" * 50)
            print("-----------BIENVENID@", full_name, "-----------")
            print("----------------¿Que desea hacer?-----------------")
            print("-" * 50)
            print("1-. Ingresar Producto al Inventario")
            print("2-. Visualizar el Inventario")
            print("3-. Cambiar algún Dato de un Producto")
            print("4-. Agregar Productos al Inventario")
            print("5-. Eliminar Producto del Inventario")
            print("6-. Administracion de Clientes")
            print("0-. Regresar al Menú Principa")
            print("-" * 50)
            option = int(input("Ingrese el Número de la Opción que Desee: "))

            while True:
                if option == 1:
                    print("Ingresar Producto al Inventario")

                elif option == 2:
                    print("Visualizar el Inventario")

                elif option == 3:
                    print("Cambiar algún Dato de un Producto")

                elif option == 4:
                    print("Agregar Productos al Inventario")

                elif option == 5:
                    print("Eliminar Producto del Inventario")

                elif option == 6:
                    Administracion_Clientes()

                elif option == 0:
                    break

                else:
                    print("Opcion Invalida")
                    print("Intente de Nuevo")

    if position == 1:
        while True:
            print("\nBIENVENID@")
            print("1-. Registarme")
            print("2-. Iniciar Sesion")
            print("3-. Invitado")
            print("4-. Regresar al Menú Principal")
            print("5-. Salir del Programa")
            option = int(input("Ingrese el Número de la Opción que Desee: "))

            if option == 1:
                Registro_Clientes()

            elif option == 2:
                Iniciar_Sesion_Cliente()

            elif option == 3:
                print("MODO INVITADO")

            elif option == 4:
                break

            elif option == 5:
                print("Gracias Por Utilizar Nuestro Programa")
                exit()

            else:
                print("Opcion Invalida")
                print("Intente de Nuevo")

    elif option == 2:
        print("Gracias por Utilizar Nuestro Programa")
        exit()

    else:
        print("Opcion Invalida")
        print("Intente de Nuevo")