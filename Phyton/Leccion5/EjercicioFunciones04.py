#CALCULADORA DE IMPUESTOS
#calcular el total de un pago incluyendo un impuesto aplicado IVA
#formula = pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

pago_sin_impuesto = int(input('Ingrese el valor del pago'))
impuestto = 21/100
total_a_pagar = pago_sin_impuesto + (pago_sin_impuesto * impuestto)
print(f'El total a pagar es {total_a_pagar}')


def calcularTotalPago (pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal

pagoSinImpuesto = float(input('Digite el pago sin impuesto : '))
impuesto = float(input('Digite el impuesto : ')
pagoConImpuesto = calcularTotalPago(pagoSinImpuesto, impuesto)
print(f'El pago con impuesto es {pagoConImpuesto} ')