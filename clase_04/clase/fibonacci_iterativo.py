"""
Diseña un programa que genere una secuencia de números Fibonacci utilizando una función recursiva.
"""

def fibonacci_iterativo(posicion):
    actual = 0
    siguiente = 1
    for _ in range(posicion + 1):
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal

# Solicitar al usuario el número de términos
n_terminos = int(input("Ingrese el número de términos de la secuencia Fibonacci que desea generar: "))

# Generar e imprimir la secuencia Fibonacci
print("Secuencia Fibonacci:")
for i in range(1, n_terminos + 1):
    print(fibonacci_iterativo(i))
