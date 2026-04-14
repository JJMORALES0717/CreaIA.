print("Tienda La Santa")

# Mostrar productos
print("Productos disponibles:")
print("1. Leche - $20")
print("2. Azúcar - $5")
print("3. Huevos  - $2")

# Elegir producto
producto = input("¿Qué producto quiere comprar? ")

# Cantidad
cantidad = int(input("¿Cuántos quiere? "))
print("5 cartones de leche")
print("10 libras de azúcar")
print("200 de huevos")

# Precios
if producto == "leche":
    precio = 20
elif producto == "azúcar":
    precio = 5
elif producto == "huevos":
    precio = 2
else:
    print("Producto no disponible")
    precio = 0

# Total
total = precio * cantidad

# Factura
print("\nFactura")
print("======Tienda La Santa======")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Total a pagar: $", total)