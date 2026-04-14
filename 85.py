class Cajero:
    def __init__(self, nombre, id_empleado):
        """
        Constructor de la clase. Recibe el nombre e ID 'de fuera'
        e inicializa el dinero en caja en 0.
        """
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.dinero_en_caja = 0

    def cobrar_articulo(self, precio):
        """
        Suma el precio de un artículo al total acumulado en la caja.
        """
        self.dinero_en_caja += precio
        print(f"[{self.nombre}] Cobró artículo de: ${precio}")

    def mostrar_dinero_en_caja(self):
        """
        Imprime el estado actual de la caja con la información del responsable.
        """
        print("\n--- REPORTE DE CAJA ---")
        print(f"Cajero: {self.nombre}")
        print(f"ID Empleado: {self.id_empleado}")
        print(f"Total acumulado: ${self.dinero_en_caja}")
        print("-" * 23)


# 1. Crear dos cajeros (inventando los datos)
cajero1 = Cajero("Carlos Ruiz", "ID-9921")
cajero2 = Cajero("Elena Torres", "ID-4405")

# 2. Cobrar 2 artículos en el cajero1
cajero1.cobrar_articulo(125.50)
cajero1.cobrar_articulo(50.00)

# 3. Cobrar 1 artículo en el cajero2
cajero2.cobrar_articulo(300.75)

# 4. Mostrar el dinero que tiene la caja del cajero1
cajero1.mostrar_dinero_en_caja()

# 5. Mostrar el dinero que tiene la caja del cajero2
cajero2.mostrar_dinero_en_caja()
