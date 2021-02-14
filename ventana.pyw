# ejemplo de ventanas

from tkinter import *

# definición de la ventana
raiz=Tk()
raiz.title("Ventana de prueba")
raiz.geometry('720x600') # dimensiones de la ventana
raiz.state(newstate = "normal")
raiz.resizable(False,False) # se evita el modificar las dimensiones de la ventana (ancho, alto)




# entrada de los datos de entrada de las condiciones de los parametros del terreno
parametrosTerreno=Frame() # declaramos un frame como contenedor
parametrosTerreno.pack() # empaquetado del frame 
parametrosTerreno.place(x=20,y=175) # posicionamiento del frame
parametrosTerreno.config(width='550',height='120') # dimensiones del frame
parametrosTerreno.config(bd='2.5') # dimensiones del borde
parametrosTerreno.config(cursor='hand2')
parametrosTerreno.config(relief='groove')


lbl_terreno=Label(parametrosTerreno, text="Parámetros del terreno")
lbl_terreno.place(x=20,y=25)
#colocacion de las etiqueta de entrada de datos del terreno,coeficiente de consolidación

lbl_cv=Label(parametrosTerreno, text="Coeficiente de consolidacion ")
lbl_cv.place(x=20,y=25)

#caja de texto de entrada
T_cv=StringVar()
txt_cv = Entry(parametrosTerreno, width=5,textvariable=T_cv)
txt_cv.place(x=350, y=25)
cv = T_cv.get()

#unidades de entrada
lbl_Ucv=Label(parametrosTerreno, text=" [m2/día]")
lbl_Ucv.place(x=400,y=25)



#colocacion de las etiqueta de entrada valor del coeiciente de comprsibilidad volumetrivo

lbl_mv=Label(parametrosTerreno, text="Coeficiente de compresibilidad volumétrica")
lbl_mv.place(x=20,y=50)

#caja de texto de entrada
T_mv=StringVar()
txt_mv = Entry(parametrosTerreno, width=5,textvariable=T_mv)
txt_mv.place(x=350, y=50)
mv = T_mv.get()

#unidades de entrada
lbl_Umv=Label(parametrosTerreno, text=" [m2/kN]")
lbl_Umv.place(x=400,y=50)















# entrada de los datos de entrada de las condiciones de contorno
condicionesContorno=Frame() # declaramos un frame
condicionesContorno.pack() # empaquetado del frame 
#condicionesContorno.config(bg='grey') # color de fondo del frame
condicionesContorno.place(x=20,y=400) # posicionamiento del frame
condicionesContorno.config(width='350',height='120') # dimensiones del frame
condicionesContorno.config(bd='2.5') # dimensiones del borde
condicionesContorno.config(cursor='hand2')
condicionesContorno.config(relief='groove')



# Selección de las condiciones de contorno mediante un radiobutton dentro del Frame
lbl_tipocontorno=Label(condicionesContorno, text="Selección de las condiciones de contorno")
lbl_tipocontorno.place(x=0,y=0)

radioValue = IntVar() 

rdioOne = Radiobutton(condicionesContorno, text='Permeable-Permeable',variable=radioValue, value=1) 
rdioTwo = Radiobutton(condicionesContorno, text='Permeable-Impermeable',variable=radioValue, value=2) 
rdioThree = Radiobutton(condicionesContorno, text='Impermeable-Permeable',variable=radioValue, value=3)

# colocacion de los radiobutton
rdioOne.place(x=20, y=25)
rdioTwo.place(x=20, y=50)
rdioThree.place(x=20, y=75)



raiz.mainloop() # mantenemos la ventana abierta en un bucle 
