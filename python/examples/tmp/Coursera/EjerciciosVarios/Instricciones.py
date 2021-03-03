llueve = True
temperatura = int(input('Ingresa temperatura'))
if temperatura < 18:
    if llueve == True:
        print('Llevare paraguas y abrigo')
    else:
        print('Solo llevare abrigo')
else:
    print('No necesito praguas ni abrigo')