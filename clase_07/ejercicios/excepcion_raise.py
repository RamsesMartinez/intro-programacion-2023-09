def validar_edad(edad):
    if edad < 0:
        raise Exception("La edad no puede ser negativa")

try:
    validar_edad(-10)
except Exception as msg:
    print("El error introducido es incorrecto: ", str(msg))

print("Continuo el proyecto sin problemas")


