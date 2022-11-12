# ******* FUNCIONES ****

#dEFINIMOS UNA FUNCION
# def mi_funcion():
#     print('Saludos a todos')
#
# mi_funcion() #Llamo a la funcion, primero debo definirla
# mi_funcion()
# mi_funcion()

# LIST UNPACKING - desempaquetar listas
# def show(name, lastName):
#     print(name+ '  '+lastName)
#     person = ["Florencia", "Ailín"]
#     show(person[0], person[1])#indicamos de a 1 para q muestre
#     show(*person)# igual q lo anterior pero indico solo la variable
#
#     person2 = ("Federico", "Germán") # desempaquetamos a traves de TUPLAS
#     show(*person2)
#
#     person3 = {"lastName": "Lucero", "name": "Natalia"}
#     show(**person3)# pongo dos** para q muestre dos elementos

#repaso for/else
# numbers = [1,2,3,4,5]# incluso con la lista vacia ejecuta el ELSE
# for n in numbers:
#     print(n)
#     if n == 3:
#         break # usando breaj unica forma q no ejecute el ELSE
# else:
#     print('Esto se terminó')

#Lista de comprension
# names = ["Paolo, "Rodrigo", "Lupe", "Pepe"]
# alongP =[p for p in names if p[0] == 'P']
# print(alongP)
#
# bottleC = [{"name": "Quilmes","country": "Arg"},
#            {"name": "Corona","country": "Mx"},
#            {"name": "Stella Artois","country": "Belgica"}]
# Arg = [b for b in bottleC b["country"] =="Arg"]
# print(Arg)
# print(bottleC)

#ARGUMENTOS
# def mi_funcion2(name,lastName):
#     print("Saludos a los que me ven a traves del canal de YouTuBe")
#     print(f'Nombre: {name}, Apellido: {lastName}')
# mi_funcion2('Florencia', 'Shapasnikoff')
# mi_funcion2('Federico', 'Suter')
# mi_funcion2('Gaston', 'Suter')

#RETURN
#creamos una funcion para sumer
def sumar(a,b):
    return a + b
# resultado = sumas (15,35)
#print(f'El resultado de la suma es: {resultado}')
#print(f'El resultado de la suma es: {sumar(35,15)}')

#valores por defecto
# def sumar2(a = 0, b = 0):
#     return a + b
# resultado = sumar2()
# print(f'El resultado de la suma es: {resultado}')
# print(f'El resultado de la suma es: {sumar2(35,15)}')


#argumentos, variables en funciones
# def listarNombres(*nombres):
#     for nombre in nombres:
#         print(nombre)
# listarNombres('Lucas','Martin','Juan','Pablo','Rucardo')
# listarNombres('Florencia','Juana', 'Lucia')
#
# def listarTerminos(**terminos): #lo mas usado en **kwargs
#     for llave, valor in terminos.items():
#         print(f'{llave} : {valor}')
#
# listarTerminos() #si esta vacio no muestra nada
# listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primary Key')

#DATOS COMO ARGUMENTOS - usando lista

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
# para poder utilizar numero debo convertirlo a tupla()
desplegarNombres((10,11))
desplegarNombres([10,11]) # convertido a lista


#FUNCIONES RECURSIVAS
#determinar el factorial de un numero
def factorial(numero):
    if numero == 1:  #caso base
        return 1
    else:
        return numero * factorial(numero-1) # caso recursivo
numeroFactorial = int(input('Digite un numero para calcular el factorial: '))
resultado = factorial(numeroFactorial) #en cod. duro
print(f' El factorial del numero {numeroFactorial} es: {resultado}')