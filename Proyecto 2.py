#IMPORTACIONES
import queue
import time

#DICCIONARIOS
users_clients = {}

#CLASES
#Clase Para La Administracion del Inventario
class Inventory_and_Orders:
    def __init__(self):
        self.principal = [[1, "Hamburguesa Volcanica", 40, "Tocino y Queso", 25, "Hamburguesas"],
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
            [15, "Agua Pura", 5, "Agua Pura", 15, "Bebidas"]]

        self.car = []
        self.administrator = []
        self.subtotal = 0
        self.taxes = 0
        self.total = 0
        self.ticket = 0
        self.line = queue.Queue()
        self.ganancias = 0
        self.iva = 0
        self.dinero = 0
        self.facturas = []

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
            categoria = input("Ingrese la categoria del producto (Hamburguesas, Pizza, Tacos, Postres, Bebidas o Combos: ")

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
                        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*x))
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
                        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*x))
                        print("-" * 100)

                        confirm = input("¿Desea Cambiar la Cantidad que Tiene del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
                            new = input("Ingrese la Nueva Cantidad que Tiene del Producto: ")
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

            if challenge == "3":
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*x))
                        print("-" * 100)

                        confirm = input("¿Desea Cambiar el Precio del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
                            new = input("Ingrese el Nuevo Precio del Producto: ")
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

            if challenge == "4":
                print("-" * 50)
                id = int(input("Ingrese Número del Producto que Desea Actualizar: "))
                print("-" * 50)
                for x in self.principal:
                    if x[0] == id:
                        position = self.principal.index(x)
                        print("Los Datos del Producto son los Siguientes:")
                        print("-" * 100)
                        titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
                        print("-" * 100)
                        print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*x))
                        print("-" * 100)

                        confirm = input("¿Desea Cambiar la Descripción del Producto?\n 1. Si\n 2. No\n")
                        print("-" * 50)

                        if confirm == "1":
                            new = input("Ingrese la Nueva Descripción del Producto: ")
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
                titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción", "Cantidad"]
                print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*titles))
                print("-" * 100)
                print("{:<15} {:<30} {:<10} {:<25} {:<10}".format(*x))
                print("-" * 100)
                return
            else:
                print("Producto no Encontrado, Asegurese de que el Producto Exista")
                print("-" * 50)

    def agregar_producto_carrito(self):
        print("-" * 50)
        id = int(input("Ingrese Número del Producto que Desea agregar al carrito: "))
        print("-" * 50)

        found = False

        for x in self.principal:
            if x[0] == id:
                found = True
                position = self.principal.index(x)
                print("Los datos son:")
                print("-" * 80)
                titles = ["No.", "Nombre del Producto", "Precio Q.", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<15}".format(*titles))
                print("-" * 80)
                print("{:<15} {:<30} {:<10} {:<15}".format(*x))
                print("-" * 80)

                price = x[2]
                amount = int(input("Ingrese la Cantidad que Desea del Producto: "))
                if amount <= int(x[4]):
                    self.principal[position][4] = str(int(x[4]) - amount)
                    total_price = price * amount
                    self.car.append((x[0], x[1], price, amount, total_price, x[3]))
                    self.administrator.append((x[0], x[1], price, amount, total_price, x[3]))
                    print("Producto agregado al carrito correctamente")
                else:
                    print("No hay suficiente cantidad disponible del producto")
                break

        if not found:
            print("Producto no Encontrado, Asegúrese de que el Producto Exista")

    def Ver_carro(self):
        if self.car:
            print("-" * 115)
            titles = ["No.", "Nombre del Producto", "Precio Q.", "Cantidad adquirida", "Total", "Descripción"]
            print("{:<15} {:<30} {:<10} {:<20} {:<10} {:<15}".format(*titles))
            print("-" * 115)
            for product in self.car:
                product_no, product_name, price, quantity_adquired, total_price, description = product
                print(f"{product_no:<15} {product_name:<30} {price:<10} {quantity_adquired:<20} {total_price:<10} {description:<15}")
                print("-" * 115)

    def ver_ventas_del_dia(self):
        if self.administrator:
            print("-" * 115)
            titles = ["No.", "Nombre del Producto", "Precio Q.", "Cantidad adquirida", "Total", "Descripción"]
            print("{:<15} {:<30} {:<10} {:<20} {:<10} {:<15}".format(*titles))
            print("-" * 115)
            for product in self.administrator:
                product_no, product_name, price, quantity_adquired, total_price, description = product
                print(f"{product_no:<15} {product_name:<30} {price:<10} {quantity_adquired:<20} {total_price:<10} {description:<15}")
                print("-" * 115)
        else:
            print("No se Han Hecho Ventas Durante el Día")

    def Eliminar_Producto_del_carrito(self):
        if self.car:
            print("-" * 50)
            id = int(input("Ingrese Número del Producto que Desea Eliminar: "))
            print("-" * 115)
            for x in self.car:
                if x[0] == id:
                    self.car.remove(x)
                    print("El Producto se Elimino del Inventario con los  Siguientes Datos:")
                    print("-" * 115)
                    titles = ["No.", "Nombre del Producto", "Precio Q.", "Cantidad adquirida", "Total", "Descripción"]
                    print("{:<15} {:<30} {:<10} {:<20} {:<10} {:<15}".format(*titles))
                    print("-" * 115)
                    print("{:<15} {:<30} {:<10} {:<20} {:<10} {:<15}".format(*x))
                    print("-" * 115)
                    return
                else:
                    print("Producto No Encontrado, Asegurese de que el Producto Exista")
                    print("-" * 50)

        else:
            print("Asegurese de que Haya Producto en el Carro")

    def sumar_producto_al_carrito(self):
        if self.car:
            print("-" * 80)
            id = int(input("Ingrese el Número del Producto, al que le Desea Cambiar la Cantidad: "))
            print("-" * 80)
            for i, product in enumerate(self.car):
                if product[0] == id:
                    new = int(input("Ingrese la Nueva Cantidad: "))
                    product_no, product_name, price, old_total, old_quantity, description = product
                    new_total = price * new
                    self.car[i] = (product_no, product_name, price, new, new_total, description)
                    print(f"Cantidad del producto: {product_name}, actualizada a: {new}")
                    return
            print("Producto no Encontrado en el Carrito")

    def Impuesto(self):
        if self.car:
            iva_rate = 0.12
            self.taxes = self.subtotal * iva_rate
            print("IMPUESTO (12%): Q.", self.taxes)
            print("-" * 115)
        else:
            print("Asegurese de que Haya Producto en el Carro")

    def Iord(self):
        if self.car:
            print("-" * 115)
            print("---PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--")
            print("-" * 115)
            print("--------------------------------------------------------FACTURA----------------------------------------------------")
            print("-" * 115)
            print("No. de Orden", self.ticket)

            subtotal = 0
            taxes = 0
            total = 0

            car_copy = self.car.copy()

            factura = {"No. de Orden": self.ticket,
                "Productos": car_copy,
                "Subtotal": subtotal,
                "Impuesto (12%)": taxes,
                "Total": total}

            for product in car_copy:
                subtotal += product[4]
            taxes = subtotal * 0.12
            total = subtotal + taxes

            factura["Subtotal"] = subtotal
            factura["Impuesto (12%)"] = taxes
            factura["Total"] = total

            self.facturas.append(factura)

    def Ver_facturas(self):
        if self.facturas:
            print("")
            print("")
            print("-------------------------------------------------REALIZAR PEDIDOS--------------------------------------------------")
            print("")
            print("")
            print("")
            for i, factura in enumerate(self.facturas):
                print("-" * 115)
                print("---PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--")
                print("-" * 115)
                print("--------------------------------------------------------FACTURA----------------------------------------------------")
                print("-" * 115)
                print("No. de Orden", factura["No. de Orden"])
                print("-" * 115)
                titles = ["No.", "Nombre del Producto", "Precio Q.", "Cantidad adquirida", "Total", "Descripción"]
                print("{:<15} {:<30} {:<10} {:<20} {:<10} {:<15}".format(*titles))
                print("-" * 115)
                for product in factura["Productos"]:
                    product_no, product_name, price, quantity_adquired, total_price, description = product
                    print(
                        f"{product_no:<15} {product_name:<30} {price:<10} {quantity_adquired:<20} {total_price:<10} {description:<15}")
                    print("-" * 115)
                print(f"SUBTOTAL: Q. {factura['Subtotal']}")
                print("-" * 115)
                print(f"IMPUESTO (12%): Q. {factura['Impuesto (12%)']}")
                print("-" * 115)
                print(f"TOTAL Q. {factura['Total']}")
                print("-" * 115)
                print("")
                print("")
                print("")

        else:
            print("No hay Facturas disponibles")

    def Sub_total_carrito(self):
        if self.car:
            self.subtotal = sum(product[4] for product in self.car)
            print("SUBTOTAL: Q.", self.subtotal)
            print("-" * 115)

    def total_ventas_dia(self):
        if self.administrator:
            self.ganancias = sum(product[4] for product in self.administrator)
            iva_rate = 0.13
            self.iva = self.ganancias * iva_rate
            print("SUBTOTAL: Q.", self.ganancias)
            print("-" * 115)
            print("IMPUESTO (12%): Q.", self.iva)
            self.dinero = self.ganancias + self.iva
            print("-" * 115)
            print("TOTAL Q.", self.dinero)
            print("-" * 115)


    def calcular_total(self):
        if self.car:
            self.total = self.subtotal + self.taxes
            print("TOTAL Q.", self.total)
            print("-" * 115)
            print("---PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--PEDIDO--")
            print("-" * 115)

    def Pago(self):
        while True:
            print("\n------------------Metodo de Pago------------------")
            print("\n¿Como Desea Pagar?")
            print("\n1-. Efectivo")
            print("2-. Tarjeta\n")
            print("-" * 50)
            opcion_pago = input("Ingrese el Número de la Opción que Desee: ")
            print("-" * 50)

            if opcion_pago == "1":
                efectivo = float(input("\nIngrese la Cantidad con la que Pagara (Q.): "))
                if efectivo >= self.total:
                    cambio = efectivo - self.total
                    print("\n-------------------Pago Exitoso-------------------")
                    print(f"Su cambio es Q. {cambio:.2f}")
                    break
                else:
                    print("\n----------------------ERROR!----------------------")
                    print("------La Cantidad Ingresada es Insuficiente-------")

            elif opcion_pago == "2":
                print("--------- Acerque la Tarjeta al Lector... --------")
                time_eight = 5
                for tiempo_restante in range(time_eight, -1, -1):
                    print("\rTiempo Restante: {} segundos".format(tiempo_restante), end='')
                    time.sleep(1)
                print("\n-----------------Tarjeta Aprobada-----------------")
                print("---------------Gracias por su Compra--------------")
                break

            else:
                print("\n----------------------ERROR!----------------------")
                print("-----------------Intente Nuevamente---------------\n")

    def atender_clientes(self):
        while not self.line.empty():
            cliente = self.line.get()
            print(f"Atendiendo al Cliente No. {cliente}")


            time_twenty = 20
            for tiempo_restante in range(time_twenty, -1, -1):
                print("\rTiempo Restante: {} segundos".format(tiempo_restante), end='')
                time.sleep(1)

            print("\nEntregando Pedido al Cliente No. {}".format(cliente))

            time_eight = 8
            for tiempo_restante in range(time_eight, -1, -1):
                print("\rTiempo Restante: {} segundos".format(tiempo_restante), end='')
                time.sleep(1)

            print("\nPedido Entregado Exitosamente")
            self.car.clear()

    def take_ticket(self):
        if self.car:
            self.line.put(self.ticket)
            print("")
            print("")
            print("")
            print("-" * 50)
            print(f"Tu número de ticket es: {self.ticket}")

    def suma_ticket(self):
        self.ticket += 1

