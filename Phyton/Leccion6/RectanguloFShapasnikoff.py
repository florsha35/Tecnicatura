"""
Crear una clase llamada rectangulo, debe tener dos atributos: altura y base
el nombre de metodo sera calcular area utilizando la forma
area = base * altura, los que deben ser ingresador por el usuario y los objetos deben ser tres
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
base = int(input('Digite la base del rectangulo'))
altura = int(input('Digite la altura del rectangulo'))

base1 = int(input('Digite la base del rectangulo'))
altura1 = int(input('Digite la altura del rectangulo'))

base2 = int(input('Digite la base del rectangulo'))
altura2 = int(input('Digite la altura del rectangulo'))

rectangulo1 = Rectangulo(base, altura)

rectangulo2 = Rectangulo(base1, altura1)

rectangulo3 = Rectangulo(base2, altura2)
print(f' El area del rectangulo es: {rectangulo1.calcular_area()}')
print(f' El area del rectangulo es: {rectangulo2.calcular_area()}')
print(f' El area del rectangulo es: {rectangulo3.calcular_area()}')