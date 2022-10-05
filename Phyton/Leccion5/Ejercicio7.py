#Juego adivina el numero

import random
print("\t Juego Adivina el Numero")
aleatorio = random.randint(0,100)
contador = 0
while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print("\t no es el número, digite otro numero menor")
    elif numero < aleatorio:
        print("\t no es el numero, digite un numero mayor")
    else:
        print(f"Felicidades, acabas de adivinar el numero {aleatorio}")
        break
print(f"\nNumero de intentos : {contador}")
