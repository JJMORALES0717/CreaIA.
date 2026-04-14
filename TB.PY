#QUIZ

# Pedir datos
nombre = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización del profesor? (si/no): ")
saldo = float(input("Saldo disponible: "))
costo = float(input("Costo de cada paquete de minutos: "))

# Verificar acceso

if edad >= 15 and autorizacion.lower() == "si":
    print("Acceso aprobado al laboratorio para", nombre)

    paquetes = 0

    # Compra de paquetes

    while saldo >= costo:
        respuesta = input("¿Desea comprar otro paquete? (si/no): ")

        if respuesta.lower() == "si":
            saldo = saldo - costo
            paquetes = paquetes + 1
            print("Compra realizada")
        else:
            break

    # Resultados finales
    
    print("\nNombre del estudiante:", nombre)
    print("Paquetes comprados:", paquetes)
    print("Saldo restante:", saldo)

else:
    print("No puede ingresar al laboratorio.")
