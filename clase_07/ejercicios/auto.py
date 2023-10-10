"""
Crear una clase "Auto" que tenga las siguientes
 características:
    Atributos: 
        color, marca, modelo y velocidad_actual.
    Métodos:
         acelerar(), 
         frenar() y 
         mostrar_informacion().

    Solicitar al usuario que ingrese los datos del auto
    y luego mostrar esa información y 
    simular el comportamiento de acelerar y frenar
"""


class Auto:
    def __init__(self, color, marca, modelo):
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad_actual = 0

    def acelerar(self, velocidad):
        self.__velocidad_actual += velocidad
        print(f"La velocidad actual es {self.__velocidad_actual}")

    def frenar(self):
        self.__velocidad_actual = 0
        print("El auto se detuvo")

    def mostrar_informacion(self):
        print(f"- Color: {self.__color}")
        print(f"- Marca: {self.__marca}")
        print(f"- Modelo: {self.__modelo}")
        print(f"- Velocidad Actual: {self.__velocidad_actual}")


color = input("Ingrese el color del auto: ")
marca = "Nissan"
modelo = "Versa"
mi_auto = Auto(color, marca, modelo)
mi_auto.acelerar(10)
mi_auto.frenar()
mi_auto.mostrar_informacion()
