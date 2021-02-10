# Funciones de cálculo para los distintos contornos definidos

def permeable_permeable(u0,u,carga,nx,alfa):

# calculo en el caso de que exista condiciones de drenaje
# en los dos contornos 
# suavizado de las condiciones de contorno para el primer calculo
# permeable-permeable

    T0=0 # condicion de contorno permeable
    TL=0 # condicion de contorno permeable


# esquema en diferencias finitas explicitas
# calculo de la primera columna
    u0[0]=(T0+carga)/2
    u0[nx]=(TL+carga)/2

    for i in range(1,nx):
        u[i]=alfa*(u0[i+1]+u0[i-1]-2*u0[i])+u0[i]


  
u=[0,0,0,0,0,0,0]
u0=[120,120,120,120,120,]


