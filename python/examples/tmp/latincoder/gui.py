import sys
from Tkinter import *

def hacer_click():
    try:
        _valor = int(entrada_txt.get())
        _valor = _valor * 5
        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Introduce un numero")

app = Tk()
app.title("Mi primera App grafica en Python")

# VP -> ventana principal
vp = Frame(app)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta = Label(vp,text="Escribe Algo:")
etiqueta.grid(column=1,row=1)

boton = Button(vp,text="Clic",command=hacer_click)
boton.grid(column=2,row=2)

valor = ""
entrada_txt = Entry(vp,width=10,textvariable=valor)
entrada_txt.grid(column=3,row=1)
app.mainloop()
