def potencia_positiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        resultado = 1
        while exponente > 0:
            resultado *= base
            exponente -=1
        return print(resultado)

potencia_positiva(3,5)