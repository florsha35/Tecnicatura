#Ejercicio 01 // crear una funcionar para sumar los valores  recibidos
#de tipo numerico, utilizando argumentos, variables
#como parametrod de la funcionar y agregar como resultado la suma de todos los argumentos

def sumar_valor(*args):
    resultado = 0
    for valor in args: #iterar cada elemento
        resultado += valor
    return resultado


print(sumar_valor(6,4,8,6,2,7))

