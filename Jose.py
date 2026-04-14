# TAREA No. 5
cantidad = int(input("Ingrese la cantidad de cajas de leche disponibles: "))

# Verificar las condiciones
if cantidad > 20:
    print("Inventario saludable")
elif cantidad >= 1 and cantidad <= 20:
    print("Alerta: Hacer pedido al proveedor")
elif cantidad == 0:
    print("Urgente: Producto agotado")