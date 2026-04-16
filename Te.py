from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(Trabajador):
    def realizar_tarea(self):
        print("Diseñando planos")

class Medico(Trabajador):
    def realizar_tarea(self):
        
        pass

print("--- Intentando instanciar al Ingeniero ---")
ing = Ingeniero()
ing.realizar_tarea()

print("\n--- Intentando instanciar al Medico ---")
try:
    med = Medico()
    print("¡Médico creado con éxito!")
    med.realizar_tarea()
except TypeError as e:
    print(f"Error al crear al médico: {e}")