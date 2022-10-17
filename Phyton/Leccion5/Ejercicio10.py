#Ejercicio 10 -- no repetir caracteres
#Hacer un programa que pida una cadena por teclado,
#luego meter los caracteres en una lista sin repetirlos

cadena = input('Digite una cadena de elementos')
lista = []
for i in cadena:
    if i not in lista: # si el caracter ingresado no esta en la lista
        lista.append(i) #se agrega el caracter a la lista

    print(f'\n Lista de caracter sin repetir:\n{lista}')