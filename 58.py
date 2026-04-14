class CajaRegistradora:
    # 1. Definimos la clase y el dinero inicial (constructor)
    def __init__(self, saldo_inicial):
        self.dinero_actual = saldo_inicial

    def mostrar_dinero_actual(self):
        print(f"💰 Saldo en caja: ${self.dinero_actual}")

    def procesar_venta(self):
        self.dinero_actual += 500
        print("✅ Venta procesada: +$500")

# ---------------------------------------------------------
# Fabricamos el objeto (Instanciación)
# ---------------------------------------------------------

mi_caja = CajaRegistradora(1000)

# ---------------------------------------------------------
# Ponemos a trabajar nuestra caja registradora
# ---------------------------------------------------------

mi_caja.mostrar_dinero_actual()

mi_caja.procesar_venta()

mi_caja.mostrar_dinero_actual()
