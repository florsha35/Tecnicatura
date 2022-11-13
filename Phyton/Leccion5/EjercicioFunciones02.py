#Funcion con *arg para multiplicar
#crear una funciona para multiplicar valores recibidiso
#numero, utilizando argumentos varibles *args
#como parametro de la funcion y regresr como resultado
#la multiplciacion de todos los valores ingresados como argumentos


def multiplicar_valores (*numeros):
    resultado = 1 #arranco del 1 pq el 0mno multiplica
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(3,5,15)) #llame  ala funcion
