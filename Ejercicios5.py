import random as rd

def log(mensaje):
    print(f"[SISTEMA]: {mensaje}")

class SableDeLuz:
    def __init__(self, duelista):
        self.duelista = duelista

        self.energia = 100

    def recargar(self, cantidad=None):
        if cantidad is None:
            self.energia += 10
            log(f"{self.duelista} hizo una recarga estándar (+10).")
        else:
            self.energia += cantidad
            log(f"{self.duelista} hizo una recarga específica (+{cantidad}).")

        if self.energia > 100: self.energia = 100

    def __sub__(self, otro_sable):
        if isinstance(otro_sable, SableDeLuz):
            self.energia -= 10
            otro_sable.energia -= 10
            log(f"¡Choque de sables! {self.duelista} y {otro_sable.duelista} pierden 10 de energía.")
            
            if self.energia < 0: self.energia = 0
            if otro_sable.energia < 0: otro_sable.energia = 0
        return self

    def __str__(self):
        return f"Sable de {self.duelista} | Energía: {self.energia}%"


sable_anakin = SableDeLuz("Anakin")
sable_obiwan = SableDeLuz("Obi-Wan")

print("--- Inicio del Combate ---")
print(sable_anakin)
print(sable_obiwan)
print("-" * 30)

sable_anakin - sable_obiwan

sable_anakin.recargar()      
sable_obiwan.recargar(5)    
print("-" * 30)

log(f"Estado Final: {sable_anakin}")
log(f"Estado Final: {sable_obiwan}")

#=====================================================================
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