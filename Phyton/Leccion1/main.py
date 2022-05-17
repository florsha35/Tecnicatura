'''miVariable: int = 3
print(miVariable)
miVariable = "Hello all student of this class"
print(miVariable)
miVariable = 3.
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))



alto = int(input('Ingrese el alto de rectangulo'))
ancho = int(input('Ingrese ancho de rectangulo'))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('area :' , area)
print('perimetro: ', perimetro)


miVariable3 = 10
#operadores de reasignacion
miVariable3 = miVariable3 +1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)


d = 4
b = 7
resultado = d == b # comparamos si son iguales,
print(resultado)   # podemos usar las variables o directamente numeros

#operador diferente
resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

#operador menor que
resultado = d < b
print(resultado)

#operador menor o igual que
resultado = d >= b
print(resultado)


# ejercicio clase 4

a = int(input('Ingrese un numero'))
print(f"El residuo de la division es {a % 2}")
if a % 2 == 0 print(f"El valor de a es: {a} es un numero PAR")
else print(f" El valor de a es: {a} es un numero IMPAR")


#ejercicio2 clase 4
#solicitamos  al a persona que ingrese un edad
edad = 18
edad = int(input("ingrese un numero"))
if edad >= 18:
    print(f'su edad es {edad} :eres mayor de edad')
else:
    print(f'su edad es {edad} :eres menor de edad')


#operadores logicos
a = True
b = True
resultado = a and b
print(resultado)

a = True
b = False
resultado = a or b
print(resultado)

a = True
b = False
resultado = not a
print(resultado)


# Valor dentro de un rango
num = int(input('Ingrese un numero'))
valorMinimo = 0
valorMaximo = 5
dentroRango = (num >=valorMinimo and num <=valorMaximo)
if dentroRango:
    print(f'el valor {num} esta dentro del rango')
else:
    print(f'el valor {num} NO esta dentro del rango'


  # ejercicio cn operador OR

vacaciones = False
dialibre = True
if vacaciones or dialibre:
    print(f'Puede asistir al juego de su hijo')
else:
    print(f'esta ocupado')


#ejercicio rango de edades
edad = int(input('Ingrese su edad'))

#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)
# if veinte or treinta:

if (20 <= edad < 30) or (30 <= edad <= 40):
    print("estas dentro del rango de los (20'0) a (30'0)")
#    if veinte:
#       print(f'su edad {edad} esta dentro de rango de 20')
#    elif treinta:
#       print('estas dentro del rango de 30')
#    else:
#        print(f'no estas dentro del rango')
else:
     print(f'su edad {edad} no esta dentro de rango')


# Ejercicio el mayor de dos numeros
num1= int(input('Digite el valor de num1: '))
num2 = int(input('Digite el valor de num2: '))
if num1 > num2:
    print(f'el numero mayor es: {num1}')
else:
    print(f'el numero mayor es: {num2}')

 # Tienda de libros
print('Ingrese los siguientes datos del libro:')
nombre = input('Digite el nombre del libro:')
ID = int(input('Digite el ID del libro:'))
precio = float(input('Digite el precio del libro: '))
enviogratuito = input('Indique si el envio es gratuito (True/False):' )
if enviogratuito == 'True':
    enviogratuito = True
elif enviogratuito == 'False':
    enviogratuito = False
else:
    enviogratuito = 'El valor es incorrecto, debe escribir True/False'
print (f'''
        "nombre {nombre}
        "ID: {ID}"
        "precio: {precio}
        "envio gratuito: {enviogratuito}
''')

'''