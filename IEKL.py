class Termostato:
    def __init__(self, temperatura_inicial):

        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self):
        """Permite leer la temperatura como si fuera un atributo público."""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nuevo_valor):
        """Valida el valor antes de asignarlo."""
        if nuevo_valor < -273.15:
            print(f"Error: {nuevo_valor}°C es físicamente imposible.")
        else:
            self.__temperatura = nuevo_valor
            print(f"Temperatura actualizada a: {self.__temperatura}°C")

t = Termostato(20)

print(f"Temperatura actual: {t.temperatura}°C")

t.temperatura = -500

t.temperatura = 25
