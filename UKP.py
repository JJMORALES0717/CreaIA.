class Empleado:
    def __init__(self):
        
        self.__salario = 300

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 300:
            self.__salario = nuevo_salario
            print(f"Salario actualizado a: {self.__salario}")
        else:
            print("Error: El nuevo salario debe ser mayor a 300.")

empleado1 = Empleado()

print(f"Salario inicial: {empleado1.salario}")

empleado1.salario = 250 

empleado1.salario = 500

print(f"Salario final: {empleado1.salario}")