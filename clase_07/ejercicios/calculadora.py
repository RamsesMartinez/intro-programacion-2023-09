class Calculadora:
    def dividir(self, a, b):
        result = 0
        try:
            result = a / b
        except ZeroDivisionError:
            print("No puedes dividir por cero.")
            return None
        except TypeError:
            print("Los operandos deben ser números.")
        finally:
            print("Llegamos al finally!!!!")
        return result

calc = Calculadora()

# Ejemplo de uso correcto
print(calc.dividir(10, 2)) 
# 5.0


# Ejemplo de división por cero
print(calc.dividir(10, 0)) 
# No puedes dividir por cero.
# None

# Ejemplo con tipos de datos incorrectos
print(calc.dividir("diez", 2)) 
# Los operandos deben ser números.
# None
print(calc.dividir(None, 2)) 

