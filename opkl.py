
with open('nombres.txt', 'r') as archivo:

    total_personas = 0

    for nombre in archivo:

        print(nombre.strip())

        total_personas += 1

print(f"Total de personas anotadas: {total_personas}")