"""
Ejercicio integrador
Crear una función llamada filtrar_pares que tome una lista de números como parámetro y retorne una nueva lista que contenga solo los números pares de la lista original. Deberás utilizar un bucle for para iterar sobre la lista original y una lista para almacenar los números pares
"""

def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Prueba de la función
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filtrar_pares(lista_original)
print("Lista Original:", lista_original)
print("Lista de Pares:", lista_pares)
