#Ejercicio Funcion Recursiva
#imprimir numero del 5 a 1 de manera descendente
#usando funciones recursivas

def imprimirNumDescendente(numero):
    if numero >= 1:
        print(numero)
        imprimirNumDescendente(numero-1)
    elif numero <=0:
        print('Valor incorrecto, numero negativo')
imprimirNumDescendente(5)