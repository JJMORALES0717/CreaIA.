#Ejercicio 2
precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

for i in range(len(precios_pasillos)):
    for j in range(len(precios_pasillos[i])):
        
       
        if precios_pasillos[i][j] < 50:
            precios_pasillos[i][j] *= 1.10

for fila in precios_pasillos:
    print(fila)
