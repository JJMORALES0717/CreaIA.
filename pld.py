class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):

        self.nombre = nombre_alumno          
        self.__nota = nota_inicial          
        self.cuenta_activa = True           

    def get_nota(self):
        return self.__nota

    def bloquear_cuenta(self):
        self.cuenta_activa = False

    def set_nota(self, nueva_nota):
        if not self.cuenta_activa:
            return -2  
        
        if 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
            return 1   
        else:
            return -1  

# --- PROGRAMA PRINCIPAL ---

alumna = RegistroAcademico("Laura", 85)

intentos_permitidos = 3

while intentos_permitidos > 0:
    try:
        print(f"\nIntentos restantes: {intentos_permitidos}")
        nota_ingresada = float(input("Ingrese la nueva nota para el alumno: "))
       
        resultado = alumna.set_nota(nota_ingresada)
        
        if resultado == 1:
            print("¡Felicidades! La nota ha sido actualizada correctamente.")
            break
        elif resultado == -1:
            intentos_permitidos -= 1
            print("Error: La nota debe estar entre 0 y 100.")
            if intentos_permitidos > 0:
                print("Por favor, intente de nuevo.")
                
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        intentos_permitidos -= 1

if intentos_permitidos == 0:
    alumna.bloquear_cuenta()
    print("\n--- SISTEMA BLOQUEADO ---")
    print("Se han agotado los intentos. La cuenta ha sido bloqueada por seguridad.")