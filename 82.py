class CajaRegistradora:
    def __init__(self, dinero_inicial):
        self.dinero_actual = dinero_inicial

    def mostrar_dinero_actual(self):
        print(f"El dinero actual en la caja es: {self.dinero_actual}")

    def procesar_venta(self):
        self.dinero_actual += 500
        print("Venta de 500 procesada exitosamente.")

mi_caja = CajaRegistradora(1000)

mi_caja.mostrar_dinero_actual()

mi_caja.procesar_venta()

mi_caja.mostrar_dinero_actual()