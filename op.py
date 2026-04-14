# Función que verifica si es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# Programa principal
edad = int(input("Ingrese su edad: "))

resultado = es_mayor_de_edad(edad)

if resultado:
    print("Puedes comprar alcohol")
else:
    print("Venta denegada")