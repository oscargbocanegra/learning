# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

valor_compra = int(input('Ingrese el valor de la compra : '))
porcentaje_descuento = int(input('Ingrese el porcentaje de descuento : '))

descuento = (valor_compra * porcentaje_descuento)/100
total_factura = valor_compra - descuento

print('El valor de su compra es :' + str(valor_compra) + ' Menos el descuento de ' +str(porcentaje_descuento) + ' Total a pagar ' + str(total_factura ))