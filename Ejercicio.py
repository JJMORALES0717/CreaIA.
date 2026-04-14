# DISCOTECA 
print("Bienvenido a la discoteca")
edad = int(input("Ingresa tu edad: "))
membresia = input("¿Tienes membresía premium? (si/no): ").lower()

tiene_membresia = membresia == "si"

print("AND (mayor de 18 y membresía):", edad >= 18 and tiene_membresia)
print("OR (mayor de 18 o membresía):", edad >= 18 or tiene_membresia)
print("NOT (no tiene membresía):", not tiene_membresia)

if edad >= 18 and tiene_membresia:
    print("Puede entrar a la sala exclusiva")
else:
    print("No puede entrar a la sala exclusiva")