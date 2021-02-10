 # Solucion Numerica de la Ecuacion de la consolidacion
# para las condiciones de contorno permeable/permeable y
# permeable/impermeable
# Metodo de las Diferencias Finitas
# Metodo explicito

#importacion de librerias 
import os
import numpy as np

#librerias propias de creacion de archivos
import archivos
import calculos


# borrado de la pantalla para Mac, Linux y Windows
if os.name == "posix" or os.name=="mac":
    os.system("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system("cls")

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


# creacion del vector espacial inicial
nx=int(longitud/h) # numero de elementos del intervalo
if longitud/h!=nx:
    print('division no entera del intervalo x\n')
else:
    print('division entera del intervalo x \n')

# creacion de los vectores iniciales de presiones y del intervalo espacial
u0=np.ones(nx+1)*Ti #  valores iniciales de presiones
u=np.zeros(nx+1) #  vector de presiones
x=np.arange(0,longitud+h,h) # division de x intervalo espacial


# maximo grado de consolidacion a alcanzar
max_U=input('Maximo grado de consolidacion a calcular [%] =');

# seleccion del tipo de contorno de la capa de arcilla saturada
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
        tipoContorno='Permeable-Permeable'
        calculos.permeable_permeable(u0)
        break
    elif(tipo_calculo==2):
        tipoContorno='Permeable-Impermeable'
        break
    elif(tipo_calculo==3):
        tipoContorno='Impermeable-Permeable'
        break
    else:
        print('Entrada erronea probar de nuevo')
    

#creamos el archivo de los datos de entrada del modelo
archivos.archivo_datos(longitud,Ti,c,mv,permeabilidad,h,k,alfa,tipoContorno);