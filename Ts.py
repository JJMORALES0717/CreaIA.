class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro):
        if isinstance(otro, Producto):
            return self.precio + otro.precio
        return self.precio + otro

    def __radd__(self, otro):
        return self.__add__(otro)

    def __sub__(self, otro):
        if isinstance(otro, Producto):
            return self.precio - otro.precio
        return self.precio - otro

    def __lt__(self, otro):
        return self.precio < otro.precio

    def __str__(self):
        return f"{self.nombre:<15} | Precio: Q{self.precio:>8.2f}"

p1 = Producto("Laptop HP", 6500.00)
p2 = Producto("Mouse Logi", 150.00)
p3 = Producto("Teclado Mec.", 450.00)
p4 = Producto("Monitor Dell", 1800.00)

inventario = [p1, p2, p3, p4]

inventario_ordenado = sorted(inventario)

total_inventario = sum(inventario)
diferencia = p1 - p2  

mas_caro = max(inventario)

print("="*42)
print("        RESUMEN DE INVENTARIO")
print("="*42)
print("PRODUCTOS CLASIFICADOS (MENOR A MAYOR):")
for prod in inventario_ordenado:
    print(f" • {prod}")

print("-"*42)
print(f"TOTAL EN INVENTARIO:        Q{total_inventario:>9.2f}")
print(f"PRODUCTO MÁS COSTOSO:       {mas_caro.nombre} (Q{mas_caro.precio})")
print(f"DIFERENCIA P1 - P2:         Q{diferencia:>9.2f}")
print("="*42)