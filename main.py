# Solucion Numerica de la Ecuacion de la consolidacion
# para las condiciones de contorno permeable/permeable y
# permeable/impermeable
# Metodo de las Diferencias Finitas
# Metodo explicito
# con este programa se obtienen tres archivos de salida para su analisis
# y cuatro capturas de resultados graficos

u=0
u0=0
# borrado del archivo
#limpiamos las variables
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
# definicion de la malla
h=float(input('Incremento de x[m]= '))
k=float(input('Incremento de t[dias]= '))
#tiempo_max=input('Tiempo maximo[Dias]  = ');
# comprobacion de la convergencia del metodo