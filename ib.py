nombre = input("Nombre: ")
edad = int(input("Edad: "))
aut = input("¿Tiene autorización? (si/no): ")
saldo = float(input("Saldo: "))
costo = float(input("Costo del paquete: "))

if edad >= 15 and aut == "si":
    print("Acceso aprobado para", nombre)

    paquetes = 0
    comprar = "si"

    while saldo >= costo and comprar == "si":
        saldo = saldo - costo
        paquetes = paquetes + 1
        comprar = input("¿Comprar otro paquete? (si/no): ")

    print("Paquetes comprados:", paquetes)
    print("Saldo restante:", saldo)

else:
    print("No puede ingresar al laboratorio")