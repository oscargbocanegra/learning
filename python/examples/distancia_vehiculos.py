# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y 
# con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia_v1 = int(input('Ingrese velocidad de coche 1 (km/h): '))
distancia_v2 = int(input('Ingrese velocidad de coche 2 (km/h): '))
distancia_coches = int(input('Ingrese la distancia de los coches: '))

tiempo = distancia_coches / (distancia_v1 - distancia_v2)
tiempo = tiempo * 60

print(f'El tiempo que tardara en alcanzarlo es de : {tiempo} Minutos' )



