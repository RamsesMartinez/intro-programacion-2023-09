"""
9. Crea una lista con 3 elementos string, 
    1 elemento de tipo lista y ésta a su vez debe tener 3 elementos string. 
    Imprime los 4 elementos de la lista y los 3 sub elementos de la lista 
    en la posición 3.
"""

mi_lista = ["elemento1", "elemento2", "elemento3", ["subelemento1", "subelemento2", "subelemento3"]]

print("Elementos de la lista principal:")
for elemento in mi_lista:
    print(elemento)

print("Subelementos de la lista en la posición 3:")
for subelemento in mi_lista[3]:
    print(subelemento)
