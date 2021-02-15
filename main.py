# ejemplo de ventanas

from tkinter import *

def sumar():
    # funcion de prueba
    print('Holi')



# definición de la ventana
raiz=Tk()
raiz.title("Aproximación de la Ecuación de la Consolidación mediante el método de Diferencias Finitas")
raiz.geometry('720x550') # dimensiones de la ventana
raiz.state(newstate = "normal")
raiz.resizable(False,False) # se evita el modificar las dimensiones de la ventana (ancho, alto)


#colocacion de las etiqueta de entrada de datos de espesor del estrato

lbl_cartel=Label(raiz, text="Introducción de los datos para los cálculos")
lbl_cartel.place(x=20,y=60)
lbl_cartel.pack()
lbl_cartel.config(font=('Arial', 15)) #Cambiar tipo y tamaño de fuente
lbl_cartel.config(fg="black") #Cambiar color del texto



# entrada de los datos de las condiciones de los parametros del terreno
cargasGeometria=Frame() # declaramos un frame como contenedor
cargasGeometria.pack() # empaquetado del frame 
cargasGeometria.place(x=20,y=75) # posicionamiento del frame
cargasGeometria.config(width='550',height='90') # dimensiones del frame
cargasGeometria.config(bd='2.5') # dimensiones del borde
cargasGeometria.config(cursor='hand2')
cargasGeometria.config(relief='groove')



lbl_geometria=Label(cargasGeometria, text="Características de cargas y geometría")
lbl_geometria.grid(row=0,column=0,sticky='w',pady=5)


lbl_espesor=Label(cargasGeometria, text="Espesor del estrato")
lbl_espesor.grid(row=1,column=0,sticky='w')

#caja de texto de espesor del estrato

T_espesor=StringVar()
txt_espesor = Entry(cargasGeometria, width=5,textvariable=T_espesor)
#txt_espesor.pack()
txt_espesor.grid(row=1,column=1,sticky='w')
espesor = T_espesor.get()


#unidades de entrada
lbl_Uespesor=Label(cargasGeometria, text=" [m]")
lbl_Uespesor.grid(row=1,column=2,sticky='w')

#colocacion de las etiqueta de entrada de datos de espesor de carga exterior
lbl_carga=Label(cargasGeometria, text="Carga exterior")
lbl_carga.grid(row=2,column=0,sticky='w')

#caja de texto de la carga exterior
T_carga=StringVar()
txt_carga = Entry(cargasGeometria, width=5,textvariable=T_carga.get())
#txt_carga.pack()
txt_carga.grid(row=2,column=1,sticky='w',pady=5)
#carga = T_carga.get()

#unidades de entrada
lbl_Ucarga=Label(cargasGeometria, text=" [kPa]")
lbl_Ucarga.grid(row=2,column=2,sticky='w')






# entrada de los datos de las condiciones de los parametros del terreno
parametrosTerreno=Frame() # declaramos un frame como contenedor
parametrosTerreno.pack() # empaquetado del frame 
parametrosTerreno.place(x=20,y=175) # posicionamiento del frame
parametrosTerreno.config(width='550',height='95') # dimensiones del frame
parametrosTerreno.config(bd='2.5') # dimensiones del borde
parametrosTerreno.config(cursor='hand2')
parametrosTerreno.config(relief='groove')


lbl_terreno=Label(parametrosTerreno, text="Parámetros del terreno")
lbl_terreno.place(x=20,y=0)
#colocacion de las etiqueta de entrada de datos del terreno,coeficiente de consolidación

lbl_cv=Label(parametrosTerreno, text="Coeficiente de consolidacion ")
lbl_cv.place(x=20,y=25)

#caja de texto de entrada
T_cv=StringVar()
txt_cv = Entry(parametrosTerreno, width=5,textvariable=T_cv)
#txt_cv.pack()
txt_cv.place(x=350, y=25)
cv = T_cv.get()

#unidades de entrada
lbl_Ucv=Label(parametrosTerreno, text=" [m2/día]")
lbl_Ucv.place(x=400,y=25)



#colocacion de las etiqueta de entrada valor del coeficiente de comprsibilidad volumetrivo

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
datosMallado=Frame() # declaramos un frame
datosMallado.pack() # empaquetado del frame 
datosMallado.place(x=20,y=275) # posicionamiento del frame
datosMallado.config(width='550',height='120') # dimensiones del frame
datosMallado.config(bd='2.5') # dimensiones del borde
datosMallado.config(cursor='hand2')
datosMallado.config(relief='groove')


#caracterización de la malla de cálculo
lbl_geometria_malla=Label(datosMallado, text="Datos del mallado del modelo")
lbl_geometria_malla.place(x=20,y=0)

# Datos de la malla en x

lbl_x=Label(datosMallado, text="Incremento de la malla en x")
lbl_x.place(x=20,y=25)

#caja de texto de entrada de los valores del espaciado en x
T_x=StringVar()
txt_x = Entry(datosMallado, width=5,textvariable=T_x)
#txt_x.pack()
txt_x.place(x=350, y=25)
x = T_x.get()

#unidades de entrada
lbl_Ux=Label(datosMallado, text=" [m]")
lbl_Ux.place(x=400,y=25)



# Datos de la malla en t

lbl_t=Label(datosMallado, text="Incremento de la malla en t")
lbl_t.place(x=20,y=50)

#caja de texto de entrada de los valores del espaciado en t
T_t=StringVar()
txt_t = Entry(datosMallado, width=5,textvariable=T_t)
#txt_t.pack()
txt_t.place(x=350, y=50)
x = T_t.get()

#unidades de entrada
lbl_Ut=Label(datosMallado, text=" [días]")
lbl_Ut.place(x=400,y=50)



# entrada de los datos de entrada de las condiciones de contorno
condicionesContorno=Frame() # declaramos un frame
condicionesContorno.pack() # empaquetado del frame 
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
rdioOne.select
# colocacion de los radiobutton
rdioOne.place(x=20, y=25)
rdioTwo.place(x=20, y=50)
rdioThree.place(x=20, y=75)


# Colocación del Frame para colocar los botones de ejecucion

# Frame de la entrada de los botones
botones=Frame() # declaramos un frame
botones.pack() # empaquetado del frame 
botones.place(x=400,y=400) # posicionamiento del frame
botones.config(width='170',height='120') # dimensiones del frame
botones.config(bd='2.5') # dimensiones del borde
botones.config(cursor='hand2')
botones.config(relief='groove')

#definición de los botones

boton_ejecuta=Button(botones, text="Calcular", command=sumar)
boton_ejecuta.grid(row=0,column=0,pady=10,padx=10)
boton_ejecuta.config(width='8',height='2') # dimensiones del boton

#cerramos la aplicación
boton_salir=Button(botones, text="Salir", command=raiz.destroy)
boton_salir.grid(row=0,column=1,pady=10,padx=10)
boton_salir.config(width='8',height='2') # dimensiones del boton


raiz.mainloop() # mantenemos la ventana abierta en un bucle 
