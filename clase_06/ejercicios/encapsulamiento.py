class Coche:
    def __init__(self, marca, modelo, color):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__precio = None
       
    # Métodos públicos
    def obtener_marca(self):
        return self.__marca
   
    def obtener_modelo(self):
        return self.__modelo
   
    def obtener_color(self):
        return self.__color
    
    def obtener_precio(self):
        return self.__precio
    
    def modificar_precio(self, precio):
        self.__precio = precio

    def modificar_color(self, color):
        self.__color = color
        
    def pisar_acelerador(self):
        print("Se está pisando el acelerador")
        self.__acelerar()

    # Métodos privados
    def __acelerar(self):
        print("El auto está acelerando")

    def __str__(self) -> str:
        return f"El auto es de color {self.__color}"

coche = Coche("Toyota", "BMW", "Rojo")
# coche.__color = "Verde" # No se debe hacer
# print(coche)
# coche.modificar_precio(100)
# coche.__acelerar()  # AttributeError: 'Coche' object has no attribute '__acelerar'

# coche.pisar_acelerador()  # El auto está acelerando


# Forma incorrecta
coche_2 = Coche("VW", "Jetta", "Blanco")
coche_2.__color = "VERDE"
print(coche_2.__color)

# Forma correcta:
coche_3 = Coche("VW", "Jetta", "Blanco")
coche_3.modificar_color("Verde")
print(coche_3.obtener_color())

