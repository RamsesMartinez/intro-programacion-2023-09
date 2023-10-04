class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.year = "1990"
        print(f'Vehiculo {marca} {modelo} creado.')

    def __del__(self):
        print(f'Vehiculo {self.marca} {self.modelo} destruido.')

    def __str__(self) -> str:
        return "HOLA! este es un auto de la marca " + self.marca

# Crear un objeto de la clase Vehiculo
mi_coche = Vehiculo("Toyota", "Corolla")
coche_2 = Vehiculo("VolksWagen", "Jetta")

print(mi_coche)

mi_coche.marca = "TOYATA!"

print(mi_coche)

print(coche_2)



