
class Animal:
    def __init__(self, name) -> None:
        self.__name = name
        self.__apodo = None

    @property
    def name(self):
        return self.__name
    
    @property
    def apodo(self):
        return self.__apodo

    @apodo.setter
    def apodo(self, apodo):
        if apodo == "":
            print("El apodo no puede estar vacío")
            raise Exception("Animal Name exception")
        if type(apodo) == int:
            print("El apodo no puede ser un número")
            raise Exception("Animal Name exception")
        
        self.__apodo = apodo

    def make_sound(self):
        pass

    def move(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print(f"Lion {self.name} roars")
    
    def move(self):
        print(f"Lion {self.name} is running")


class Snake(Animal):
    def make_sound(self):
        print(f"Snake {self.name} hiss")
    
    def move(self):
        print(f"Snake {self.name} is slithering")


class Bird(Animal):
    def make_sound(self):
        print(f"Bird {self.name} sings")
    
    def move(self):
        print(f"Bird {self.name} is flying")


class Visitor:
    def interact_with_animal(self, animal:Animal):
        animal.make_sound()
        animal.move()
        self.crear_apodo(animal)

    def crear_apodo(self, animal: Animal):
        animal.apodo = 1234
        print("El apodo del animal ahora es: " + animal.apodo)

    def zoo_simulation(self, list_animals):
        for animal in list_animals:
            self.interact_with_animal(animal)
    



animals = [Lion("King")]
juan = Visitor()
juan.zoo_simulation(animals)

