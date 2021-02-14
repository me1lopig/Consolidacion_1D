

import tkinter as tk
import tkinter.font as tkFont


def imprimir (valor):
    print('El valor es ',valor)


print('hola mundo')


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
lbl_geometria.pack()
lbl_geometria.config(font=('Arial', 17)) #Cambiar tipo y tamaño de fuente
lbl_geometria.config(fg="black") #Cambiar color del texto



lbl_cartel=tk.Label(window, text="Entrada de datos, para un suelo homogéneo")
lbl_cartel.place(x=20,y=40)
lbl_cartel.pack()
lbl_cartel.config(font=('Arial', 15)) #Cambiar tipo y tamaño de fuente
lbl_cartel.config(fg="black") #Cambiar color del texto


lbl_geometria=tk.Label(window, text="Características de cargas y geometría")
lbl_geometria.place(x=20,y=75)


lbl_espesor=tk.Label(window, text="Espesor del estrato")
lbl_espesor.place(x=20,y=100)

#caja de texto de espesor del estrato

T_espesor=tk.StringVar()
txt_espesor = tk.Entry(window, width=5,textvariable=T_espesor)
txt_espesor.place(x=350, y=100)
espesor = T_espesor.get()



#unidades de entrada
lbl_Uespesor=tk.Label(window, text=" [m]")
lbl_Uespesor.place(x=400,y=100)

#colocacion de las etiqueta de entrada de datos de espesor de carga exterior
lbl_carga=tk.Label(window, text="Carga exterior")
lbl_carga.place(x=20,y=125)

#caja de texto de la carga exterior
T_carga=tk.StringVar()
txt_carga = tk.Entry(window, width=5,textvariable=T_carga)
txt_carga.place(x=350, y=125)
carga = T_carga.get()

#unidades de entrada
lbl_Ucarga=tk.Label(window, text=" [kPa]")
lbl_Ucarga.place(x=400,y=125)


lbl_terreno=tk.Label(window, text="Parámetros del terreno")
lbl_terreno.place(x=20,y=175)
#colocacion de las etiqueta de entrada de datos del terreno,coeficiente de consolidación

lbl_cv=tk.Label(window, text="Coeficiente de consolidacion ")
lbl_cv.place(x=20,y=200)

#caja de texto de entrada
T_cv=tk.StringVar()
txt_cv = tk.Entry(window, width=5,textvariable=T_cv)
txt_cv.place(x=350, y=200)
cv = T_cv.get()

#unidades de entrada
lbl_Ucv=tk.Label(window, text=" [m2/día]")
lbl_Ucv.place(x=400,y=200)



#colocacion de las etiqueta de entrada valor del coeiciente de comprsibilidad volumetrivo

lbl_mv=tk.Label(window, text="Coeficiente de compresibilidad volumétrica")
lbl_mv.place(x=20,y=225)

#caja de texto de entrada
T_mv=tk.StringVar()
txt_mv = tk.Entry(window, width=5,textvariable=T_mv)
txt_mv.place(x=350, y=225)
mv = T_mv.get()

#unidades de entrada
lbl_Umv=tk.Label(window, text=" [m2/kN]")
lbl_Umv.place(x=400,y=225)


#caracterización de la malla de cálculo
lbl_geometria_malla=tk.Label(window, text="Datos del mallado del modelo")
lbl_geometria_malla.place(x=20,y=275)

# Datos de la malla en x

lbl_x=tk.Label(window, text="Incremento de la malla en x")
lbl_x.place(x=20,y=300)

#caja de texto de entrada de los valores del espaciado en x
T_x=tk.StringVar()
txt_x = tk.Entry(window, width=5,textvariable=T_x)
txt_x.place(x=350, y=300)
x = T_x.get()

#unidades de entrada
lbl_Ux=tk.Label(window, text=" [m]")
lbl_Ux.place(x=400,y=300)



# Datos de la malla en t

lbl_t=tk.Label(window, text="Incremento de la malla en t")
lbl_t.place(x=20,y=325)

#caja de texto de entrada de los valores del espaciado en t
T_t=tk.StringVar()
txt_t = tk.Entry(window, width=5,textvariable=T_t)
txt_t.place(x=350, y=325)
x = T_t.get()

#unidades de entrada
lbl_Ut=tk.Label(window, text=" [días]")
lbl_Ut.place(x=400,y=325)


# comprobación de la convergencia del modelo
lbl_convergencia=tk.Label(window, text="Convergencia del modelo")
lbl_convergencia.place(x=20,y=350)

lbl_Cconvergencia=tk.Label(window, text='El valor del coeficiente es ')
lbl_Cconvergencia.place(x=350,y=350)

lbl_Cconvergencia=tk.Label(window, text="El modelo es convergente")
lbl_Cconvergencia.place(x=475,y=350)





# Selección de las condiciones de contorno mediante un radiobutton
lbl_tipocontorno=tk.Label(window, text="Selección de las condiciones de contorno")
lbl_tipocontorno.place(x=20,y=400)

radioValue = tk.IntVar() 

rdioOne = tk.Radiobutton(window, text='Permeable-Permeable',variable=radioValue, value=1) 
rdioTwo = tk.Radiobutton(window, text='Permeable-Impermeable',variable=radioValue, value=2) 
rdioThree = tk.Radiobutton(window, text='Impermeable-Permeable',variable=radioValue, value=3)

# colocacion de los radiobutton
rdioOne.place(x=20, y=425)
rdioTwo.place(x=20, y=450)
rdioThree.place(x=20, y=475)




window.mainloop()
