# Ejercicio Integrador - Sala de videojuegos
# Nombre: Jose Julian Morales Arango

# Funcion para calcular fichas
def calcular_fichas(dinero):
    precio_ficha = 500
    fichas = dinero // precio_ficha
    vuelto = dinero % precio_ficha
    return fichas, vuelto


opcion = 0

while opcion != 2:
    print("\n--- SALA DE VIDEOJUEGOS ---")
    print("1 - Comprar fichas")
    print("2 - Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del cliente: ")
        dinero = int(input("Ingrese cuanto dinero tiene: "))

        fichas, vuelto = calcular_fichas(dinero)

        if fichas < 1:
            print("No tiene dinero suficiente para comprar una ficha.")
        else:
            print("Cliente:", nombre)
            print("Cantidad de fichas que puede comprar:", fichas)
            print("Dinero de vuelto:", vuelto)

    elif opcion == 2:
        print("Gracias por usar el sistema.")

    else:
        print("Opcion no valida.")