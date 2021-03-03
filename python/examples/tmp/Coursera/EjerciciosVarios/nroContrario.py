def opposite(number):
    if (number < 0):
        opuesto = abs(number)
    else:
        opuesto = number * (-1)
    return print(opuesto)

opposite(15)