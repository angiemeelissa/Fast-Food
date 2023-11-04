#LIBRERIAS
#import time

import time

#DICCIONARIOS
users_clients = {}

#CLASES
#Clase para la administracion e inventario
class Inventory:
    def __init__(self):
        self.principal = []

    def Ingreso_Producto_Inventario(self):
        print("-" * 50)
        account = int(input("¿Cuantos Productos Ingresara?: "))
        print("-" * 50)

        for i in range(account):
            products = []
            print("Producto No.", i + 1)
            name_product = input("Ingrese el Nombre del Producto: ")
            idProduct = i + 1
            stock = input("Ingrese la Cantidad Exacta que Tiene del Producto: ")
            price = int(input("Ingrese el Precio del Producto: "))
            description = input("Ingrese la Descripción del Producto: ")
            print("-" * 50)
            products.append(idProduct)
            products.append(name_product)
            products.append(stock)
            products.append(price)
            products.append(description)
            self.principal.append(products)
            print("Información del Producto No.", i + 1, "Guardada Correctamente")
            print("-" * 50)

    def Ver_Inventario(self):
        print("-" * 100)
        titles = ["No.", "Nombre del Producto", "Cantidad", "Precio Q.", "Descripción"]
        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
        print("-" * 100)
        for product in self.principal:
            print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*product))
            print("-" * 100)

    def Cambio_de_Datos(self):
        while True:
            print("-" * 50)
            print("¿Que Dato Desea Cambiar?")
            print("1-. Nombre")
            print("2-. Cantidad del Producto")
            print("3-. Precio")
            print("4-. Descripción")
            print("5-. Ver Actualizaciones")
            print("6-. Regresar al Menú Anterior")
            print("7-. Salir del Programa")

            print("-" * 50)
            challenge = int(input("Ingrese el Número de la Opcion que Desea Actualizar: "))


            if challenge == 1:
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["No.", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                        print("-" * 100)

                        confirm = int(input("¿Desea Cambiar Nombre del Producto?\n 1. Si\n 2. No\n"))
                        print("-" * 50)

                        if confirm == 1:
                            new = input("Ingrese el Nuevo Nombre del Producto: ")
                            print("-" * 50)

                            self.principal[position][1] = new
                            print("Datos Actualizados Correctamente")
                            break
                        else:
                            print("El Dato no Fue Cambiado")
                            print("-" * 50)

                    else:
                        print("Producto no Encontrado, Asegurese de que el Producto Exista")
                        print("-" * 50)

            if challenge == 2:
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                        print("-" * 100)

                        confirm = int(input("¿Desea Cambiar la Cantidad que Tiene del Producto?\n 1. Si\n 2. No\n"))
                        print("-" * 50)

                        if confirm == 1:
                            new = input("Ingrese la Nueva Cantidad que Tiene del Producto: ")
                            print("-" * 50)

                            self.principal[position][2] = new
                            print("Datos Actualizados Correctamente")
                            break
                        else:
                            print("El Dato no Fue Cambiado")
                            print("-" * 50)
                    else:
                        print("Producto no Encontrado, Asegurese de que el Producto Exista")
                        print("-" * 50)

            if challenge == 3:
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                        print("-" * 100)

                        confirm = int(input("¿Desea Cambiar el Precio del Producto?\n 1. Si\n 2. No\n"))
                        print("-" * 50)

                        if confirm == 1:
                            new = input("Ingrese el Nuevo Precio del Producto: ")
                            print("-" * 50)

                            self.principal[position][3] = new
                            print("Datos Actualizados Correctamente")
                            break
                        else:
                            print("El Dato no Fue Cambiado")
                            print("-" * 50)

                    else:
                        print("Producto no Encontrado, Asegurese de que el Producto Exista")
                        print("-" * 50)

            if challenge == 4:
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                        print("-" * 100)

                        confirm = int(input("¿Desea Cambiar la Descripción del Producto?\n 1. Si\n 2. No\n"))
                        print("-" * 50)

                        if confirm == 1:
                            new = input("Ingrese la Nueva Descripción del Producto: ")
                            print("-" * 50)

                            self.principal[position][4] = new
                            print("Datos Actualizados Correctamente")
                            break
                        else:
                            print("El Dato no Fue Cambiado")
                            print("-" * 50)

                    else:
                        print("Producto no Encontrado, Asegurese de que el Producto Exista")
                        print("-" * 50)

            elif challenge == 5:
                print("Sus actualizaciones quedaron de la siguiente manera: ")
                self.Ver_Inventario()

            elif challenge == 6:
                print("Datos Cambiados Correctamente")
                break

            else:
                print("Gracias Por Utilizar Nuestro Programa")
                exit()

    def Eliminar_Producto(self):
        print("-" * 50)
        id = int(input("Ingrese Número del Producto que Desea Eliminar: "))
        print("-" * 50)
        for x in self.principal:
            if x[0] == id:
                self.principal.remove(x)
                print("El Producto se Elimino del Inventario con los  Siguientes Datos:")
                print("-" * 100)
                titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                print("-" * 100)
                return
            else:
                print("Producto no Encontrado, Asegurese de que el Producto Exista")
                print("-" * 50)

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
    while True:
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

        option = input("\nDesea Enviar Nuevas Promociones a los Clientes (S/N): ")


        if option.lower() == "s" or option.upper() == "S" or option.lower() == "si" or option.upper() == "SI":
            while True:
                print("\nOPCIONES")
                print("1-. Por Medio de Número Telefonico")
                print("2-. Por Medio de Correo Electronico")
                print("3-. Regresar al Menú Principal")

                option = int(input("Ingrese el Número de la Opción que Desea: "))

                if option == 1:
                    print("\nPor Medio de Número Telefonico")
                    header = input("Ingrese el Encabezado del Mensaje: ")
                    description = input("Ingrese la Descripcion de la Promocion: ")
                    print("\nEl Mensaje se vera Asi: ")
                    print(header)
                    print(description)

                    option2 = input("Confirmar Mensaje (S/N): ")

                    if option2.lower() == "s" or option2.upper() == "S" or option2.lower() == "si" or option2.upper() == "SI":
                        print("\nTodos Los Mensajes han Sido Enviados con Exito")

                    elif option2.lower() == "n" or option2.upper() == "N" or option2.lower() == "no" or option2.upper() == "NO":
                        print("Ingrese Nuevamente el Mensaje\n")

                    else:
                        print("Opcion Invalida")
                        print("Intente de Nuevo")

                elif option == 3:
                    return

                else:
                    print("Opcion Invalida")
                    print("Intente de Nuevo")

#Llamar a las clases
Administration = Inventory()

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
            while True:
                print("-" * 50)
                print("----------------BIENVENID@", full_name, "-----------------")
                print("----------------¿Que desea hacer?-----------------")
                print("-" * 50)
                print("1-. Ingresar Producto al Inventario")
                print("2-. Ver el Inventario")
                print("3-. Cambiar algún Dato de un Producto")
                print("4-. Eliminar Producto del Inventario")
                print("5-. Administracion de Clientes")
                print("6-. Regresar al Menú Principal")
                print("7-. Salir del Programa")
                print("-" * 50)
                option = int(input("Ingrese el Número de la Opción que Desee: "))
                if option == 1:
                    Administration.Ingreso_Producto_Inventario()

                elif option == 2:
                    Administration.Ver_Inventario()

                elif option == 3:
                    Administration.Cambio_de_Datos()

                elif option == 4:
                    Administration.Eliminar_Producto()

                elif option == 5:
                    Administracion_Clientes()

                elif option == 6:
                    print("Inventario Registrado Crorrectamente")
                    break

                elif option == 7:
                    print("Gracias Por Utilizar Nuestro Programa")
                    exit()

                else:
                    print("Opcion Invalida")
                    print("Intente nuevamente")

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
                print("Gracias por su Compra")
                break

            elif option == 5:
                print("Gracias Por Utilizar Nuestro Programa")
                exit()

            else:
                print("Opcion Invalida")
                print("Intente de Nuevo")

    elif position == 2:
        print("Gracias por Utilizar Nuestro Programa")
        exit()

    else:
        print("Opcion Invalida")
        print("Intente de Nuevo")

#AGREGAR PEDIDOS A LA COLA
import queue

class Pedido:
    def __init__(self, plato, cantidad):
        self.plato = plato
        self.cantidad = cantidad
        self.tiempo_creacion = time.time()

cola_pedidos = queue.Queue()
pedidos_procesados = []

def agregar_pedido():
    plato = input("Ingrese el nombre del plato o producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    pedido = Pedido(plato, cantidad)
    cola_pedidos.put(pedido)
    print(f"Pedido de {cantidad} {plato} agregado a la cola.")

def procesar_pedido():
    if not cola_pedidos.empty():
        pedido = cola_pedidos.get()
        pedido.tiempo_procesado = time.time()
        pedidos_procesados.append(pedido)
        print(f"Pedido de {pedido.cantidad} {pedido.plato} procesado.")

def mostrar_pedidos_pendientes():
    print("Pedidos pendientes:")
    for pedido in list(cola_pedidos.queue):
        print(f"{pedido.cantidad} {pedido.plato}")

def calcular_tiempo_promedio_espera():
    if not pedidos_procesados:
        print("Aún no se han procesado pedidos.")
    else:
        total_tiempo_espera = 0
        for pedido in pedidos_procesados:
            total_tiempo_espera += pedido.tiempo_procesado - pedido.tiempo_creacion

        if pedidos_procesados:
            promedio_tiempo_espera = total_tiempo_espera / len(pedidos_procesados)
            print(f"Tiempo promedio de espera: {promedio_tiempo_espera:.2f} segundos")
        else:
            print("No hay pedidos procesados aún.")
while True:
    print("Menú:")
    print("1. Agregar Pedido")
    print("2. Procesar Pedido")
    print("3. Mostrar lista de pedidos pendientes")
    print("4. Calcular tiempo promedio de espera")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pedido()
    elif opcion == "2":
        procesar_pedido()
    elif opcion == "3":
        mostrar_pedidos_pendientes()
    elif opcion == "4":
        calcular_tiempo_promedio_espera()
    elif opcion == "0":
        break
    else:
        print("Opción no válida")

#DARLE UN NÚMERO A CADA CLIENTE

cola_de_clientes = queue.Queue()

def agregar_clientes(numero):
    for x in range(numero):
        cola_de_clientes.put(numero)
        print("Se ha agregado a la fila el cliente: ", (x + 1))

def atender_clientes():
    numero = 0
    while not cola_de_clientes.empty():
        numero = numero + 1
        try:
            cliente = cola_de_clientes.get(block=False)
            print(f"El Cliente {numero} Fue Atendido")
        except queue.Empty:
            print("La cola de clientes está vacía.")
            break

numero = int(input("Ingrese El Número De Clientes:"))

numero_nuevo = 0
for x in range(1, numero + 1):
    numero_nuevo = numero_nuevo + 1

agregar_clientes(numero_nuevo)
print("")
atender_clientes()
