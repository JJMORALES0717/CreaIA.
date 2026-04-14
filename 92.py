# =========================================
#        SISTEMA DE GESTIÓN VIP v1.0
# ========================================

class TarjetaVIP:
    """Clase para gestionar los beneficios de clientes VIP"""
    
    def mostrar_puntos(self):
        """Imprime el saldo actual de puntos del cliente"""
        print(f"--- [ CONSULTA DE SALDO ] ---")
        print(f"Sus puntos acumulados son: {self.puntos}")
        print("-" * 30)

    def sumar_puntos(self):
        """Suma 50 puntos fijos por cada compra realizada"""
        self.puntos += 50
        print("\n>>> PROCESANDO COMPRA...")
        print("Se han sumado 50 puntos por su compra.")
        print("¡Gracias por preferirnos!")

# ----------------------------------------
#          PROGRAMA PRINCIPAL
# -----------------------------------------

tarjeta_carlos = TarjetaVIP()

tarjeta_carlos.puntos = 100

# 1. Verificación inicial
tarjeta_carlos.mostrar_puntos()

# 2. Registro de nueva compra
tarjeta_carlos.sumar_puntos()

# 3. Verificación final del nuevo saldo
tarjeta_carlos.mostrar_puntos()

# =========================================
#           FIN DEL PROGRAMA
# =======================================

