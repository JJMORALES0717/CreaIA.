class Arma:
    def __init__(self, nombre: str, daño: int):
        self.nombre = nombre
        self.daño = daño

    def __str__(self):
        return f"{self.nombre} (Daño: {self.daño})"

class Guerrero:
    def __init__(self, nombre: str, arma: Arma):
        self.nombre = nombre.upper()
        self.arma = arma

    def presentar(self):
        print("-" * 30)
        print(f"GUERRERO: {self.nombre}")
        print(f"Equipamiento: {self.arma}")
        print("-" * 30)

    def atacar(self):
        print(f"{self.nombre} lanza un ataque feroz!")
        print(f"¡Causa {self.arma.daño} de daño usando su {self.arma.nombre}!")
        print("=" * 30 + "\n")

if __name__ == "__main__":

    espada_real = Arma("Espada de Fragmentos Estelares", 75)

    guerrero = Guerrero("Aragorn", espada_real)

    guerrero.presentar()
    guerrero.atacar()