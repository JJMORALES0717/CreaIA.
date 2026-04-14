#Ejercicio 1
cliente = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Guatemala"
}

print("Datos iniciales:")
print(cliente["nombre"])
print(cliente["edad"])
print(cliente["ciudad"])


cliente["ciudad"] = "Antigua"


cliente["edad"] += 1

print("\nDatos modificados:")
print(cliente["nombre"])
print(cliente["edad"])
print(cliente["ciudad"])
