class BioSonda:
    # Constructor: recibe numero_serie y ubicacion. Energia al 100% y activa en False.
    def __init__(self, numero_serie, ubicacion):
        self.numero_serie = numero_serie
        self.ubicacion = ubicacion
        self.energia = 100
        self.esta_activa = False

    # Metodo para activar la sonda.
    def activar(self):
        self.esta_activa = True

    # Metodo para realizar lectura con validaciones de estado y energia.
    def realizar_lectura(self, temperatura):
        if self.esta_activa == False:
            return f"[ERROR]: La sonda {self.numero_serie} se encuentra apagada. Operación cancelada."
        
        if self.energia < 15:
            return "Batería baja."
        
        self.energia -= 10
        return f"[LECTURA EXITOSA]: Temperatura de {temperatura}°C registrada en {self.ubicacion}. Energía restante: {self.energia}%."

    # Metodo para restablecer la energia al 100%.
    def recargar(self):
        self.energia = 100

# --- Ejemplo de Entrada (Lo que debes programar para probar) ---

# Instanciación
mi_sonda = BioSonda("S-2026", "Laboratorio Central")

# Intento de lectura con sonda apagada
print(mi_sonda.realizar_lectura(36.5))

# Activación y lectura exitosa
mi_sonda.activar()
print(mi_sonda.realizar_lectura(37.2))