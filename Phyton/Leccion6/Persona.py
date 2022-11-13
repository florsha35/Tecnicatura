class Persona: # creacion de una clase
    def __init__(self, nombre, apellido,dni, edad, *args, **kwargs): #Metodo Init Dunder
        #self.nombre = 'Juan' # en codigo duro
        #self.apellido = 'Zalazar' # cod duro
        #self.edad = 22 #codigo duro
        self.__nombre = nombre #ENCAPSULAMIENTO DEFINITIVO
        self.apellido = apellido
        self._dni = dni #encapsulamiento sugerido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Florencia','Shapasnikoff','31')
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Gianini','45')
print(f' El objeto 2 de la clase persona es {persona2.nombre}, {persona2.apellido}, su edad es {persona2.edad}')
print(f'El objeto 1 de la clase persona es {persona1.nombre}, {persona1.apellido}, su edad es {persona1.edad}')

#modificamos los atributos del objeto
persona1.nombre = 'Liliana'
persona1.apellido = 'Sanchez'
persona1.edad = 40
print(f'El objeto 1  modificado de la clase persona es {persona1.nombre}, {persona1.apellido}, su edad es {persona1.edad}')

#Los atributos son CARACTERISTICAS
#Los metodos son el COMPORTAMIENTO QUE VAN A TENER LOS OBJETOCS (ACCIONES)
persona1.mostrar_detalle()# la referencia se pasa de manera automatica
persona2.mostrar_detalle()

Persona.mostrar_detalle(persona1)# debemos pasarle una referencia para el self o dara error
#codigo no utilizado, si lo vemos hay que modificarlo

persona1.telefono = '260412345'
print(persona1.telefono) #se crea el atributo desde el objeto // persona2 no lo va  apoder usar
print(f' Este es el telefono de {persona1.nombre}  {persona1.telefono}')

persona3 = Persona ('Valentina', 'Reche', 35622356, '31', 'Tel', 2604404368, 'Calle Sarmiento', 2775, 'altura = 1.60', CFavorito = 'negro', Auto ='Jeep', Modelo =2022)
persona3.mostrar_detalle()
print(persona3._dni) #NO SE DEBE USAR FUERA DE LA CLASE SI LO ENCAPSULE