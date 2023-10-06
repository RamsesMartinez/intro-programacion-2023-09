"""
Ejercicio con Constructor:
Crear una clase llamada Estudiante.
Utilizar el constructor __init__ para tomar nombre, edad y grado como parámetros 
    y asignarlos a atributos del objeto.
Crear un método presentarse que imprima un mensaje que diga: 
    "Hola, mi nombre es [nombre], tengo [edad] años y estoy en [grado] grado".
Crear un objeto de Estudiante
 y llamar al método presentarse.
"""

class Estudiante:
    def __init__(self, nombre, edad, grado) -> None:
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estoy en {self.grado} grado.")

anita = Estudiante("ana", 15, "tercero")
anita.presentarse()