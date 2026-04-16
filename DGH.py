from abc import ABC, abstractmethod

class VehiculoTerrestre(ABC):
    
    @abstractmethod
    def conducir_ruedas(self):
        pass


class VehiculoAcuatico(ABC):
    
    @abstractmethod
    def encender_helices(self):
        pass
    
class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    
    def conducir_ruedas(self):
        print("Activando tracción 4x4 en terreno rocoso.")
    
    def encender_helices(self):
        print("Retrayendo ruedas y activando propulsión acuática.")


class AutoComun(VehiculoTerrestre):
    
    def conducir_ruedas(self):
        print("Conduciendo auto en carretera.")


class Lancha(VehiculoAcuatico):
    
    def encender_helices(self):
        print("Encendiendo hélices de la lancha.")



auto = AutoComun()
lancha = Lancha()
anfibio = VehiculoAnfibio()

ruta_terrestre = [auto, anfibio]

print("=== Ruta Terrestre ===")
for vehiculo in ruta_terrestre:
    vehiculo.conducir_ruedas()

ruta_acuatica = [lancha, anfibio]

print("\n=== Ruta Acuática ===")
for vehiculo in ruta_acuatica:
    vehiculo.encender_helices()