# ==========================================
# Ejercicio 1
# Control de entrada a un torneo
# ==========================================

nombre = input("Nombre del participante: ")
edad = int(input("Edad: "))
inscripcion = input("Inscripción confirmada (si/no): ")

if edad >= 15 and inscripcion == "si":
    print("Participante autorizado para ingresar al torneo.")
else:
    print("Participante no autorizado.")


# ==========================================
# Ejercicio 2
# Batería de celular
# ==========================================

bateria = int(input("Ingrese el porcentaje de batería: "))

if bateria <= 20:
    print("Debe cargar el celular")
else:
    print("La batería es suficiente")


# ==========================================
# Ejercicio 3
# Clasificación de envío
# ==========================================

peso = float(input("Peso del paquete: "))

if peso < 1:
    print("Paquete liviano")
elif peso <= 5:
    print("Paquete estándar")
else:
    print("Paquete pesado")


# ==========================================
# Ejercicio 4
# Semáforo (corregido)
# ==========================================

color = input("Ingrese el color del semáforo: ")

if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Precaución")
else:
    print("Detenerse")


# ==========================================
# Ejercicio 5
# Acceso VIP a concierto
# ==========================================

nombre = input("Nombre del cliente: ")
edad = int(input("Edad: "))
entrada = input("Tipo de entrada (general/vip): ")
dinero = float(input("Dinero disponible: "))
precio_bebida = float(input("Precio de la bebida especial: "))

if edad >= 18 and entrada == "vip":
    print("Acceso VIP aprobado para", nombre)
    comprar = input("¿Desea comprar bebida especial? (si/no): ")

    if comprar == "si":
        if dinero >= precio_bebida:
            cambio = dinero - precio_bebida
            print("Compra de bebida aprobada")
            print("Cambio:", cambio)
        else:
            print("No tiene dinero suficiente para la bebida")
else:
    print("No puede ingresar al área VIP")


# ==========================================
# Ejercicio 6
# Sistema de becas
# ==========================================

nombre = input("Nombre del estudiante: ")
promedio = float(input("Promedio final: "))
ingreso = float(input("Ingreso familiar mensual: "))
materias = int(input("Cantidad de materias aprobadas: "))

if promedio < 70:
    beca = "Sin beca"
    monto = 0

elif promedio <= 84:
    if ingreso <= 400000:
        beca = "Beca parcial"
        monto = 50000
    else:
        beca = "Sin beca"
        monto = 0

else:
    if materias >= 5 and ingreso <= 400000:
        beca = "Beca completa"
        monto = 100000
    else:
        beca = "Beca parcial"
        monto = 50000

print("Estudiante:", nombre)
print("Resultado:", beca)
print("Monto asignado:", monto)


# ==========================================
# Ejercicio 7
# Tarifa de hotel
# ==========================================

nombre = input("Nombre del cliente: ")
temporada = input("Temporada (alta/media/baja): ")
noches = int(input("Cantidad de noches: "))
precio = float(input("Precio base por noche: "))
membresia = input("¿Tiene membresía? (si/no): ")

subtotal = noches * precio

if temporada == "alta":
    subtotal = subtotal * 1.20
elif temporada == "media":
    subtotal = subtotal * 1.10

if membresia == "si" and noches >= 3:
    descuento = subtotal * 0.15
elif membresia == "si" or noches == 2:
    descuento = subtotal * 0.05
else:
    descuento = 0

total = subtotal - descuento

print("Cliente:", nombre)
print("Subtotal con recargo:", subtotal)
print("Descuento aplicado:", descuento)
print("Total final:", total)


# ==========================================
# Ejercicio 8
# Menú de academia
# ==========================================

opcion = input("Opción: ")
usuario = input("Tipo de usuario (admin/profesor/estudiante): ")
promedio = float(input("Promedio: "))

match opcion:
    case "1" | "matricular":
        if usuario == "admin" or usuario == "profesor":
            print("Matriculación permitida")
        else:
            print("No tiene permisos")

    case "2" | "notas":
        if usuario == "profesor" or usuario == "estudiante":
            print("Acceso a notas permitido")
        else:
            print("No tiene permisos")

    case "3" | "certificado":
        if usuario == "estudiante" and promedio >= 70:
            print("Certificado generado correctamente")
        else:
            print("No se puede generar certificado")

    case "4" | "salir":
        print("Programa finalizado")

    case _:
        print("Opción inválida")


# ==========================================
# Ejercicio 9
# Tienda gamer
# ==========================================

nombre = input("Nombre del cliente: ")
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad deseada: "))
stock = int(input("Cantidad en stock: "))
membresia = input("¿Tiene membresía gamer? (si/no): ")

if cantidad > stock:
    print("No hay suficiente stock")
else:
    subtotal = precio * cantidad

    if subtotal > 50000 and membresia == "si":
        descuento = subtotal * 0.20
    elif subtotal > 30000 or membresia == "si":
        descuento = subtotal * 0.10
    else:
        descuento = 0

    total = subtotal - descuento

    print("Venta aprobada")
    print("Subtotal:", subtotal)
    print("Descuento:", descuento)
    print("Total final:", total)


# ==========================================
# Ejercicio 10
# Misiones de videojuego
# ==========================================

jugador = input("Nombre del jugador: ")
clase = input("Clase del jugador (guerrero/mago/arquero): ")
opcion = input("Opción de misión: ")
nivel = int(input("Nivel del jugador: "))
enemigos = int(input("Enemigos derrotados: "))

if opcion == "bosque":
    if nivel >= 1:
        recompensa = enemigos * 10
        print("Misión bosque completada")
        print("Recompensa total:", recompensa)

elif opcion == "castillo":
    if nivel >= 5:
        recompensa = enemigos * 20
        bono = 0

        if clase == "guerrero" or clase == "mago":
            bono = 50

        total = recompensa + bono

        print("Misión castillo completada")
        print("Recompensa base:", recompensa)
        print("Bono adicional:", bono)
        print("Recompensa total:", total)
    else:
        print("Nivel insuficiente para misión castillo")

elif opcion == "dragon":
    if nivel >= 10 and (clase == "guerrero" or clase == "arquero"):
        recompensa = enemigos * 50
        bono = 0

        if enemigos > 3:
            bono = 100

        total = recompensa + bono

        print("Misión dragón completada")
        print("Recompensa total:", total)
    else:
        print("No cumple requisitos para misión dragón")

elif opcion == "salir":
    print("Saliendo del juego")
    