#Llamar a las Clases
Administration = Inventory_and_Orders()

#FUNCIONES
#VALIDACIONES
def Validar_Nombres(nombres):
    if not nombres.isalpha():
        raise ValueError ("\n----------------------ERROR!----------------------"
                          "\nLos Nombres NO Deben Contener Caracteres Especiales")

def Validar_Apellidos(apellidos):
    if not apellidos.isalpha():
        raise ValueError ("\n----------------------ERROR!----------------------"
                          "\nLos Appellidos NO Deben Contener Caracteres Especiales")

def Validar_Fecha_Nacimiento(fecha):
    partes = fecha.split('/')
    if len(partes) != 3 or not all(part.isdigit() for part in partes):
        raise ValueError ("\n----------------------ERROR!----------------------"
                          "\n--Formato Incorrecto Para la Fecha de Nacimiento--")

def Validar_Correo_Electronico(correo):
    if correo.count('@') != 1:
        raise ValueError ("\n----------------------ERROR!----------------------"
                          "\n-----Direccion de Correo Electronica NO Valida----")


def Validar_Numero_Telefonico(telefono):
    if not telefono.isdigit() or len(telefono) != 8:
        raise ValueError ("\n----------------------ERROR!----------------------"
                          "\n---Formato Incorrecto para el Número Telefonico---")

