class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        # Debe retornar el texto "{titulo}" escrito por {autor}
        return f'"{self.titulo}" escrito por {self.autor}'

class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal

        self.catalogo = []

    def agregar_libro(self, nuevo_libro):

        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self):

        print(f"\n--- INVENTARIO DE LA SUCURSAL: {self.nombre_sucursal} ---")
        
        for libro in self.catalogo:

            print(libro)
        
        print("-" * 50)

if __name__ == "__main__":

    libro1 = Libro("El rastro de tu sangre en la nieve", "Gabriel García Márquez")
    libro2 = Libro("Crónicas de una muerte anunciada", "Gabriel García Márquez")
    libro3 = Libro("La ciudad y los perros", "Mario Vargas Llosa")

    mi_biblioteca = Biblioteca("Librería Central")

    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)

    mi_biblioteca.mostrar_inventario()
    