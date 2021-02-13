import tkinter as tk
import tkinter.font as tkFont

#declaracion de la ventana
window = tk.Tk()
window.title("Introducción de los datos")
window.geometry('720x600')
window.state(newstate = "normal")
window.resizable(False,False) # se evita el modificar las dimensiones de la ventana



#colocacion de las etiqueta de entrada de datos de espesor del estrato
# encabezadp
lbl_geometria=tk.Label(window, text="Aproximación de la Ecuación de la Consolidación mediante el método de Diferencias Finitas")
lbl_geometria.place(x=20,y=10)
fuente = tkFont.Font(family="Arial", size=15, weight="bold", slant="italic")
lbl_geometria.configure(font=fuente)


lbl_cartel=tk.Label(window, text="Entrada de datos, para un suelo homogéneo")
lbl_cartel.place(x=20,y=40)
fuente = tkFont.Font( size=14,weight="bold", slant="italic")
lbl_cartel.configure(font=fuente)

lbl_geometria=tk.Label(window, text="Características de cargas y geometría")
lbl_geometria.place(x=20,y=75)


lbl_espesor=tk.Label(window, text="Espesor del estrato")
lbl_espesor.place(x=20,y=100)

#caja de texto de espesor del estrato
espesor=tk.DoubleVar()
txt_espesor = tk.Entry(window, width=5,textvariable=espesor)
txt_espesor.place(x=350, y=100)

#unidades de entrada
lbl_Uespesor=tk.Label(window, text=" [m]")
lbl_Uespesor.place(x=400,y=100)

#colocacion de las etiqueta de entrada de datos de espesor de carga exterior
lbl_carga=tk.Label(window, text="Carga exterior")
lbl_carga.place(x=20,y=125)

#caja de texto de la carga exterior
carga=tk.DoubleVar()
txt_carga = tk.Entry(window, width=5,textvariable=carga)
txt_carga.place(x=350, y=125)

#unidades de entrada
lbl_Ucarga=tk.Label(window, text=" [kPa]")
lbl_Ucarga.place(x=400,y=125)



lbl_terreno=tk.Label(window, text="Parámetros del terreno")
lbl_terreno.place(x=20,y=175)
#colocacion de las etiqueta de entrada de datos del terreno,coeficiente de consolidación

lbl_cv=tk.Label(window, text="Coeficiente de consolidacion ")
lbl_cv.place(x=20,y=200)

#caja de texto de entrada
cv=tk.DoubleVar()
txt_cv = tk.Entry(window, width=5,textvariable=cv)
txt_cv.place(x=350, y=200)

#unidades de entrada
lbl_Ucv=tk.Label(window, text=" [m2/día]")
lbl_Ucv.place(x=400,y=200)



#colocacion de las etiqueta de entrada valor del coeiciente de comprsibilidad volumetrivo

lbl_mv=tk.Label(window, text="Coeficiente de compresinilidad volumétrica")
lbl_mv.place(x=20,y=225)

#caja de texto de entrada
mv=tk.DoubleVar()
txt_mv = tk.Entry(window, width=5,textvariable=mv)
txt_mv.place(x=350, y=225)

#unidades de entrada
lbl_Umv=tk.Label(window, text=" [m2/kN]")
lbl_Umv.place(x=400,y=225)



#caracterización de la malla de cálculo

lbl_x=tk.Label(window, text="Incremento de la malla en x")
lbl_x.place(x=20,y=250)

#caja de texto de entrada
x=tk.DoubleVar()
txt_x = tk.Entry(window, width=5,textvariable=x)
txt_x.place(x=350, y=250)

#unidades de entrada
lbl_Ux=tk.Label(window, text=" [m]")
lbl_Ux.place(x=400,y=250)

# Cálculos intermedios
s_max=espesor*mv*carga  # asiento máximo
permeabilidad=cv*mv*10  # coeficiente de permeabilidad [m/dia]





window.mainloop()