#Funion Para el Registro de Clientes
def Registro_Clientes():
    while True:
        print("\n--------------BIENVENIDOS A FASTFOOD--------------")
        print("\nIngrese sus Datos a Continuacion:")
        try:
            names = input("Ingrese sus Nombres: ")
            Validar_Nombres(names)

            last_name = input("Ingrese sus Apellidos: ")
            Validar_Apellidos(last_name)

            birth_date = input("Ingrese su Fecha de Nacimiento (DD/MM/AA): ")
            Validar_Fecha_Nacimiento(birth_date)

            email = input("Ingrese su Correo Electronico: ")
            Validar_Correo_Electronico(email)

            phone = input("Ingrese su Número Telefonico: ")
            Validar_Numero_Telefonico(phone)

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
        except ValueError as ve:
            print(f"Error: {ve}")

#Funcion Para el Inicio de Sesion de Clientes
def Iniciar_Sesion_Cliente():
    username = input("Ingrese su Nombre de Usuario: ")
    password = input("Ingrese su Contraseña: ")
    print("-" * 50)

    if username in users_clients:
        usuario = users_clients[username]
        if usuario["contraseña"] == password:
            print("\nIniciando Sesión como Cliente:", usuario["nombres"], usuario["apellidos"])
            Menu_Clientes()
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
                        time_eight = 5
                        for tiempo_restante in range(time_eight, -1, -1):
                            print("\rTiempo Restante: {} segundos".format(tiempo_restante), end='')
                            time.sleep(1)
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
                        time_eight = 5
                        for tiempo_restante in range(time_eight, -1, -1):
                            print("\rTiempo Restante: {} segundos".format(tiempo_restante), end='')
                            time.sleep(1)
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

