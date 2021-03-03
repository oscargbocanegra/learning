import random
import datetime
import sys
import time

"""
valor = random.randint(0,10)

lista = [True, "Strings", 23, False]
print(lista)
random.shuffle(lista)
print(lista)
"""

print(datetime.datetime.now())

for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d" % i)
	sys.stdout.flush()
	#sys.stdout.write("Texto")
	