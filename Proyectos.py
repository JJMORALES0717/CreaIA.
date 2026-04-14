# ====================================================================
# PROYECTO 3: SISTEMA POKÉMON (VERSIÓN OPTIMIZADA)
# ====================================================================
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible

class Pokemon:
    def __init__(self, nombre, tipo, hp_max, ep_max):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = self.hp_max = hp_max
        self.ep = self.ep_max = ep_max

    def mostrar_hud(self):
        """Muestra una interfaz visual compacta."""
        barra = "■" * (self.ep // 5) + "□" * ((self.ep_max - self.ep) // 5)
        print(f"\n{'━'*30}")
        print(f" POKÉMON: {self.nombre.upper()} | {self.tipo}")
        print(f" SALUD:   {self.hp} HP")
        print(f" ENERGÍA: [{barra}] {self.ep} EP")
        print(f"{'━'*30}")

    def descansar(self):
        self.ep = self.ep_max
        print(f"✨ {self.nombre} ha descansado. ¡Energía al 100%!")

# Clases por tipo con ataques específicos (Herencia y Polimorfismo)
class PokemonFuego(Pokemon):
    def atacar(self):
        if self.ep >= 20: self.ep -= 20; print("🔥 ¡LLAMARADA!")
        else: print("⚠️ Sin energía suficiente...")

class PokemonAgua(Pokemon):
    def atacar(self):
        if self.ep >= 25: self.ep -= 25; print("💧 ¡HIDROBOMBA!")
        else: print("⚠️ Sin energía suficiente...")

class PokemonPlanta(Pokemon):
    def atacar(self):
        if self.ep >= 15: self.ep -= 15; print("🍃 ¡RAYO SOLAR!")
        else: print("⚠️ Sin energía suficiente...")

class PokemonElectrico(Pokemon):
    def atacar(self):
        if self.ep >= 20: self.ep -= 20; print("⚡ ¡IMPACTRUENO!")
        else: print("⚠️ Sin energía suficiente...")

# --- EJECUCIÓN PRINCIPAL ---
print("\n>>> BIENVENIDO AL CENTRO DE ENTRENAMIENTO <<<")
mostrar_catalogo_disponible()

seleccion = input("\nIngrese el ID del Pokémon: ")

if seleccion in CATALOGO_POKEMON:
    d = CATALOGO_POKEMON[seleccion]
    
    # Mapeo de tipos a sus respectivas clases
    clases = {
        "Fuego": PokemonFuego, "Agua": PokemonAgua, 
        "Planta": PokemonPlanta, "Electrico": PokemonElectrico
    }
    
    # Instanciamos usando el tipo del catálogo
    clase_elegida = clases.get(d['tipo'], Pokemon)
    mi_poke = clase_elegida(d['nombre'], d['tipo'], d['hp_maximo'], d['energia_maxima'])

    while True:
        mi_poke.mostrar_hud()
        print("1. Atacar | 2. Descansar | 3. Salir")
        op = input("Selección: ")

        if op == "1":
            mi_poke.atacar()
        elif op == "2":
            mi_poke.descansar()
        elif op == "3":
            print("Cerrando Pokédex...")
            break
else:
    print("ID no válido.")