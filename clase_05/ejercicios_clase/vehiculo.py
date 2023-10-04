class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f'Vehiculo {marca} {modelo} creado.')
        
    def __del__(self):
        print(f'Vehiculo {self.marca} {self.modelo} destruido.')
        
# Crear un objeto de la clase Vehiculo
mi_coche = Vehiculo("Toyota", "Corolla")

# No es necesario llamar al destructor explícitamente, pero aquí está el uso para demostración.
del mi_coche
