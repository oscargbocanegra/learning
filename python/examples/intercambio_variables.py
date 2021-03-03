# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
var_a  = input('Ingrese valor numerico A ')
var_b  = input('Ingrese valor numerico B ')

print(f'Valor de A {var_a} Valor de B {var_b}')

aux = var_a
var_a = var_b
var_b = aux

print(f'Cambiando valores en variables A = {var_a} B = {var_b}')