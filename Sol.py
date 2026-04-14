# 1. Creamos la clase CajaRegistradora
class CajaRegistradora:

    # 2. Método para cobrar un producto
    def cobrar_producto(self):
       
        precio = float(input("Ingrese el precio del producto: "))
        
        self.dinero_acumulado += precio
        
        print(f"Cobro exitoso. Llevamos acumulado: {self.dinero_acumulado}")

    # 3. Método para imprimir el cierre de turno
    def imprimir_cierre_turno(self):
        print("-" * 30)
        print("REPORTE DE CIERRE")
        print(f"Cajero encargado: {self.cajero_asignado}")
        print(f"Total de dinero recaudado en el día: {self.dinero_acumulado}")
        print("-" * 30)


# 4. Programa principal (fuera de la clase)

caja_express = CajaRegistradora()

caja_express.cajero_asignado = "Diego" 
caja_express.dinero_acumulado = 0

caja_express.cobrar_producto()
caja_express.cobrar_producto()

caja_express.imprimir_cierre_turno()
