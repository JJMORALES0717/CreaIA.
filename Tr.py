# ==========================================
#  SISTEMA DE GESTIÓN DE FLOTA: EJERCICIO 3
# ==========================================

# ========= 1. CLASES =========
class Camion:
    pass

class CentroLogistico:
    pass


# ========= 2. CREACIÓN DE CAMIONES =========
camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()


# ========= 3. GARAJE =========
garaje_principal = [camion1, camion2, camion3, camion4, camion5]


# ========= 4. PROCESAMIENTO =========
total_camiones = len(garaje_principal)
impuesto_total = total_camiones * 500


# ========= 5. SALIDA =========
print("\n" + "="*40)
print(" REPORTE DEL CENTRO LOGÍSTICO")
print("="*40)

print(f"Total de camiones: {total_camiones}")
print(f"Impuesto total: ${impuesto_total}")

print("\n Identificación de camiones:")
for i, camion in enumerate(garaje_principal, start=1):
    print(f"Camión {i} → ID: {id(camion)}")


# ========= 6. CONTROL DE CAPACIDAD =========
capacidad_maxima = 4

print("\n Estado del garaje:")
if total_camiones > capacidad_maxima:
    print(" Capacidad excedida!")
    print(" Debes mover camiones a otra sucursal.")
else:
    print(" Capacidad óptima.")


print("="*40)
print(" Fin del reporte")
print("="*40)
