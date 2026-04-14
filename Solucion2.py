# -------------------------------------------------
# Proyecto: Línea de Producción
# Curso: Fundamentos de Programación
# Nombre: Jose Julian Morales Arango
# -------------------------------------------------

# Funcion para clasificar el promedio
def categoria(prom):
    if prom <= 99:
        return "Insuficiente"
    elif prom <= 299:
        return "Regular"
    elif prom <= 599:
        return "Idoneo"
    else:
        return "Sobreproduccion"


# Lista con los nombres de los productos
productos = ["Fertilizante", "Insecticida", "Herbicida"]

# Listas para guardar datos
lotes = [0, 0, 0]
unidades = [0, 0, 0]

# -----------------------------
# Lectura de datos
# -----------------------------
dato = input("Ingrese dato: ")

while dato != "FIN":

    # Validar que tenga 5 digitos
    if len(dato) != 5 or not dato.isdigit():
        print("dato invalido", dato)

    else:
        codigo = int(dato[0])

        # Validar codigo de producto
        if codigo < 1 or codigo > 3:
            print("dato invalido", dato)

        else:
            cantidad = int(dato[1:4])
            i = codigo - 1

            # Guardar datos
            lotes[i] = lotes[i] + 1
            unidades[i] = unidades[i] + cantidad

    dato = input("Ingrese dato: ")

# -----------------------------
# Mostrar tabla
# -----------------------------
print()
print(f'{"Producto":15} {"Lotes":15} {"Total unidades":15} {"Prom. por lote":15} {"Categoria":15}')

total_lotes = 0
total_unidades = 0

for i in range(3):

    if lotes[i] != 0:
        prom = unidades[i] / lotes[i]
    else:
        prom = 0

    cat = categoria(prom)

    print(f'{productos[i]:15} {lotes[i]:15} {unidades[i]:15} {prom:15.2f} {cat:15}')

    total_lotes = total_lotes + lotes[i]
    total_unidades = total_unidades + unidades[i]

# -----------------------------
# Calculos finales
# -----------------------------
mayor_unidades = max(unidades)
pos = unidades.index(mayor_unidades)

mayor_lotes = max(lotes)
pos2 = lotes.index(mayor_lotes)

if total_lotes != 0:
    prom_general = total_unidades / total_lotes
else:
    prom_general = 0

# -----------------------------
# Resumen final
# -----------------------------
print()
print("Producto mayor cantidades:", productos[pos])
print("Producto con mas lotes:", productos[pos2])
print("Promedio de productos producidos:", round(prom_general, 2))

