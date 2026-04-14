# Tarea No. 2
total_latas = int(input("Total de latas: "))
latas_por_estante = int(input("Latas por estante: "))

estantes = total_latas // latas_por_estante
sobran = total_latas % latas_por_estante

print("Estantes que se llenan:", estantes)
print("Latas que sobran:", sobran)
