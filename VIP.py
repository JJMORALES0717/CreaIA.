# 1. La Lista Principal
lista_invitados = []

# 2. Funciones del Sistema
def agregar_invitado(nombre):
    
    lista_invitados.append(nombre.strip())
    print(f"{nombre} ha sido añadido a la lista.")

def mostrar_lista():
    print("\n--- CONTROL DE ACCESO VIP ---")
    if not lista_invitados:
        print("[ La lista está vacía actualmente ]")
    else:
        
        for i, invitado in enumerate(lista_invitados, 1):
            print(f"{i}. {invitado}")
    print("----------------------------")

def buscar_invitado(nombre):
    
    if nombre.strip().lower() in [i.lower() for i in lista_invitados]:
        return "El invitado ya está en la lista"
    else:
        return "Nombre disponible"

def eliminar_invitado(nombre):
   
    nombre_limpio = nombre.strip()
    
    
    encontrado = False
    for i in lista_invitados:
        if i.lower() == nombre_limpio.lower():
            lista_invitados.remove(i)
            print(f"{i} ha sido retirado del evento.")
            encontrado = True
            break
            
    if not encontrado:
        print(f" Error: '{nombre_limpio}' no figura en los registros.")

# 3. Menú de Usuario (Interfaz del Portero)
def ejecutar_menu():
    while True:
        print("\n--- MENÚ DEL GESTOR ---")
        print("1. Registrar nuevo invitado")
        print("2. Ver lista completa")
        print("3. Eliminar a alguien")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del invitado: ")
            estado = buscar_invitado(nombre)
            print(f"Resultado: {estado}")
            
            if estado == "Nombre disponible":
                agregar_invitado(nombre)
        
        elif opcion == "2":
            mostrar_lista()
            
        elif opcion == "3":
            nombre = input("¿A quién desea eliminar?: ")
            eliminar_invitado(nombre)
            
        elif opcion == "4":
            print("Sistema cerrado. ¡Que disfrutes la fiesta!")
            break
        else:
            print(" Opción no reconocida. Por favor, marca 1, 2, 3 o 4.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_menu()
    