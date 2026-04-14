class AgenteSeguridad:
    def  int  (self):

        self.nombre = ""
        self.nivel_acceso = 0
    
    def evaluar_entrada(self):
        try:
            nivel_puerta = int(input("Ingrese el nivel de Seguridad de la puerta (1-5): "))

            if self.nivel_acceso >= nivel_puerta:
                print(f"Acceso consedido para {self.nombre}")
            else:
                print("Acceso denegado")
        except ValueError:
            print("Error: Por favor ingrese un numero entero valido")

guardia_turno = AgenteSeguridad()

guardia_turno.nombre = "Carlos Perez"
guardia_turno.nivel_acceso = 1
guardia_turno.evaluar_entrada()