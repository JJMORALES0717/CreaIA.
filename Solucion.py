# Proyecto - Linea de produccion
# Nombre: Jose Julian Morales Arango

# ---------------- FUNCIONES ----------------

def categoria(prom):
    if prom <= 99:
        return "Insuficiente"
    elif prom <= 299:
        return "Regular"
    elif prom <= 599:
        return "Idoneo"
    else:
        return "Sobreproduccion"


def nombre_producto(codigo):
    if codigo == 1:
        return "Fertilizante"
    elif codigo == 2:
        return "Insecticida"
    else:
        return "Herbicida"


# ---------------- LISTAS ----------------

lotes = [0, 0, 0]
unidades = [0, 0, 0]


# ---------------- LECTURA DE DATOS ----------------

dato = input()

while dato != "FIN":

    if len(dato) != 5 or not dato.isdigit():
        print("dato invalido", dato)

    else:
        codigo = int(dato[0])
        cantidad = int(dato[1:5])   # corregido

        if codigo < 1 or codigo > 3:
            print("dato invalido", dato)
        else:
            indice = codigo - 1
            lotes[indice] += 1
            unidades[indice] += cantidad

    dato = input()


# ---------------- TABLA ----------------

print(f'{"Producto":15} {"Lotes":15} {"Total unidades":15} {"Prom. por lote":15} {"Categoria":15}')

total_lotes = 0
total_unidades = 0

for i in range(3):

    if lotes[i] > 0:
        promedio = unidades[i] / lotes[i]
    else:
        promedio = 0

    cat = categoria(promedio)

    print(f'{nombre_producto(i+1):15} {lotes[i]:15} {unidades[i]:15} {promedio:15.2f} {cat:15}')

    total_lotes += lotes[i]
    total_unidades += unidades[i]


# ---------------- RESULTADOS ----------------

mayor_unidades = max(unidades)
producto_mayor_unidades = nombre_producto(unidades.index(mayor_unidades) + 1)

mayor_lotes = max(lotes)
producto_mayor_lotes = nombre_producto(lotes.index(mayor_lotes) + 1)

if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0


print()
print("Producto mayor cantidades:", producto_mayor_unidades)
print("Producto con mas lotes:", producto_mayor_lotes)
print(f"Promedio de productos producidos: {promedio_general:.2f}")
