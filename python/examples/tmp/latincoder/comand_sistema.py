import subprocess

subprocess.call(['clear'])

def creardirectorios():
    for i in range(0,10):
        nombredir = "dir" + str(i)
        subprocess.call(['mkdir',nombredir])


def borradirecorios():
    for i in range(0,10):
        nombredir = "dir" + str(i)
        subprocess.call(['rm','-r',nombredir])

#borradirecorios()
#creardirectorios()
subprocess.call(['ls','-l'])
