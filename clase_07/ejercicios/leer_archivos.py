"""
Escribe un programa en Python que:
    Pida al usuario el nombre de un archivo de texto para leer.
    Lea el archivo e imprima su contenido en la pantalla.
    Use excepciones para manejar los casos donde el archivo 
        no pueda ser encontrado o leído.
"""


def leer_archivo(nombre_archivo: str):
    """
    Este método permitirá leer un archivo a partir del nombre que
    indique el usuario
    :param nombre_archivo : Indica el nombre del archivo que será leído
    """
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print(f"No se pudo encontrar el arhivo: \"{nombre_archivo}\"")
    except Exception as e:
        print(f"Ocurrió un error: {e}" )

nombre_archivo = input("Por favor, indica el nombre del archivo a leer: ")
leer_archivo(nombre_archivo)

print("Fin del programa")