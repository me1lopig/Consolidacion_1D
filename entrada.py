import tkinter as tk

#declaracion de la ventana
window = tk.Tk()
window.title("Introducción de los datos")
window.geometry('720x600')
window.state(newstate = "normal")
window.resizable(False,False)



#colocacion de las etiqueta de entrada de datos de espesor del estrato

lbl_espesor=tk.Label(window, text="Espesor del estrato")
lbl_espesor.place(x=20,y=25)

lbl_Uespesor=tk.Label(window, text=" [m]")
lbl_Uespesor.place(x=220,y=25)

#caja de text
espesor = tk.Entry(window, width=5)
espesor.place(x=160, y=25)



#colocacion de las etiqueta de entrada de datos de espesor de carga exterior

lbl_carga=tk.Label(window, text="Carga exterior")
lbl_carga.place(x=20,y=50)


lbl_Ucarga=tk.Label(window, text=" [kPa]")
lbl_Ucarga.place(x=220,y=50)

#caja de texto
carga = tk.Entry(window, width=5)
carga.place(x=160, y=50)










window.mainloop()
