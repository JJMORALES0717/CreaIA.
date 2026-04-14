#ejemplo

# 1. Crear clase FacturaEmitida

class FacturaEmitida:
    pass

# 2. Crear clase TerminalDePago
class TerminalDePago:
    pass

# 3. Crear dos objetos de FacturaEmitida
factura_001 = FacturaEmitida()
factura_002 = FacturaEmitida()

# 4. Crear un objeto de TerminalDePago
terminal_principal = TerminalDePago()

# 5. Mostrar el tipo del objeto terminal_principal
print("Tipo de terminal_principal:", type(terminal_principal))

# 6. Mostrar el ID (dirección en memoria) de las facturas
print("ID factura_001:", id(factura_001))
print("ID factura_002:", id(factura_002))

# 7. Evaluar si los IDs son iguales
print("¿factura_001 y factura_002 son iguales?:", id(factura_001) == id(factura_002))
