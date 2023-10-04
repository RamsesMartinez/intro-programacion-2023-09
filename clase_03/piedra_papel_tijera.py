"""
Jugador -> Piedra
Computadora -> Piedra
Empate

J -> Papel
C -> Piedra
Gané

C -> Tijera
J -> Papel
Perdí
"""
import random

OPCIONES = ("piedra", "papel", "tijeras")


def obtener_opciones() -> dict:
    """
    Regresa un diccionario con las opciones del jugador y de la computadora
    """
    opcion_del_jugador = input("Elije una opción: (piedra, papel, tijeras): ")
    opcion_de_la_computadora = random.choice(OPCIONES)
    opciones = {
        "jugador": opcion_del_jugador,
        "computadora": opcion_de_la_computadora
    }
    return opciones


def obtener_resultado(opcion_jugador, opcion_computadora):
    if opcion_jugador == opcion_computadora:
        return "Es un empate!"
    elif opcion_jugador == "piedra":
        if opcion_computadora == "tijeras":
            return "Piedra destroza tijeras... ¡Ganaste!"
        else:  # la computadora eligió papel
            return "Papel envuelve a piedra... Perdiste :("
    elif opcion_jugador == "papel":
        if opcion_computadora == "tijeras":
            return "Tijeras cortan papel... Perdiste :("
        else:  # Computadora eligió piedra
            return "Papel envuelve a piedra... ¡Ganaste!"
    elif opcion_jugador == "tijeras":
        if opcion_computadora == "papel":
            return "Tijeras cortan papel... ¡Ganaste!"
        else:  # Computadora eligió piedra
            return "Piedra destroza tijeras... Perdiste :("

    return "La computadora ganó"


opciones: dict = obtener_opciones()
resultado = obtener_resultado(opciones["jugador"], opciones["computadora"])
print(resultado)

