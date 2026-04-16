class Libro:
    """Clase que representa un libro individual."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):

        return f'"{self.titulo}" escrito por {self.autor}'


class Biblioteca:
    """Clase que gestiona el catálogo de una sucursal."""
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []

    def agregar_libro(self, nuevo_libro):
        """Añade un objeto Libro a la lista del catálogo."""
        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self):
        """Imprime el inventario con un diseño limpio."""
        titulo_seccion = f" INVENTARIO: {self.nombre_sucursal} "
        print("\n" + "=" * 50)
        print(titulo_seccion.center(50, " "))
        print("=" * 50)
        
        if not self.catalogo:
            print("El catálogo está vacío actualmente.")
        else:
            for i, libro in enumerate(self.catalogo, 1):

                print(f"{i}. {libro}")
        
        print("=" * 50 + "\n")

if __name__ == "__main__":

    l1 = Libro("El rastro de tu sangre en la nieve", "Gabriel García Márquez")
    l2 = Libro("Crónicas de una muerte anunciada", "Gabriel García Márquez")
    l3 = Libro("La ciudad y los perros", "Mario Vargas Llosa")

    mi_biblioteca = Biblioteca("Biblioteca Nacional de Guatemala")

    mi_biblioteca.agregar_libro(l1)
    mi_biblioteca.agregar_libro(l2)
    mi_biblioteca.agregar_libro(l3)

    mi_biblioteca.mostrar_inventario()
    