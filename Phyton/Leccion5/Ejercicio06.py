# Tabla de multiplicar

numero = int(input('Digite un numero'))
lista =[] # Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f'\n Tabla de multiplicar del {numero}; \n {lista}')

for indice, i in enumerate(lista):
        print(f'{numero} x {i} = {lista[indice]}') # de esta forma vemos uno por uno el resultado que va arrojando