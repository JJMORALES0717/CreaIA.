class Termostato:
    def __init__(self, temperatura_inicial: float = 20.0):

        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self) -> float:
        """Getter: Retorna la temperatura actual."""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor: float):
        """Setter: Valida y ajusta la temperatura."""
        if valor < -273.15:
            print(f"[ERROR] {valor}°C está por debajo del cero absoluto.")
        elif valor > 50.0:
            print(f"[AVISO] {valor}°C es demasiado alto para este equipo.")
        else:
            self.__temperatura = valor
            print(f"[SISTEMA] Temperatura ajustada a {self.__temperatura}°C")

# --- Pruebas de funcionamiento ---
term = Termostato(22.5)

print(f"Estado actual: {term.temperatura}°C")

term.temperatura = -300

term.temperatura = 24.0