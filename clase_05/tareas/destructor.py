"""
Ejercicio con Destructor:
Crear una clase llamada Libro.
Utilizar el constructor para tomar titulo y autor y asignarlos a atributos del objeto.
Utilizar el destructor para imprimir un mensaje que diga: 
    "El libro [titulo] de [autor] fue destruido".
Crear un objeto de Libro y luego destruirlo utilizando del. Observar el mensaje del destructor.
"""


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.paginas = None
        # print(f"Libro {titulo} de {autor} fue creado")

    def __del__(self):
        print(f"Libro {self.titulo} {self.autor} destruido. ")

    def __str__(self) -> str:
        if self.paginas is None:
            return f"El libro {self.titulo} no tiene páginas configuradas"
        return f"El libro {self.titulo} tiene {self.paginas} páginas en total"

mi_libro = Libro(
    "Cien años de soledad", "Gabriel Garcia Marquez"
)  # Libro Cien años de soledad de Gabriel Garcia Marquez fue creado

libro_2 = Libro(
    "Harry Potter 1", "J.K. Rowling"
)  # Libro Harry Potter de J.K. Rowling fue creado

libro_3 = Libro(
    "Harry Potter 3", "J.K. Rowling"
)  # Libro Harry Potter de J.K. Rowling fue creado

