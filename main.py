 # Solucion Numerica de la Ecuacion de la consolidacion
# para las condiciones de contorno permeable/permeable y
# permeable/impermeable
# Metodo de las Diferencias Finitas
# Metodo explicito

#importacion de librerias
import os
import numpy as np

import librerias


# borrado de la pantalla para Mac, Linux y Windows
if os.name == "posix" or os.name=="mac":
    os.system("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system("cls")


# inicio del programa main

u=0
u0=0

# Entrada de datos
longitud=float(input('Espesor del estrato [m]='))

# condiciones iniciales
Ti=float(input('Carga exterior [kPa]='))
T0=0 # condicion de contorno permeable
TL=0  # condicion de contorno permeable

# Parametros del material
c=float(input('Coeficiente de consolidacion [m2/dia] ='))
mv=float(input('Coeficiente de compresibilidad volumetrico [m2/kN] ='))
# calculo del asiento maximo
s_max=longitud*mv*Ti; 
permeabilidad=c*mv*10; # coeficiente de permeabilidad [m/dia]






# comprobacion de la convergencia del metodo
alfa=1
while True:
    # definicion de la malla
    h=float(input('Incremento de x[m]= '))
    k=float(input('Incremento de t[dias]= '))
    alfa=c*k/h**2
    if (alfa>0.5):
        print('El modelo no es convergente alfa>0.5')
        print('alfa = ',alfa)
        print('Reintroduzca los datos de la malla correctamente')
        
    else:
        print('El modelo es convergente alfa<=0.5')
        print('alfa = ',alfa)
        break



while True:
# introducción de las condiciones de contorno
# calculos especificos en funcion de las condiciones de contorno
# Seleccion del tipo de calculo a realizar
    print('Tipos de condiciones de contorno')
    print('[1] Permeable-Permeable')
    print('[2] Permeable-Impermeable')
    print('[3] Impermeable-Permeable')
    tipo_calculo=int(input('Seleccionar el tipo de condiciones de contorno [1],[2],[3] ='))

    if (tipo_calculo==1):
        print('Permeable-Permeable')
        break
    elif(tipo_calculo==2):
        print('Permeable-Impermeabbe')
        break
    elif(tipo_calculo==3):
        print('Impermeable-Permeable')
        break
    else:
        print('Entrada erronea probar de nuevo')

