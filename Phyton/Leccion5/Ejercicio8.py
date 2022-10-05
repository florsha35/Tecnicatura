#Ejercicio8 - Cajero Automático

saldoInicial = 1000
while True:
    print('\t. :MENU:')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Digite una opcion de menu:'))
    print()
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar ->'))
        saldoInicial += extra
        print(f"Dinero en la cuenta es ${saldoInicial}")
    elif opcion == 2:
        retiro = float(input("Cuánto dinero desea extraer??"))
        if retiro > saldoInicial:
            print("Saldo Insuficiente")
        else:
            saldoInicial -= retiro
            print(f"Su saldo actual es ${saldoInicial}")
    elif opcion == 3:
        print(f"Su saldo disponible es: ${saldoInicial}")
    elif opcion == 4:
        print("Gracias por utilizar nuestro servicio")
        break
    else:
        print("ERROR, digite una opcion valida")
        print()