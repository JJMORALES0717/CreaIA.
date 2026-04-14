#Ejercicio No.1: Centro de Control de Drones "SkyWatch"

class DronVigilancia:
    def __init__(self, nombre, modelo):
        # Al crear el dron, asignamos su identidad y valores iniciales
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado_vuelo = "En Tierra"
        self.integridad = 100  # Salud física del dron
        self.historial = []    # Lista para guardar los eventos (bitácora)

    def registrar_evento(self, evento):
        # Agregamos un texto a la lista de historial para llevar el control
        self.historial.append(evento)

    def despegar(self):
        # Primero revisamos si el dron ya está en el aire
        if self.estado_vuelo == "En Tierra":
            # Verificamos que el dron no esté muy dañado (integridad)
            if self.integridad < 50:
                print(f"[PELIGRO: Integridad al {self.integridad}%. Requiere reparación antes de volar].")
            # Verificamos si tiene suficiente energía para subir
            elif self.bateria >= 25:
                self.estado_vuelo = "En Vuelo"
                self.registrar_evento("Despegue exitoso")
                print("¡Despegue exitoso! El dron está en el aire.")
            else:
                # Si tiene menos de 25%, no lo dejamos salir
                print(f"[ERROR: Batería insuficiente ({self.bateria}%).]")
        else:
            print("[ERROR: El dron ya está volando].")

    def patrullar(self):
        # El patrullaje solo se puede hacer si el dron ya despegó
        if self.estado_vuelo == "En Vuelo":
            # Restamos 30 de batería por el esfuerzo del patrullaje
            # max(0, ...) asegura que la batería nunca sea un número negativo
            self.bateria = max(0, self.bateria - 30)
            self.registrar_evento(f"Patrullaje (Batería restante: {self.bateria}%)")
            print(f"Patrullaje completado. Batería: {self.bateria}%.")
            
            # Si después de patrullar la batería es muy baja (menos de 10)
            if self.bateria < 10:
                self.estado_vuelo = "En Tierra" # El dron cae/aterriza
                self.integridad -= 20           # El aterrizaje brusco daña el dron
                self.registrar_evento("EMERGENCIA: Aterrizaje por batería baja (-20% integridad)")
                print("ALERTA: Batería crítica. Aterrizaje de emergencia realizado.")
        else:
            print("[ERROR: El dron debe estar en vuelo para patrullar].")

    def aterrizar(self):
        # Solo podemos aterrizar si estamos volando
        if self.estado_vuelo == "En Vuelo":
            self.estado_vuelo = "En Tierra"
            self.registrar_evento("Aterrizaje manual exitoso")
            print("Aterrizaje completado con éxito.")
        else:
            print("[ERROR: El dron ya está en tierra].")

    def recargar(self):
        # Por seguridad, no se puede cargar la batería mientras vuela
        if self.estado_vuelo == "En Tierra":
            self.bateria = 100
            self.registrar_evento("Recarga completa de batería")
            print("Batería cargada al 100%.")
        else:
            print("[ERROR: No se puede recargar mientras vuela].")

    def reparar(self):
        # Solo se puede reparar si el dron está apagado en tierra
        if self.estado_vuelo == "En Tierra":
            self.integridad = 100
            self.registrar_evento("Mantenimiento y reparación completa")
            print("Dron reparado. Integridad al 100%.")
        else:
            print("[ERROR: No se puede reparar en el aire].")

    def mostrar_reporte(self):
        # Imprimimos una interfaz visual con los datos finales
        print(f"\n{'='*30}")
        print(f"REPORTE FINAL: {self.nombre}")
        print(f"Estado final: {self.estado_vuelo}")
        print(f"Batería: {self.bateria}% | Integridad: {self.integridad}%")
        print("-" * 30)
        # Recorremos el historial y mostramos cada evento con su número de orden
        for i, evento in enumerate(self.historial, 1):
            print(f"{i}. {evento}")
        print(f"{'='*30}")
#========================================================================================================

#Ejercicio No.2: Sistema de Bio-Ingenería "Ares-1"

class PlantaEspacial:
    def __init__(self, nombre, especie):
      
        self.nombre = nombre
        self.especie = especie
        self.hidratacion = 100
        self.salud = 100
        self.estado = "Saludable"

    def regar(self):
       
        if self.estado == "Marchita":
            print(f"Imposible regar. {self.nombre} está marchita.")
            return

        self.hidratacion += 15
        if self.hidratacion > 100:
            self.hidratacion = 100
        print(f"Suministrando agua... Hidratación actual: {self.hidratacion}%.")

    def pasar_dia(self):
        if self.estado == "Marchita":
            print("El tiempo pasa, pero la planta ya no tiene vida.")
            return

        self.hidratacion -= 20
        print(f"Ha pasado un día en Marte. La hidratación bajó a {self.hidratacion}%.")

        if self.hidratacion < 30:
            self.salud -= 40
            print(f"¡ALERTA! Hidratación crítica. La salud de {self.nombre} ha sufrido daños.")

        if self.salud <= 0:
            self.salud = 0
            self.estado = "Marchita"
            print(f"ESTADO CRÍTICO: {self.nombre} se ha marchitado.")

# --- Programa Principal (Monitor del Laboratorio) ---
print(">>> INICIANDO SISTEMA DE BIO-INGENIERÍA ARES-1 <<<")
n = input("Nombre de la planta: ")
e = input("Especie de la planta: ")
mi_planta = PlantaEspacial(n, e)

while True:
    print(f"\nREPORTE DE BIO-MONITOR: {mi_planta.nombre}")
    print(f"Estado: {mi_planta.estado} | Hidratación: {mi_planta.hidratacion}% | Salud: {mi_planta.salud}%")
    
    opcion = input("¿Qué acción desea realizar? (1. Regar / 2. Dejar pasar día / 3. Salir): ")
    
    if opcion == "1":
        mi_planta.regar()
    elif opcion == "2":
        mi_planta.pasar_dia()
    elif opcion == "3":
        print("Saliendo del monitor de bio-ingeniería...")
        break
    else:
        print("Opción no válida.")

