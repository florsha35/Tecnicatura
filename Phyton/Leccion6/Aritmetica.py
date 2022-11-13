class Aritmetica:
    """"
    El nombre de este tipo de comentario con 3 comillas es DocString
    esto es una documentacion de la clase en Phyton
    vamos a hacer algunas operaciones de : suma, resta, multiplicaciones y mas
    """

    def __init__(self, operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB
    #metodo para sumar
    def sumar(self):
        return self.operadorA + self.operadorB

    def resta(self):
        return self.operadorA - self.operadorB

    def multiplicar(self):
        return self.operadorA * self.operadorB

    def dividir(self):
        return self.operadorA / self.operadorB

aritmetica1 = Aritmetica(7, 9) #los aegumentos para el operador A y B
print(aritmetica1.sumar())
print(f' La resta de los numeros es {aritmetica1.resta()}')
print(f' La division de los numeros es {aritmetica1.multiplicar()}')
print(f' La division de los numeros es {aritmetica1.dividir(): .2f}')