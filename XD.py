#Ejercicio 1
# Pedir un número al usuario
numero = int(input("Ingresa un número: "))

# Mostrar la tabla de multiplicar
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

    
#Ejercicio 2
    meta = 100000
ahorro = 0

while ahorro < meta:
    deposito = float(input("¿Cuánto dinero depositamos hoy? "))
    ahorro = ahorro + deposito
    print("Ahorro actual:", ahorro)

print("¡Felicidades! Alcanzaste la meta de ahorro.")