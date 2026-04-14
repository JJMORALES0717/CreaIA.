# ==========================================
#   SISTEMA DE LECTURA DE REGISTROS 
# ==========================================

def procesar_archivo():
    nombre_archivo = 'registro.txt'
    contador = 0

    print("--- INICIANDO LECTURA DE DATOS ---")
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:

            for linea in archivo:
                # Limpiamos y mostramos la línea
                dato_limpio = linea.strip()
                print(f" > {dato_limpio}")

                contador += 1
                
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{nombre_archivo}'.")
        return

    print("-" * 34)
    print(f" Total de lineas leídas: {contador}")
    print("-" * 34)

if __name__ == "__main__":
    procesar_archivo()