#Funcion Para El Menu de Clientes
def Menu_Clientes():
    while True:
        print("--------------------------------------------------")
        print("--------------BIENVENIDOS A FASTFOOD--------------")
        print("--------------------------------------------------")
        print("\n1-. Ver Menu")
        print("2-. Agregar Producto al Carrito")
        print("3-. Ver Carrito")
        print("4-. Editar Carrito")
        print("5.- Finalizar Comprar")
        print("6.- Regresar al Menu Principal")
        print("7.- Salir del Programa\n")
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
            elif option2 == "6":
                Administration.Ver_Inventario_Clientes(category="Combos")
            else:
                print("\n------------------Opcion Invalida-----------------")
                print("-----------------Intente Nuevamente---------------\n")

        elif option == "2":
            Administration.agregar_producto_carrito()

        elif option == "3":
            Administration.Ver_carro()

        elif option == "4":
                print("--------------------------------------------------")
                print("\n--------------BIENVENIDOS A FASTFOOD--------------")
                print("--------------------------------------------------")
                print("\n1-. Eliminar Producto")
                print("2-. Cambiar Cantidad del Producto\n")
                print("-" * 50)
                option3 = input("Ingrese el Número de la Opción que Desee: ")
                print("-" * 50)

                if option3 == "1":
                    Administration.Eliminar_Producto_del_carrito()

                elif option3 == "2":
                    Administration.sumar_producto_al_carrito()

                else:
                    print("\n------------------Opcion Invalida-----------------")
                    print("-----------------Intente Nuevamente---------------\n")

        elif option == "5":
            Administration.suma_ticket()
            Administration.Iord()
            Administration.Ver_carro()
            Administration.Sub_total_carrito()
            Administration.Impuesto()
            Administration.calcular_total()
            Administration.Pago()
            Administration.take_ticket()
            print("-" * 50)
            Administration.atender_clientes()
            print("\n--------------Gracias Por Tu Compra---------------")
            print("-----------Esperamos que Vuelvas Pronto!----------\n")
            break

        elif option == "6":
            print("\n------------------ Regresando... -----------------")
            break

        elif option == "7":
            print("\n-----------Esperamos que Vuelvas Pronto!----------")
            exit()

        else:
            print("\n------------------Opcion Invalida-----------------")
            print("-----------------Intente Nuevamente---------------\n")

