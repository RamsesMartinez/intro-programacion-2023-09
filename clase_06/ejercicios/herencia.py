# Definición de la clase "Animal"
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"El animal {self.nombre} está hablando")

# Definición de la clase "Perro", que hereda de la clase "Animal"
class Perro(Animal):
    # def __init__(self, nombre):
    #    super().__init__("Sobreescribiendo " + nombre + "!")
    def hablar(self):
        # super().hablar()
        print(f"El perro {self.nombre} está ladrando!!! GUAU GUAU!")

# Creación de un objeto a partir de la clase "Animal"
mi_animal = Animal("Gato")

# Llamada al método "hablar" del objeto creado
mi_animal.hablar() # Imprime "El animal está hablando"

# Creación de un objeto a partir de la clase "Perro"
mi_perro = Perro("Firulais")

# Llamada al método "hablar" del objeto creado
mi_perro.hablar() # Imprime "El perro está ladrando"
