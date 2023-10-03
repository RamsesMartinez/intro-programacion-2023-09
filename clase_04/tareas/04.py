"""
Crea dos sets, uno con los números del 1 al 5 y otro con los números del 3 al 7. 
- Encuentra la intersección y la diferencia entre ambos.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
interseccion = set1 & set2  # {3, 4, 5}
diferencia = set1 - set2  # {1, 2}
print("INTERSECCION:", interseccion, "DIFERENCIA:", diferencia)  # {3, 4, 5} {1, 2}
