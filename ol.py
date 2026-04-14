# 1. Crear la clase Empleado usando pass
class Empleado:
    pass

# 2. Fabricar tres objetos físicos independientes
empleado_1 = Empleado()
empleado_2 = Empleado()
empleado_3 = Empleado()

# 3 y 4. Asignar atributos (nombre, cargo, salario) con los datos inventados
# Empleado 1: Gerente
empleado_1.nombre = "Carlos Ruiz"
empleado_1.cargo = "Gerente"
empleado_1.salario = 5000

# Empleado 2: Cajero
empleado_2.nombre = "Ana Martínez"
empleado_2.cargo = "Cajero"
empleado_2.salario = 2500

# Empleado 3: Bodeguero
empleado_3.nombre = "Luis Gómez"
empleado_3.cargo = "Bodeguero"
empleado_3.salario = 2200

# 5. Utilizar print() con f-strings para la presentación
print(f"Hola, mi nombre es {empleado_1.nombre}, trabajo como {empleado_1.cargo} y gano Q{empleado_1.salario}.")
print(f"Hola, mi nombre es {empleado_2.nombre}, trabajo como {empleado_2.cargo} y gano Q{empleado_2.salario}.")
print(f"Hola, mi nombre es {empleado_3.nombre}, trabajo como {empleado_3.cargo} y gano Q{empleado_3.salario}.")
