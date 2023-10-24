class Inventory:
    def __init__(self):
        self.nom = []
        nmer.append(self.nom)

    def ingreso_de_datos(self):
        print("-" * 50)
        cuenta = int(input("¿Cuantos Productos Ingresara?: "))
        print("-" * 50)

        for i in range(cuenta):
            products = []
            print("Producto No.", i+1)
            name_product = input("Ingrese el Nombre del Producto: ")
            idProduct = i+1
            stock = input("Ingrese la cantidad exacta que tiene del producto: ")
            price = int(input("Ingrese el precio del producto: "))
            description = input("Ingrese la descripción del producto: ")
            print("-" * 50)
            nome.append(resultado)
            nome.append(name)
            nome.append(stock)
            nome.append(precio)
            nome.append(descripcion)
            self.nom.append(nome)
            print("Información del producto No.", i+1, "guardada correctamente")
            print("-" * 50)

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
            print("4-. Sumar Producto a lo que ya Teniamos")
            print("5-. Eliminar Producto del Inventario")
            print("0-. Regresar al Menú Principa")
            print("-" * 50)


