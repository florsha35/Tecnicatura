import math
#Ejercio1  A) Crear lista B) Eliminar elementos repetidos
# ListaAlumnos = ['Fiorela','Marina', 'Virginia', 'Florencia','Marina','Valentina','Virginia'] # creo una lista
# conjunto = set(ListaAlumnos) # Convierto a set, que no permite elementos repetidos
# ListaAlumnos = list((conjunto)) # vuelvo a convertir el set a lista y ya no tengo nada duplciado
# ListaAlumnos = list(set(ListaAlumnos)) # Lo anterior en una sola linea
# print(ListaAlumnos) # veo elementos repetidos


#Ejercicio2  a)crear dos listas
# lista = ['Mishina','Peters','Kira','Matilda']
# lista1 = ['Kira','Chubaki','Philippo','Greta','Berta','Emma']
# print(lista+lista1) # Lista de palabras que aparecen en la lista
# conjunto = set(lista)
# conjunto1 = set(lista1)
# solo1 = list(conjunto - conjunto1) #palabras que aparecen en la prim y no en la seg lista
# solo2 = list(conjunto1 - conjunto)
# print (solo1)#palabras que aparecen en la seg y no en la prim lista
# print(solo2)
# ambas = (conjunto & conjunto1)#palabras que aparecen en ambas listas
# print(ambas)



#Ejercicio3 Agregar personajes a la lista
# diccionario = {
#     1 : {'nombre' : 'Aragon', 'Clase' : 'Guerrero', 'Raza' : 'Dúnadan del norte'},
#     2 : { 'Nombre' : 'Gandalf', 'Clase' : 'Mago', 'Raza' : 'Istar'}
# }
#
# diccionario['3'] = {'Nombre' : 'Legolas', 'Clase' : 'Arquero', 'Raza' : 'Elfo'}
# print(diccionario)



#Ejercicio4, calcular la raiz cuadrada de un num
# numero = int(input('Digite un numero positivo'))
# while numero < 0:
#     print('Error -> deberia ser un numero positivo')
#     numero = int(input('Digite un numero positivo: '))
# print(f' \n Su raiz cuadrada es: {math.sqrt(numero):.2f}')



#Ejercicio Llenar una lista del 1 al 50, mostrarla con bucle for
# lista = []
# i = 1
# while i <= 50:
#     lista.append(i)
#     i += 1
# lista= list(range (1,51))
# for i in lista:
#     print (i, end= '-')


# #Ejercicio Modificar los elementos de una lista
# lista = list(range(1-11))
# print(lista)
# for i in lista:
#     print(i, end='-')
# valor = int(input('digite un valor entero: '))
# for indice, i in enumerate(lista):
#     lista[indice] *= valor
#
# print(f' Lista final de los elementos multiplicados por {valor}')
# for i in lista:
#     print(i, end='-')

#Ejercicio insertar elementos y ordenarlos
# lista = []
# salir = False
# while not salir:
#     numero = int(input('Digite un numero: '))
#     if numero == 0:
#         salir = True
#     else:
#          lista.append(numero)
# lista.sort()
# print(lista)