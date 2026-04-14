import random

class Pokemon:
    """Clase padre que define los atributos base y el encapsulamiento."""
    def __init__(self, nombre, nivel, hp, ep):
        self.nombre = nombre
        self.nivel = nivel
        # 6. Encapsulamiento: Uso de propiedades privadas (__hp, __ep)
        self.__hp = hp
        self.__ep = ep

    # 6. Decoradores @property y @setter para proteger HP
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, valor):
        # 7. Lógica de Estado: El HP jamás permite valores matemáticos negativos
        if valor < 0:
            self.__hp = 0
        else:
            self.__hp = valor

    @property
    def ep(self):
        return self.__ep

    @ep.setter
    def ep(self, valor):
        # 7. Lógica de Estado: El EP (energía) no puede ser negativo
        if valor < 0:
            self.__ep = 0
        else:
            self.__ep = valor

    def atacar(self, rival):
        """Método base para ser sobrescrito por las clases hijas."""
        pass

# 4. Herencia Implementada (Crítico): 4 clases hijas construidas
class Fuego(Pokemon):
    def atacar(self, rival):
        # 7. Valida tener suficientes EP antes de proceder
        if self.ep >= 10:
            self.ep -= 10
            # 5. Polimorfismo: Cálculo de daño por ventaja elemental (Fuego > Planta)
            daño = 25 if isinstance(rival, Planta) else 10
            rival.hp -= daño
            return f"{self.nombre} usó Lanzallamas. Daño: {daño}."
        return f"{self.nombre} no tiene energía suficiente."

class Agua(Pokemon):
    def atacar(self, rival):
        if self.ep >= 10:
            self.ep -= 10
            # 5. Polimorfismo: Agua > Fuego
            daño = 25 if isinstance(rival, Fuego) else 10
            rival.hp -= daño
            return f"{self.nombre} usó Hidrobomba. Daño: {daño}."
        return f"{self.nombre} no tiene energía suficiente."

class Planta(Pokemon):
    def atacar(self, rival):
        if self.ep >= 10:
            self.ep -= 10
            # 5. Polimorfismo: Planta > Agua
            daño = 25 if isinstance(rival, Agua) else 10
            rival.hp -= daño
            return f"{self.nombre} usó Hoja Afilada. Daño: {daño}."
        return f"{self.nombre} no tiene energía suficiente."

class Electrico(Pokemon):
    def atacar(self, rival):
        if self.ep >= 10:
            self.ep -= 10
            # 5. Polimorfismo: Eléctrico es neutral en este ejemplo
            daño = 15
            rival.hp -= daño
            return f"{self.nombre} usó Impactrueno. Daño: {daño}."
        return f"{self.nombre} no tiene energía suficiente."
    

#===========
import random
from  pokemon_clases import Fuego, Agua, Planta, Electrico

# Simulación de catálogo de datos (pokedex.py ficticio)
pokedex = [
    {"nombre": "Charizard", "tipo": "Fuego", "nivel": 50, "hp": 100, "ep": 40},
    {"nombre": "Blastoise", "tipo": "Agua", "nivel": 50, "hp": 110, "ep": 35},
    {"nombre": "Venusaur", "tipo": "Planta", "nivel": 52, "hp": 105, "ep": 45},
    {"nombre": "Pikachu", "tipo": "Electrico", "nivel": 48, "hp": 80, "ep": 50}
]

def simulador_pve():
    print("--- BIENVENIDO AL SIMULADOR POKEMON ---")
    
    try:
        # Mostrar catálogo
        for i, p in enumerate(pokedex):
            print(f"{i}. {p['nombre']} ({p['tipo']})")
        
        # 3. Manejo de Errores (Try/Except): Atrapa letras o símbolos
        opcion = int(input("\nSelecciona tu Pokemon por número: "))
        datos = pokedex[opcion]

        # 2. Instanciación Dinámica: Usa condicionales para llamar a la clase hija
        if datos["tipo"] == "Fuego":
            jugador = Fuego(datos["nombre"], datos["nivel"], datos["hp"], datos["ep"])
        elif datos["tipo"] == "Agua":
            jugador = Agua(datos["nombre"], datos["nivel"], datos["hp"], datos["ep"])
        elif datos["tipo"] == "Planta":
            jugador = Planta(datos["nombre"], datos["nivel"], datos["hp"], datos["ep"])
        else:
            jugador = Electrico(datos["nombre"], datos["nivel"], datos["hp"], datos["ep"])

        # 8. Modo Simulación PvE: Uso de librería random para el rival
        rival_datos = random.choice(pokedex)
        rival = Planta(rival_datos["nombre"], rival_datos["nivel"], rival_datos["hp"], rival_datos["ep"])

        print(f"\n¡Combate! {jugador.nombre} vs {rival.nombre} (Computadora)")
        
        # Ejecutar ataque y mostrar resultado
        print(jugador.atacar(rival))
        print(f"Estado Final: {rival.nombre} tiene {rival.hp} HP restantes.")

    except (ValueError, IndexError):
        # 3. Respuesta ante entradas numéricas inválidas o letras
        print("\n[ERROR]: Entrada inválida. Debes elegir un número de la lista.")
    except Exception as e:
        print(f"\n[ERROR CRÍTICO]: {e}")

if __name__ == "__main__":
    simulador_pve()