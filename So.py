# ==========================================
# Proyecto - Línea de Producción 
# ==========================================

productos = ["Fertilizante", "Insecticida", "Herbicida"]

lotes = [0, 0, 0]
unidades = [0, 0, 0]

total_lotes = 0
total_unidades = 0

# ==========================================
# Entrada de datos
# ==========================================
while True:
    dato = input("Ingrese lote: ")

    if dato == "FIN":
        break

    if len(dato) != 5 or not dato.isdigit() or int(dato[0]) not in [1, 2, 3]:
        print("dato invalido", dato)
        continue

    codigo = int(dato[0]) - 1
    cantidad = int(dato[1:4])

    lotes[codigo] += 1
    unidades[codigo] += cantidad

    total_lotes += 1
    total_unidades += cantidad


# ==========================================
# Mostrar tabla
# ==========================================
print("\n")
print(f"{'Producto':15} {'Lotes':15} {'Total unidades':15} {'Promedio':15} {'Categoria':15}")

for i in range(3):
    if lotes[i] > 0:
        promedio = unidades[i] / lotes[i]
    else:
        promedio = 0

    # Categoría (sin función)
    if promedio <= 99:
        cat = "Insuficiente"
    elif promedio <= 299:
        cat = "Regular"
    elif promedio <= 599:
        cat = "Idoneo"
    else:
        cat = "Sobreproduccion"

    print(f"{productos[i]:15} {lotes[i]:15} {unidades[i]:15} {promedio:15.2f} {cat:15}")


# ==========================================
# Resultados finales
# ==========================================

indice_unidades = unidades.index(max(unidades))

indice_lotes = lotes.index(max(lotes))

if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0


print("\n")
print("Producto mayor cantidades:", productos[indice_unidades])
print("Producto con mas lotes:", productos[indice_lotes])
print("Promedio de productos producidos:", round(promedio_general, 2))
