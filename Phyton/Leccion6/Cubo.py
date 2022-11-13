"""
Crear la clase Cubo con los atributos: alto, ancho y profundidad
con un metodo calcular_volumen que trendra la formula:
volumen = ancho * alto * profundidad que el usuario ingresara
"""

class Cubo:
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad

alto = int(input('Digite el alto del cubo'))
ancho = int(input('Digite el ancho del cubo'))
profundidad = int(input('Digite la profundidad del cubo'))

cubo = Cubo(alto, ancho, profundidad)
print(f' El volumen del cubo es {cubo.calcular_volumen()}')