#Contraseña Administrativa PREDETERMINADA
predetermined = "FASTFOOD023"

while True:
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
                print("--------------------BIENVENID@--------------------")
                print("--------------------------------------------------")
                print("\nIngresando Como:", full_name)
                print("\n1-. Ingresar Producto al Inventario")
                print("2-. Ver el Inventario")
                print("3-. Cambiar algún Dato de un Producto")
                print("4-. Eliminar Producto del Inventario")
                print("5-. Realizar Pedidos")
                print("6-. Administracion de Clientes")
                print("7-. Ventas del Día")
                print("8-. Regresar al Menú Principal")
                print("9-. Salir del Programa\n")
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
                    Administration.Ver_facturas()

                elif option == "6":
                    Administracion_Clientes()

                elif option == "7":
                    Administration.ver_ventas_del_dia()
                    Administration.total_ventas_dia()

                elif option == "8":
                    print("\n------------------ Regresando... -----------------")
                    break

                elif option == "9":
                    print("\n-----------Esperamos que Vuelvas Pronto!----------")
                    exit()

                else:
                    print("\n------------------Opcion Invalida-----------------")
                    print("-----------------Intente Nuevamente---------------\n")

        else:
            print("\n----------------------ERROR!----------------------")
            print("---------------Contraseña Incorrecta--------------")

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

            elif option == "2":
                Iniciar_Sesion_Cliente()

            elif option == "3":
                Menu_Clientes()

            elif option == "4":
                print("\n------------------ Regresando... -----------------")
                break

            elif option == "5":
                print("\n-----------Esperamos que Vuelvas Pronto!----------")
                exit()

            else:
                print("\n------------------Opcion Invalida-----------------")
                print("-----------------Intente Nuevamente---------------\n")

    elif position == "2":
        print("\n-----------Esperamos que Vuelvas Pronto!----------")
        exit()

    else:
        print("\n------------------Opcion Invalida-----------------")
        print("-----------------Intente Nuevamente---------------\n")