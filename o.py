# 1. FUNCION SIMPLE

def mensaje_bienvenida():
    print("Bienvenido al sistema de ventas")
    print("Esperamos que tenga una excelente compra")

# Llamar la funcion
mensaje_bienvenida()


print("---------------------")


# 2. FUNCION CON PARAMETROS

def saludar_cliente(nombre):
    print("Hola", nombre, ", bienvenido al gimnasio")

# Pedir nombre al usuario
cliente = input("Ingrese el nombre del cliente: ")

# Llamar la funcion
saludar_cliente(cliente)


print("---------------------")


# 3. FUNCION CON RETORNO

def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

# Pedir datos
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad comprada: "))

# Calcular total
resultado = calcular_total(precio, cantidad)

# Mostrar resultado
print("El total a pagar es:", resultado)

# 4. EJERCICIO INTEGRADOR

PRECIO_FICHA = 500

def calcular_fichas(dinero):
    fichas = dinero // PRECIO_FICHA
    vuelto = dinero % PRECIO_FICHA
    return fichas, vuelto


opcion = 0

while opcion != 2:
    print("\n--- MENU ---")
    print("1 - Comprar fichas")
    print("2 - Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del cliente: ")
        dinero = int(input("Ingrese cuánto dinero tiene: "))

        fichas, vuelto = calcular_fichas(dinero)

        if fichas == 0:
            print("No tiene dinero suficiente para comprar una ficha.")
        else:
            print("Cliente:", nombre)
            print("Cantidad de fichas que puede comprar:", fichas)
            print("Dinero de vuelto:", vuelto)

    elif opcion == 2:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida")
        