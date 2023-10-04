"""
1. Crea una lista con 5 números enteros,
- agrega un número al final
- elimina el número en la posición 2
- modifica el último número por 100.
"""

numeros = [10, 20, 30, 40, 50,10, 20, 30, 40, 50,10, 20, 30, 40, 50,10, 20, 30, 40, 50,10, 20, 30, 40, 50]
numeros.append(60)
numeros.pop(2)
numeros[-1] = 100
print(numeros)  # [10, 20, 40, 50, 100]
