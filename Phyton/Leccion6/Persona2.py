class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son: {self._nombre} {self._apellido} {self._edad}')

    @property #decorador
    def nombre(self):  #    metodo GETTER
        print('Estamos utilizando el metodo get')
        return self._nombre

    @property  # decorador
    def apellido(self):  # metodo GETTER
        print('Estamos utilizando el metodo get')
        return self._apellido

    @property  # decorador
    def edad(self):  # metodo GETTER
        print('Estamos utilizando el metodo get')
        return self._edad



    @nombre.setter
    def nombre(self, nombre):  #metodo SETTER
        print('Estamos utilizando el metodo setter')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):  # metodo SETTER
        print('Estamos utilizando el metodo setter')
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):  # metodo SETTER
        print('Estamos utilizando el metodo setter')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido}  {self._edad}')

if __name__ == '__main__':

    persona1 = Persona2('Florencia', 'Shapasnikoff', 31)
    print(persona1.nombre) #llamamos al metodo getter

    persona1.nombre = 'Juan Pedro' #llamamos al metodo setter
    print(persona1.nombre) #metodo getter
    print(persona1.mostrar_detalles()) #metodo mostrar_detalles

    print(persona1.edad) #Atributo READ-ONLY, solo lectura porq no tiene metodo setter

    persona2 = Persona2('Federico', 'Suter', 46)
    print(persona2.nombre, persona2.apellido, persona2.edad)

    # persona3 = Persona2('Valentina', 'Reche', 31)
    # print(persona3.nombre, persona3.apellido, persona3.edad)
    persona3 = Persona2('Valentina','Rechs', 33)
    print(persona3.nombre) #get
    print(persona3.apellido) #get
    persona3.nombre = 'Valentina' #set
    persona3.apellido = 'Reche' #modificamos (setter)
    persona3.edad = 31 #modificamos (setter)

    print(persona3.mostrar_detalles())