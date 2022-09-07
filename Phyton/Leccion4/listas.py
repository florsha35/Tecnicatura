# listas

# nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
# print(nombres)
# print(nombres[1])
# print(nombres[-1])
# # listas
#
# nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
# print(nombres)
# print(nombres[1])
# print(nombres[-1])
#
# print(nombres[0:2])
#
# #recorrer de principio al que le indique
# print(nombres[ :3])
#
# # del princio a fin
# print(nombres[1: ])
#
# #modificamos un valor
# nombres[3] = 'liliana'
# print(nombres)
#
# #iterar una lista
# for nombre in nombres:   # nombre es singular, la lista es plural
#     print(nombre)
# else:
#     print('Se acabaron los nombres de la lista')
#
# #preguntamos cuántos elementos tiene una lista
# print(len(nombres))
#
# agregar elemntos a la lista // ingresa al final
#  nombres.append('Marcelo')
# nombres.append([1, 2, 3])
# nombres.append(True)
# nombres.append(10.45)
# nombres.append([4, 5])
# nombres.append(7)
# print('Nombres')

#
# # insertar nuevo elemento en un indice(lugar) específico
# nombres.insert(2,'Alberto')
# print(nombres)
# nombres.insert(5,'Florencia')
# print(nombres)
#
# #eliminamos un elemento
# nombres.remove('Alberto')
# print(nombres)
#
# #eliminar el ultimo elemento
# nombres.pop()
# print(nombres)
#
# #eliminar un indice especifico
# del nombres[2] #del= delete
#
# #eliminar todos los elementos
# nombres.clear()
# print(nombres)
#
# #eliminar la lista
# del nombres

# print(nombres[0:2])
# lista1 = [1, 2, 3] # concatenar listas
# lista2 = [4, 5, 6]
# lista3 = lista1+lista2
# print(lista3)
#
# lista3.extend([7, 8, 9]) #agregar vs elementos a la lista
# print(lista3)
#
# print(lista3.index(5)) # funcion para ubicar en que indice esta el valor ingresado
# print(lista3.count(1)) #cuantos valor iguales a 1 hay en la lista
# lista3.reverse() #para poner al reves una lista
# print(lista3)
#
# lista3 = lista3 * 2 #multiplico el contenido de la lista
# print(lista3)
#
# # METODOS DE ORDENAMIENTO
# lista3.sort() # ordena ascendentemente
# lista2.sort(reverse=True) #ordena descendente
# print(lista3)


#recorrer de principio al que le indique
# print(nombres[ :3])




# #***** TUPLAS ******
# #Definimos una tupla
# cocina = ('cuchara','cuchillo,'tenedor)
# print(len(cocina))
#
# #acceder a un elemento de la tupla
# print(cocina[0])
# print(cocina[-1]) # para ver de manera inversa
#
# #acceder a un rango de la tupla
# print(cocina[0:1])
#
# #Recorrer elemento de la tupla
# for cocinar in cocina:
#     print(cocinar,end=' ') #print esta usando \n para saltos de lines
#
# cocina[0] = 'plato' #para cambiar el elem 0 por otro debe largar error porque no esta permitido en tuplas, son inmutables
#
# #convertir la tupla  a lsita para poder modificarla
# cocinaLista = list(cocina)
# cocinaLista[0] = 'plato'
# cocina = tuple(cocinaLista)
# print('\n' cocina)
#
# del cocina
# print(cocina) #elimine la tupla cocina

# del princio a fin
# print(nombres[1: ])
#
# #modificamos un valor
# nombres[3] = 'liliana'
# print(nombres)

#iterar una lista
# for nombre in nombres:   # nombre es singular, la lista es plural
#     print(nombre)
# else:
#     print('Se acabaron los nombres de la lista')
# //*******TIPO SET O CONJUNTO*******
# planetas = {'Marte','Júpiter','Venus'}
# print(len(planetas)) #para saber cuantos elementos tiene
# print(Marte in planestas) #saber si un elemento pertenece
# planetas.add('Tierra') #añado un elemento
# planetas.remove('Júpiter')

#preguntamos cuántos elementos tiene una lista
# print(len(nombres))
#
# #agregar elemntos a la lista // ingresa al final
# nombres.append('Marcelo')
# print('Nombres')
#
# # insertar nuevo elemento en un indice(lugar) específico
# nombres.insert(2,'Alberto')
# print(nombres)
# nombres.insert(5,'Florencia')
# print(nombres)





#//*******DICCIONARIO*****
#//DIC = (KEY : VALUE)
# diccionario ={
#     'IDE' :'Integrated Development Environment',
#     'POO' : 'Programacion Orientada a Objetos',
#     'SABD': 'Sistema de Administración de Base de Datos'
# }
# print(len(diccionario)) #cant de elementos
# print(diccionario)
# print(diccionario['IDE']) # uso la key para ver el valor dentro de la misma
# print(diccionario.get('IDE'))#otra forna de recuperar elemento
#
# diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
# print(diccionario)

#eliminamos un elemento
# nombres.remove('Alberto')
# print(nombres)
# for termino in diccionario:  # Recorrer y ver SOLO llaves
#     print(termino)
#
# for termino, valor in diccionario.items() # veo llaves y valores
#     print(termino, valor)

#eliminar el ultimo elemento
# nombres.pop()
# print(nombres)
# for termino in diccionario.keys(): #otra forma de ver las llaves
#     print(termino)
#
# for valor in diccionario.values(): #otra forma de ver valores
#     print(valor)

#eliminar un indice especifico
# del nombres[2] #del= delete

#eliminar todos los elementos
# nombres.clear()
# print(nombres)

#eliminar la lista
# print('IDE' in diccionario) # devuelve con valor booleando la existencia de un elemento
#
# diccionario['PK'] = 'Primary Key' #Agrego un elemto
# print(diccionario)
#
# diccionario.pop('SABD') #eliminar un elemento
# print(diccionario)
#
# diccionario.clear() # vaciar un diccionario
# print(diccionario)


#repaso de ser o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto.add('hola')
print(conjunto1)
print(3 not in conjunto1) #respuesta booleana

#como hacer la igualdad de dos conjuntos
print(conjunto == conjunto1)

conjunto3 = conjunto1 | conjunto # une los dos conjuntos
conjunto3 = conjunto1 & conjunto # ver que elemnto tienen en comun
conjunto3 = conjunto1 - conjunto # muestra q elemento esa en el primer conjunto y no en el segundo
conjunto3 = conjunto1 ^ conjunto #elementos q no comparten
print(conjunto3)
