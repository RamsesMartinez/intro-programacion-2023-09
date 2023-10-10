"""
Crear una clase "Empleado" con lo siguientes:
    Atributos: nombre, edad, salario y departamento.
    Métodos: mostrar_informacion(), es_jubilable() y aumentar_salario().
"""


class Empleado:
    
    def __init__(self, nombre, edad, salario, departamento, anios_servicio) -> None:
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento
        self.anios_servicio = anios_servicio


    def mostrar_informacion(self):
        return (
            f"Nombre: \"{self.nombre}\"\n"
            f"Edad: \"{self.edad}\"\n"
            f"Salario: \"{self.salario}\"\n"
            f"Departamento: \"{self.departamento}\""
        )

    def es_jubilable(self) -> str:
        """
        Una persona se puede jubilar si cumple las siguientes condiciones
            - 65 años
            - 30 años de servicio cotizados (1500 semanas aprox)


        # Operaciones ternarias:
        if edad > 10:
            resultado = "Algo aqui"
        else:
            resultado = "Algo acá"
        resultado = "Algo aqui" if edad > 10 else "Algo acá"
        """
    
        return "Es jubilable: " + str(False if self.edad < 65 or self.anios_servicio < 30 else True)

    def aumentar_salario(self, aumento):
        self.salario += aumento
        return f"El salario de {self.nombre} ahora es de $ {self.salario}"

empleado_1 = Empleado("Ana", 45, 15000, "RRHH", 25)
empleado_2 = Empleado("Luis", 65, 15000, "RRHH", 35)

print(empleado_2.mostrar_informacion())
print(empleado_2.es_jubilable())
print(empleado_2.aumentar_salario(1000))