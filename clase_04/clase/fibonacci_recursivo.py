"""
Diseña un programa que genere una secuencia de números Fibonacci utilizando una función recursiva.
"""

def fibonacci_recursivo(posicion):
    if posicion < 2:
        return posicion
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# Solicitar al usuario el número de términos
n_terminos = int(input("Ingrese el número de términos de la secuencia Fibonacci que desea generar: "))

# Generar e imprimir la secuencia Fibonacci
print("Secuencia Fibonacci:")
for i in range(1, n_terminos + 1):
    print(fibonacci_recursivo(i))
