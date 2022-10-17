#Agenda Telefónica
#HAcer un programa simule una agenda telefónica
#clave sera el nombre y el valor el numero de telef. con un menu de 4 opciones


agenda = {}
while True:
    print('\t___MENU___')
    print('1. Nuevo Contacto')
    print('2.Borrar Contacto')
    print('3.Ver contactos existentes')
    print('4.Salir')
    opcion = int(input('Digite una opcion: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto')
        telefono = input('Digite el numero de telefono')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agendado correctamente')
        else:
            print('Contacto ya existente')
    elif opcion == 2:
        nombre = input('Digite el contacto que desea borrar')
        if nombre in agenda:
            del (agenda[nombre])
            print(f'El contacto{nombre} ha sido borrado exitosamente')
        else:
            print('El contacto ingresa no existe')
    elif opcion == 3:
        print ('Agenda de contactos')
        for clave,valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono : {valor}')
    elif opcion == 4:
        print('Gracias por utilizar la agenda de contactos')
        break
    else:
        print('La opcion ingresada no es válida')
    print()