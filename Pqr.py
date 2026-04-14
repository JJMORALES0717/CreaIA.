# ==========================================
# CLASE: Alumno (Más directo)
# ==========================================
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota  
        self.activo = True

    def ver_nota(self):
        return self.__nota

    def cambiar_nota(self, nueva_nota):
        if not self.activo:
            return "bloqueado"
        
        if 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
            return "ok"
        
        return "error_rango"

# ==========================================
# APP PRINCIPAL
# ==========================================

pibe = Alumno("Laura", 85)
intentos = 3

print(f"--- Gestión Académica: {pibe.nombre} ---")

while intentos > 0:
    try:
        print(f"\nTe quedan {intentos} {'oportunidad' if intentos == 1 else 'oportunidades'}.")
        n = int(input("Ingresá la nueva nota: "))
        
        status = pibe.cambiar_nota(n)
        
        if status == "ok":
            print(" Nota actualizada correctamente.")
            break
        
        elif status == "error_rango":
            intentos -= 1
            print(" Nota inválida. Probá con un número entre 0 y 100.")
            
    except ValueError:
        print(" Eso no es un número. Intentá de nuevo.")

if intentos == 0:
    pibe.activo = False
    print("\n" + "!" * 30)
    print("ACCESO DENEGADO")
    print("Cuenta bloqueada por seguridad.")
    print("!" * 30)

print(f"\nFinal -> Alumno: {pibe.nombre} | Nota: {pibe.ver_nota()} | Activo: {pibe.activo}")
