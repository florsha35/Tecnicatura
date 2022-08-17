# listas

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[1])
print(nombres[-1])

print(nombres[0:2])

#recorrer de principio al que le indique
print(nombres[ :3])

# del princio a fin
print(nombres[1: ])

#modificamos un valor
nombres[3] = 'liliana'
print(nombres)

#iterar una lista
for nombre in nombres:   # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los nombres de la lista')

#preguntamos cuántos elementos tiene una lista
print(len(nombres))

#agregar elemntos a la lista // ingresa al final
nombres.append('Marcelo')
print('Nombres')

# insertar nuevo elemento en un indice(lugar) específico
nombres.insert(2,'Alberto')
print(nombres)
nombres.insert(5,'Florencia')
print(nombres)

#eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[2] #del= delete

#eliminar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista