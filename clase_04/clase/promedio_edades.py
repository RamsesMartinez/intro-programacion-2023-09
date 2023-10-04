"""
2. Crea una función que tome una lista de números como argumento y devuelva el promedio de esos números.

"""

def calcular_promedio(lista_numeros: list):
    """
    10, 10

    formula = suma / total elementos
            = 20 / 2
            = 10
    []
    formula = suma / total elementos
            = 0 / 0
            = indef

    10 / 10 = 1
    10 / 5 = 2
    10 / 2 = 5
    10 / 1 = 10
    10 / 0.1 =  100
    10 / 0.01 = 1000
    10 / 0.001 = 10000
    """
    if len(lista_numeros) == 0:
        return "Lista vacía"
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio

# Prueba de la función
lista_de_numeros = []
print("El promedio de la lista de números es:", calcular_promedio(lista_de_numeros))
