#Iterar un rango de 0 a 10 e imprimir num divisibles entre3

print('rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

#Crear un rando de numeros de 2 a 6 e imprimirlo
print('Rango de valores que inicia en 2 y finaliza en 6')
rango = range(2, 7)
for i in rango:
    print(i)


# crear un rango de 3 a 10 con incremento de 2 en 2
print('Rango de valores de inicio en 3 y fin en 10')
for i in range(3, 11, 2):
    print(i)