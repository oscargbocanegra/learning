from sys import argv
import subprocess

script = argv
name = str(script[0])
print name

def creardirectorios():
    for i in range(0,10):
        directorio = "dir" + str(i)
        subprocess.call(['mkdir',directorio])
        subprocess.call(['cp',name,directorio])


def borradirecorios():
    for i in range(0,10):
        directorio = "dir" + str(i)
        subprocess.call(['rm','-r',directorio])

borradirecorios()
subprocess.call('clear')
#creardirectorios()
#subprocess.call(['ls','-l'])
