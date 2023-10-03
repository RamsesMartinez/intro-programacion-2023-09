"""
2. Crea una función que tome una lista de números como argumento y devuelva el promedio de esos números.

"""

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return "La lista está vacía"
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio

# Prueba de la función
lista_de_numeros = [10, 20, 30, 40, 50]
print("El promedio de la lista de números es:", calcular_promedio(lista_de_numeros))
