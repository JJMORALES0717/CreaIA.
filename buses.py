import random
import time
import os

bus1 = 0
bus2 = 0
bus3 = 0
meta = 50

while bus1 < meta and bus2 < meta and bus3 < meta:
    
    os.system("cls" if os.name == "nt" else "clear")
    
    bus1 += random.randint(1,3)
    bus2 += random.randint(1,3)
    bus3 += random.randint(1,3)

    print("META".rjust(meta + 5))
    print("Bus 1:", " " * bus1 + "🚌")
    print("Bus 2:", " " * bus2 + "🚌")
    print("Bus 3:", " " * bus3 + "🚌")

    time.sleep(0.3)

if bus1 >= meta:
    print("\n🏆 Ganó el Bus 1")
elif bus2 >= meta:
    print("\n🏆 Ganó el Bus 2")
else:
    print("\n🏆 Ganó el Bus 3")
    