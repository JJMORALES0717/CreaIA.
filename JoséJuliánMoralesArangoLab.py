# ==============================================
# Laboratorio Integrador - Sistema de Monitoreo
# de Presión Industrial
# Nombre: José Julián Morales Arango
# ==============================================

# Clase que representa un sensor de presión
class SensorPresion:

    # Atributos de clase
    LIMITE_PELIGRO = 200
    total_lecturas = 0

    # Constructor
    def __init__(self, nombre, presion):
        self.nombre = nombre
        self.__presion = 0

        # Validar la presión inicial
        self.presion = presion

        # Contador global
        SensorPresion.total_lecturas += 1

    # Getter
    @property
    def presion(self):
        return self.__presion

    # Setter con validación
    @presion.setter
    def presion(self, nueva_presion):
        if nueva_presion >= 0:
            self.__presion = nueva_presion


# ==============================================
# PROGRAMA PRINCIPAL
# ==============================================

lista_sensores = []

print("--- SISTEMA DE MONITOREO INDUSTRIAL ---")
print("Leyendo registros de presión...")

# Lectura del archivo
with open("registros.txt", "r") as archivo:

    while True:
        nombre = archivo.readline().strip()

        if nombre == "":
            break

        linea_presion = archivo.readline().strip()
        presion = int(linea_presion)

        sensor = SensorPresion(nombre, presion)
        lista_sensores.append(sensor)


# Escritura del archivo de alertas
contador = 1

with open("alertas.txt", "w") as archivo_salida:

    archivo_salida.write("REPORTE DE INCIDENCIAS - CALDERAS CRÍTICAS\n")
    archivo_salida.write("------------------------------------------\n")

    for sensor in lista_sensores:

        if sensor.presion > SensorPresion.LIMITE_PELIGRO:
            estado = "¡PELIGRO!"

            archivo_salida.write(str(contador) + ". " + sensor.nombre + "\n")
            contador += 1
        else:
            estado = "Seguro"

        print("Analizando:", sensor.nombre, "| Estado:", estado)


# Resumen final
print()
print("[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print("[RESUMEN] Total de sensores procesados:", SensorPresion.total_lecturas)
print("---------------------------------------")