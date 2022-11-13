#Convertidor de temperaturas
# crear dos funciones para convertir grado celsius a Farenheit y viceversa

def GradosCelaFar (celsius):
    return celsius * 9 / 5 + 32


def GradosFaraCel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Digite el valor de celsius'))
resultado = GradosCelaFar(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')




fahrenheit = float(input('Digite el valor de Farenheit'))
resultado1 = GradosFaraCel(fahrenheit)
print(f'{fahrenheit} F a C ->{resultado1:.2f}')
