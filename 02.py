class Bateria:
    def __init__(self):
        self.porcentaje = 100

    def descargar(self):
        self.porcentaje -= 10
        if self.porcentaje < 0:
            self.porcentaje = 0
        print(f"Batería al {self.porcentaje}%")

class Celular:
    def __init__(self, marca):
        self.marca = marca
        self.energia = Bateria()  

    def usar_app(self):
        print(f"{self.marca}: Abriendo aplicación...")
        self.energia.descargar()

mi_celular = Celular("Iphone")

mi_celular.usar_app()
mi_celular.usar_app()
