class CuentaBancaria:

    tasa_interes_global = 0.05
    total_cuentas = 0

    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
    
        CuentaBancaria.total_cuentas += 1

    # --- SEGURIDAD (Decoradores) ---

    @property
    def saldo(self):
        """Getter para el saldo (No tiene setter por seguridad)"""
        return self.__saldo

    @property
    def titular(self):
        """Getter para el titular"""
        return self.__titular

    @titular.setter
    def titular(self, nuevo_nombre):
        """Setter con validación para que el nombre no sea vacío"""
        if nuevo_nombre.strip():
            self.__titular = nuevo_nombre
        else:
            print("Error: El nombre del titular no puede estar en blanco.")

    # --- MÉTODOS DE INSTANCIA ---

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: +${cantidad}")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: -${cantidad}")
        else:
            print("Error: Fondos insuficientes o cantidad inválida.")

    def proyectar_interes(self):
        ganancia = self.__saldo * CuentaBancaria.tasa_interes_global
        print(f"Proyección: Con una tasa de {CuentaBancaria.tasa_interes_global * 100}%, ganarás ${ganancia} este año.")

    # --- MÉTODO DE CLASE ---

    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes_global = nueva_tasa
        print(f"--- Tasa de interés actualizada a nivel global: {nueva_tasa * 100}% ---")

cuenta1 = CuentaBancaria("Sofía", 0)
cuenta2 = CuentaBancaria("Carlos", 500)

print(f"Cuentas totales en el banco: {CuentaBancaria.total_cuentas}")

cuenta1.depositar(10000)

cuenta1.proyectar_interes()

CuentaBancaria.modificar_tasa_interes(0.10)

cuenta1.proyectar_interes()

print("\nIntentando cambiar nombre de Sofía a vacío...")
cuenta1.titular = ""
print(f"Titular actual: {cuenta1.titular}")
