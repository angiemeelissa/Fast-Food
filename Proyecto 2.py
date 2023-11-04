#DICCIONARIOS
users_clients = {}

#CLASES
#Clase para la Administracion del Inventario
class Inventory_and_Orders:

    def __init__(self):
        self.principal = [
            [1, "Hamburguesa Volcanica", 40, "Tocino y Queso", 25, "Hamburguesas"],
            [2, "Hamburguesa Tejana", 40, "BBQ", 25, "Hamburguesas"],
            [3, "Hamburguesa Bomba de Queso", 40, "3 Quesos Fundidos", 25, "Hamburguesas"],
            [4, "Pizza de Jamon", 35, "Jamon y Queso",25, "Pizzas"],
            [5, "Pizza de Pepperoni", 35 , "Pepperoni y Queso", 25, "Pizzas"],
            [6, "Pizza Hawaina", 35 , "Jamon, Queso y Piña", 25, "Pizzas"],
            [7, "Tacos al Pastor", 21, "3 x 21", 30, "Tacos"],
            [8, "Tacos de Cochito Horneado", 21, "3 x 21", 30, "Tacos"],
            [9, "Tacos de Pollo", 21, "3 x 21", 30, "Tacos"],
            [10, "Pie de Queso", 25, "Torta de Queso",15, "Postres"],
            [11, "Pie de Calabaza", 25, "Pastel de Temporada",10, "Postres"],
            [12, "Pie de Manzana", 25, "Torta de Manzana",15, "Postres"],
            [13, "Gaseosas", 10, "Todos los Sabores", 45, "Bebidas"],
            [14, "Jugo Natural", 15, "Limonada y Naranjada", 30, "Bebidas"],
            [15, "Agua Pura", 5, "Agua Pura", 15, "Bebidas"],

        ]
        self.car = []
        self.subtotal = 0.0
        self.taxes = 0.0
        self.total = 0.0

    def Ingreso_Producto_Inventario(self):
        print("-" * 50)
        account = int(input("¿Cuantos Productos Ingresara?: "))
        print("-" * 50)

        for i in range(account):
            products = []
            print("Producto No.", len(self.principal) + 1)
            name_product = input("Ingrese el Nombre del Producto: ")
            idProduct = len(self.principal) + 1
            price = int(input("Ingrese el Precio del Producto: "))
            description = input("Ingrese la Descripción del Producto: ")
            stock = input("Ingrese la Cantidad Exacta que Tiene del Producto: ")
            categoria = input("Ingrese la categoria del producto: ")

            print("-" * 50)
            products.append(idProduct)
            products.append(name_product)
            products.append(price)
            products.append(description)
            products.append(stock)
            products.append(categoria)
            self.principal.append(products)
            print("Información del Producto No.", len(self.principal), "Guardada Correctamente")
            print("-" * 50)

    def Ver_Inventario_Clientes(self, category=None):
        print("-" * 80)
        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción"]
        print("{:<15} {:<30} {:<10} {:<15}".format(*titles))
        print("-" * 80)
        for product in self.principal:
            if category is None or product[5] == category:
                print("{:<15} {:<30} {:<10} {:<15}".format(product[0], product[1], product[2], product[3]))
                print("-" * 80)

    def Ver_Inventario(self):
        print("-" * 100)
        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
        print("-" * 100)
        for product in self.principal:
            print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*product))
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
            challenge = input("Ingrese el Número de la Opcion que Desea Actualizar: ")


            if challenge == "1":
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

            if challenge == "2":
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

                        confirm = input("¿Desea Cambiar la Cantidad que Tiene del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
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

            if challenge == "3":
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

                        confirm = input("¿Desea Cambiar el Precio del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
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

            if challenge == "4":
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

                        confirm = input("¿Desea Cambiar la Descripción del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
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

            elif challenge == "5":
                print("Sus actualizaciones quedaron de la siguiente manera: ")
                self.Ver_Inventario()

            elif challenge == "6":
                print("Datos Cambiados Correctamente")
                break

            elif challenge == "7":
                print("Gracias Por Utilizar Nuestro Programa")
                exit()

            else:
                print("\n------------------Opcion Invalida-----------------")
                print("-----------------Intente Nuevamente---------------\n")

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

    def agregar_producto_carrito(self):
        print("-" * 50)
        id = int(input("Ingrese Número del Producto que Desea agregar al carrito: "))
        print("-" * 50)

        found = False  # Variable para rastrear si se encontró el producto

        for x in self.principal:
            if x[0] == id:
                found = True
                position = self.principal.index(x)
                print("Los datos son:")
                print("-" * 100)
                titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                print("-" * 100)

                amount = int(input("Ingrese la Cantidad que Desea del Producto: "))
                if amount <= int(x[2]):
                    self.principal[position][2] = str(int(x[2]) - amount)
                    self.car.append((x[0], x[1], amount, x[3] * amount))
                    print("Producto agregado al carrito correctamente")
                else:
                    print("No hay suficiente cantidad disponible del producto")
                break

        if not found:
            print("Producto no Encontrado, Asegúrese de que el Producto Exista")

    def Ver_carro(self):
        print("-" * 100)
        print("No. de Carrito", "Numero")
        print("-" * 100)
        titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q."]
        print("{:<15} {:<30} {:<10} {:<10}".format(*titles))
        print("-" * 100)
        for product in self.car:
            print("{:<15} {:<30} {:<10} {:<10}".format(*product))
            print("-" * 100)

    def Eliminar_Producto_del_carrito(self):
        print("-" * 50)
        id = int(input("Ingrese Número del Producto que Desea Eliminar: "))
        print("-" * 50)
        for x in self.car:
            if x[0] == id:
                self.car.remove(x)
                print("El Producto se Elimino del Inventario con los  Siguientes Datos:")
                print("-" * 100)
                titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                print("-" * 100)
                return
            else:
                print("Producto No Encontrado, Asegurese de que el Producto Exista")
                print("-" * 50)

    def sumar_producto_al_carrito(self):
        print("-" * 50)
        id = int(input("Ingrese el Número del Producto, para Sumarle Producto a la Cantidad que ya Tenia: "))
        print("-" * 50)
        for x in self.car:
            if x[0] == id:
                position = self.car.index(x)
                print("Los Datos son:")
                print("-" * 100)
                titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                print("-" * 100)

                add = int(input("¿Desea Sumarle Producto a la Cantidad que ya Tenia?\n 1. Si\n 2. No\n"))

                if add == 1:
                    new = int(input("Ingrese la Cantidad que Desea Sumar: "))
                    print("-" * 50)

                    variable = int(x[2])
                    modification = variable + new
                    self.car[position][2] = str(modification)
                    print("Datos Actualizados Correctamente")
                    print("La Cantidad de Producto que Tiene Ahora es:", modification)
                    break

                if add == 2:
                    print("Gracias...")
                    break
            else:
                print("Producto no Encontrado, Asegurese de que el Producto Exista")
                print("-" * 50)

    def restar_producto_al_carrita(self):
        print("-" * 50)
        id = int(input("Ingrese el Número del Producto, para Restarle Producto a la Cantidad que ya Tenia: "))
        print("-" * 50)
        for x in self.car:
            if x[0] == id:
                position = self.car.index(x)
                print("Los Datos son:")
                print("-" * 100)
                titles = ["ID Producto", "Nombre", "Cantidad", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<10} {:<15}".format(*x))
                print("-" * 100)

                add = int(input("¿Desea Restarle Producto a la Cantidad que ya Tenia?\n 1. Si\n 2. No\n"))

                if add == 1:
                    new = int(input("Ingrese la Cantidad que Desea Restar: "))
                    print("-" * 50)

                    variable = int(x[2])
                    modification = variable - new
                    self.car[position][2] = str(modification)
                    print("Datos Actualizados Aorrectamente")
                    print("La Aantidad de Producto que Tiene Ahora es:", modification)
                    break

                if add == 2:
                    print("Gracias...")
                    break
            else:
                print("Producto no Encontrado, Asegurese de que el Producto Exista")
                print("-" * 50)

    def Impuesto(self):
        suma = sum(producto[3] for producto in self.car)
        self.taxes = suma * 0.12
        print("IMPUESTO (12%): Q.", self.taxes)
        print("-" * 100)

    def Sub_total(self):
        self.subtotal = sum(producto[3] for producto in self.car)
        print("SUBTOTAL: Q.", self.subtotal)
        print("-" * 100)

    def total(self):
        self.total = self.subtotal + self.taxes
        print("TOTAL Q.", self.total)
        print("-" * 100)

#FUNCIONES
#Funion Para el Registro de Clientes
def Registro_Clientes():
    while True:
        print("\n--------------BIENVENIDOS A FASTFOOD--------------")
        print("\nIngrese sus Datos a Continuacion:")
        names = input("Ingrese sus Nombres: ")
        last_name = input("Ingrese sus Apellidos: ")
        birth_date = input("Ingrese su Fecha de Nacimiento (DD/MM/AA): ")
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
        print("\n----------Registro Exitoso como Cliente!----------")
        break

#Funcion Para el Inicio de Sesion de Clientes
def Iniciar_Sesion_Cliente():
    username = input("Ingrese su Nombre de Usuario: ")
    password = input("Ingrese su Contraseña: ")
    print("-" * 50)

    if username in users_clients:
        usuario = users_clients[username]
        if usuario["contraseña"] == password:
            print("\nIniciando Sesión como Cliente:", usuario["nombres"], usuario["apellidos"])
        else:
            print("\n----------------------ERROR!----------------------")
            print("----Nombre de Usuario o Contraseña Incorrectos----")
    else:
        print("\n----------------------ERROR!----------------------")
        print("----------Nombre de Usuario no Encontrado---------")

#Funcion para Mostrar la Informacion de los Clientes
def Administracion_Clientes():
    while True:
        if not users_clients:
            print("\n------------No Hay Clientes Registrados-----------")
            return
        else:
            print("\n------Datos Completos de Clientes Registrados-----")
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
                print("\n---------------------OPCIONES---------------------")
                print("\n1-. Por Medio de Número Telefonico")
                print("2-. Por Medio de Correo Electronico")
                print("3-. Regresar al Menú Principal\n")
                print("-" * 50)

                option = input("Ingrese el Número de la Opción que Desea: ")

                if option == "1":
                    print("\nPor Medio de Número Telefonico")
                    header = input("Ingrese el Encabezado del Mensaje: ")
                    description = input("Ingrese la Descripcion del Mensaje: ")
                    print("\nEl Mensaje se vera Asi: ")
                    print(header)
                    print(description)

                    option2 = input("Confirmar Mensaje (S/N): ")

                    if option2.lower() == "s" or option2.upper() == "S" or option2.lower() == "si" or option2.upper() == "SI":
                        print("\nTodos Los Mensajes han Sido Enviados con Exito")

                    elif option2.lower() == "n" or option2.upper() == "N" or option2.lower() == "no" or option2.upper() == "NO":
                        print("Ingrese Nuevamente el Mensaje\n")

                    else:
                        print("\n------------------Opcion Invalida-----------------")
                        print("-----------------Intente Nuevamente---------------\n")

                elif option == "2":
                    print("\nPor Medio de Correo Electronico")
                    header = input("Ingrese el Encabezado del Correo: ")
                    description = input("Ingrese la Descripcion del Correo:  ")
                    print("\nEl Correo se vera Asi: ")
                    print(header)
                    print(description)

                    option2 = input("Confirmar Correo (S/N): ")

                    if option2.lower() == "s" or option2.upper() == "S" or option2.lower() == "si" or option2.upper() == "SI":
                        print("\nTodos los Correos Electronicos se han Enviado con Exito")

                    elif option2.lower() == "n" or option2.upper() == "N" or option2.lower() == "no" or option2.upper() == "NO":
                        print("Ingrese Nuevamente el Mensaje\n")

                    else:
                        print("\n------------------Opcion Invalida-----------------")
                        print("-----------------Intente Nuevamente---------------\n")

                elif option == "3":
                    return

                else:
                    print("\n------------------Opcion Invalida-----------------")
                    print("-----------------Intente Nuevamente---------------\n")

        elif option.lower() == "n" or option.upper() == "N" or option.lower() == "no" or option.upper() == "NO":
            return

        else:
            print("\n------------------Opcion Invalida-----------------")
            print("-----------------Intente Nuevamente---------------\n")

#Llamar a las clases
Administration = Inventory_and_Orders()

def Menu_Clientes():
    print("--------------------------------------------------")
    print("\n--------------BIENVENIDOS A FASTFOOD--------------")
    print("--------------------------------------------------")
    print("\n1-. Ver Menu")
    print("2-. Ver Carrito")
    print("3-. Editar Carrito")
    print("4.- Finalizar Comprar")
    print("5.- Regresar al Menu Principal")
    print("6.- Salir del Programa\n")
    print("-" * 50)
    option = input("Ingrese el Número de la Opción que Desee: ")
    print("-" * 50)

    if option == "1":
        print("--------------------------------------------------")
        print("\n-------------------MENU FASTFOOD------------------")
        print("--------------------------------------------------")
        print("\n1-. Hamburguesas ")
        print("2-. Pizzas")
        print("3-. Tacos")
        print("4-. Postres")
        print("5-. Bebidas")
        print("6-. Combos\n")
        print("-" * 50)
        option2 = input("Ingrese el Número de la Opción que Desee: ")
        print("-" * 50)

        if option2 == "1":
            Administration.Ver_Inventario_Clientes(category="Hamburguesas")
        elif option2 == "2":
            Administration.Ver_Inventario_Clientes(category="Pizzas")
        elif option2 == "3":
            Administration.Ver_Inventario_Clientes(category="Tacos")
        elif option2 == "4":
            Administration.Ver_Inventario_Clientes(category="Postres")
        elif option2 == "5":
            Administration.Ver_Inventario_Clientes(category="Bebidas")

    elif option == "2":
        Administration.Ver_carro()



predetermined = "FASTFOOD023"

while True:
    print("\n")
    print("-" * 50)
    print("--------------BIENVENIDOS A FASTFOOD--------------")
    print("-" * 50)
    print("1-. Hacer Pedido")
    print("2-. Salir del Programa")
    print("-" * 50)
    position = input("Ingrese el Número de la Opción que Desee: ")
    print("-" * 50)

    if position == "0":
        #La contraseña administrativa es FASTFOOD023
        password = input("Ingrese Contraseña Administrativa: ")

        if password == predetermined:
            full_name = input("Ingrese su Nombre Completo: ")
            while True:
                print("-" * 50)
                print("\n--------------------BIENVENID@--------------------")
                print("--------------------------------------------------")
                print("\nIngresando Como:", full_name)
                print("\n1-. Ingresar Producto al Inventario")
                print("2-. Ver el Inventario")
                print("3-. Cambiar algún Dato de un Producto")
                print("4-. Eliminar Producto del Inventario")
                print("5-. Administracion de Clientes")
                print("6-. Regresar al Menú Principal")
                print("7-. Salir del Programa\n")
                print("-" * 50)
                option = input("Ingrese el Número de la Opción que Desee: ")
                print("-" * 50)
                if option == "1":
                    Administration.Ingreso_Producto_Inventario()

                elif option == "2":
                    Administration.Ver_Inventario()

                elif option == "3":
                    Administration.Cambio_de_Datos()

                elif option == "4":
                    Administration.Eliminar_Producto()

                elif option == "5":
                    Administracion_Clientes()

                elif option == "6":
                    break

                elif option == 7:
                    print("Esperamos que Vuelvas Pronto!")
                    exit()

                else:
                    print("\n------------------Opcion Invalida-----------------")
                    print("-----------------Intente Nuevamente---------------\n")

    if position == "1":
        while True:
            print("--------------------------------------------------")
            print("\n--------------------BIENVENID@--------------------")
            print("--------------------------------------------------")
            print("\n¿Que Desea Hacer?")
            print("1-. Registarme")
            print("2-. Iniciar Sesion")
            print("3-. Modo Invitado")
            print("4-. Regresar al Menú Principal")
            print("5-. Salir del Programa\n")
            print("-" * 50)
            option = input("Ingrese el Número de la Opción que Desee: ")
            print("-" * 50)

            if option == "1":
                Registro_Clientes()
                Menu_Clientes()

            elif option == "2":
                Iniciar_Sesion_Cliente()
                Menu_Clientes()

            elif option == "3":
                Menu_Clientes()

            elif option == "4":
                break

            elif option == "5":
                print("Gracias Por Utilizar Nuestro Programa")
                exit()

            else:
                print("\n------------------Opcion Invalida-----------------")
                print("-----------------Intente Nuevamente---------------\n")

    elif position == "2":
        print("Esperamos que Vuelvas Pronto!")
        exit()

    else:
        print("\n----------------------ERROR!----------------------")
        print("---------------Contraseña Incorrecta--------------")

