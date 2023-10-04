# Definición de la clase "Gato"
class Gato:
    # Definición del atributo "color"
    color = "Negro"  # Atributo de instancia
    # Definición del método "maullar"
    def maullar(self):  # Método de instancia
        print("Miau! Miau!")
    
    def correr(self):
        print("Esta corriendo!!!")

gatito = Gato()
gatito.maullar()
gatito.correr()