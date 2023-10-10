"""
Crear una clase "Animal" y subclases como "Mamifero", "Ave" y "Pez", 
cada una con características y métodos propios.
Crear al menos un objeto de cada subclase y mostrar cómo se utilizan 
sus métodos y atributos específicos.
"""

class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def comer(self):
        return f"EL animal {self.nombre} está comiendo"
    
    def dormir(self):
        return f"EL animal {self.nombre} está durmiendo"
        

class Mamifero(Animal):
    def __init__(self, nombre, edad) -> None:
        super().__init__(nombre)
        self.edad = edad
    
    def correr(self):
        return f"El mamifero {self.nombre} está corriendo"

    def mostrar_informacion(self):
        return f"El mamifero {self.nombre} tiene {self.edad} años"

class Ave(Animal):
    def __init__(self, nombre, color_plumas) -> None:
        super().__init__(nombre)
        self.color_plumas = color_plumas

    def volar(self):
        return f"El ave {self.nombre} está volando"
    
    def mostrar_informacion(self):
        return f"El Ave {self.nombre} tiene las plumas de color {self.color_plumas}"


class Pez(Animal):
    def __init__(self, nombre, color_escamas) -> None:
        super().__init__(nombre)
        self.color_escamas = color_escamas
    
    def nadar(self):
        return f"El pez {self.nombre} está nadando"
    
    def mostrar_informacion(self):
        return f"El Pez {self.nombre} tiene las escamas de color {self.color_escamas}"

vaca = Mamifero("Lola", 3)
aguila = Ave("Juan", "cafés")
salmon = Pez("Salomón", "azules")

print(vaca.correr())
print(vaca.mostrar_informacion())

print(aguila.volar())
print(aguila.mostrar_informacion())

print(salmon.nadar())
print(salmon.mostrar_informacion())