"""
1. Define una función que calcule el área de un círculo dado su radio.
"""
import math


def area_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"
    area = math.pi * (radio**2)
    return area


# Prueba de la función
radio = 5
print("El área del círculo es:", area_circulo(radio))
