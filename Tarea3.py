# TAREA DEL MARTES 09/03/2026
print("Bienvenido a Cinepolis, me puede decir su edad y si compro su entrada para poderlo dejar entrar a la sala porfavor.")

edad = int(input("Ingrese su edad por favor: "))
entrada = input("¿Tiene entrada comprada? (si/no): ")

if edad >= 18 and entrada == "si":
    print(" Bienvenido puede ingresar a la película.")
else:
    print(" Lo siento pero no se permite la entrada.")

