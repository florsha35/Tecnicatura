#Ejercicio Frase sin espacio y contar caracteres
frase = input("Digite una frase")
frase1 = ""
for i in frase:
    if i != " ":
        frase1 += i
frase = frase1
print(f'\n Frase final: {frase}')
print(f'0\n Numer   '
      f'o de caracteres: {len(frase)}')