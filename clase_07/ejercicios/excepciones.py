try:
    denominador = int(input("Ingresa un numero: "))
    print("Intentando el problema dentro del try...")
    resultado = 10 / denominador
    print(f"el resutlado es: {resultado}")
except ZeroDivisionError:
    resultado = None
    print("No puedes dividir por cero.")

