
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tkinter as tk

raiz = tk.Tk()

def hola():
    print ("Hola!")



menubar = tk.Menu(raiz) # Crear el menu principal
raiz.config(menu=menubar) # visualizamos el menú
menubarra=tk.Menu(menubar)
menubarra.add_command(label="Hola", command=hola)
menubarra.add_command(label="Salir", command=raiz.quit)
menubar.add_cascade(label="Colores", menu=menubarra)


# Mostrar la ventana
raiz.mainloop()