# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza 
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo = int(input('Ingrese el valor de su sueldo : '))
venta_1 = int(input('Ingrese el valor de la Venta 1: '))
venta_2 = int(input('Ingrese el valor de la Venta 2: '))
venta_3 = int(input('Ingrese el valor de la Venta 3: '))

comision = (venta_1 + venta_2 + venta_3) * .10

total = sueldo + comision

print ('El valor toral a pagar es de :' + str(total) + ' Discriminado asi: Sueldo ' +str(sueldo)+ ' Mas comision ' + str(comision))