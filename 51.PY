# 1. Matriz inicial de inventario
inventario = [
    ["Croquetas", 15, 20, 0],
    ["Juguete", 10, 5, 0],
    ["Champú", 5, 10, 0]
]

def calcular_valor_estante(fila):
    return fila[1] * fila[2]

def actualizar_valores_totales():
    for producto in inventario:
        producto[3] = calcular_valor_estante(producto)

# Inicializamos los valores antes de empezar
actualizar_valores_totales()

while True:
    print("\n>>> SISTEMA DE GESTIÓN HUELLITAS FELICES <<<")
    print("\nProductos Disponibles:")
    for p in inventario:
        print(f"- {p[0]:<12} | Stock: {p[1]:<3} | Precio: ${p[2]:<4}")
    
    opcion = input("\n¿Qué desea hacer? (Vender / Agregar / Eliminar / Salir): ").capitalize()

    if opcion == "Vender":
        nombre = input("Escriba el nombre del producto: ").capitalize()
        encontrado = False
        
        for p in inventario:
            if p[0] == nombre:
                encontrado = True
                while True:
                    try:
                        cantidad = int(input(f"¿Cantidad a vender de {p[0]}?: "))
                        if cantidad <= p[1]:
                            p[1] -= cantidad
                            p[3] = calcular_valor_estante(p)
                            print(f"¡Venta exitosa! Quedan {p[1]} {p[0]} en el estante.")
                            break
                        else:
                            print(f"[ERROR: Solo tenemos {p[1]} en stock]")
                            break
                    except ValueError:
                        print("[ERROR: Ingrese un número válido]")
                break 
        if not encontrado:
            print("[ERROR: El producto no existe]")

    elif opcion == "Agregar":
        try:
            nombre = input("Ingrese el nombre del nuevo producto: ").capitalize()
            stock = int(input("Ingrese la cantidad inicial: "))
            precio = int(input("Ingrese el precio unitario: "))
            # Agregamos el nuevo producto calculando su valor total de una vez
            nuevo_producto = [nombre, stock, precio, stock * precio]
            inventario.append(nuevo_producto)
            print(f"¡Éxito! '{nombre}' ha sido incorporado al inventario.")
        except ValueError:
            print("[ERROR: El stock y el precio deben ser números]")

    elif opcion == "Eliminar":
        nombre = input("Escriba el nombre del producto a eliminar: ").capitalize()
        encontrado = False
        for i in range(len(inventario)):
            if inventario[i][0] == nombre:
                inventario.pop(i)
                print(f"¡Confirmado! El producto '{nombre}' ha sido removido.")
                encontrado = True
                break
        if not encontrado:
            print(f"[ERROR: El producto '{nombre}' no se encuentra]")

    elif opcion == "Salir":
        print("\n" + "="*45)
        print("     RESUMEN DE INVENTARIO 'HUELLITAS'")
        print("="*45)
        gran_total = 0
        for p in inventario:
            print(f"Producto: {p[0]:<12} | Valor Estante: ${p[3]}")
            gran_total += p[3]
        
        print("-" * 45)
        print(f"VALOR TOTAL DEL INVENTARIO : ${gran_total}")
        print("="*45)
        print("Saliendo del sistema... ¡Guau guau!")
        break

    else:
        print("Opción no válida, intente de nuevo.")