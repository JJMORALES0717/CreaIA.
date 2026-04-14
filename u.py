#Ejercicio 1
inventario = [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6]
]

total = 0

for estante in inventario:
    for producto in estante:
        if producto > 5 and producto % 2 == 0:
            total += producto

print("Total de frutas válidas:", total)


#Ejercicio 2

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]


for i in range(len(precios_pasillos)):
    
    for j in range(len(precios_pasillos[i])):
        precio_actual = precios_pasillos[i][j]
        
        if precio_actual < 50:
            precios_pasillos[i][j] = precio_actual * 1.10

for pasillo in precios_pasillos:
    print(pasillo)