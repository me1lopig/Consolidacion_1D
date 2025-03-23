import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def genera_archivo(longitud, Ti, c, mv, s_max, h, k, permeabilidad):
    format_out = '%d_%m_%y_%H_%M_%S_'
    fecha = datetime.now().strftime(format_out)

    nombre_archivo1 = f'datos_{fecha}.txt'
    nombre_archivo2 = f'presiones_{fecha}.txt'
    nombre_archivo3 = f'asientos_{fecha}.txt'
    nombre_archivo4 = f'caudales_{fecha}.txt'

    with open(nombre_archivo1, 'a') as x1:
        x1.write('Datos del modelo\n')
        x1.write(f'Espesor del estrato {longitud:.2f} m\n')
        x1.write(f'Valor de la carga exterior {Ti:.2f} kPa\n')
        x1.write(f'Coeficiente de consolidacion {c:.5f} m2/dia\n')
        x1.write(f'Coeficiente de compresibilidad volumetrico {mv:.5E} m2/kN\n')
        x1.write(f'Coeficiente de deformacion edometrico {1/mv:.3f} kN/m2\n')
        x1.write(f'Coeficiente de permeabilidad {permeabilidad:.5E} m/dia\n')
        x1.write('Datos del mallado\n')
        x1.write(f'Incremento de x[m]= {h:.2f}\n')
        x1.write(f'Incremento de t[dias]= {k:.2f}\n')
        x1.write('Resultado de los calculos\n')
        x1.write(f'Asiento maximo esperado [cm]= {s_max * 100:.2f}\n\n')

    with open(nombre_archivo2, 'a') as x2:
        pass

    with open(nombre_archivo3, 'a') as x3:
        x3.write('[dias]\tU\tS [cm]\n')

    with open(nombre_archivo4, 'a') as x4:
        x4.write('[dias]\tQ [m3/dia/m2]\n')

    return nombre_archivo2, nombre_archivo3, nombre_archivo4

def caudal(u0, h, permeabilidad, t, x4):
    derivada = u0[1] / h
    Q = permeabilidad * derivada

    with open(x4, 'a') as file:
        file.write(f'{t:.2f}  {Q:.5e}\n')

def doble_drenaje(T0, Ti, TL, alfa, u0, max_U, longitud, s_max, k, x2, x3, x4):
    nx = len(u0) - 1
    u = u0.copy()
    u[0] = (T0 + Ti) / 2
    u[-1] = (TL + Ti) / 2

    for i in range(1, nx):
        u[i] = alfa * (u0[i + 1] + u0[i - 1] - 2 * u0[i]) + u0[i]

    u[0] = T0
    u[-1] = TL

    grado_consolidacion = 0
    t = k

    while grado_consolidacion <= max_U / 100:
        t += k
        for i in range(1, nx):
            u[i] = alfa * (u0[i + 1] + u0[i - 1]) + (1 - 2 * alfa) * u0[i]

        representaPresiones(x, u, t, x2)
        u0 = u.copy()
        u_maxima = max(u0)
        Hf = longitud
        caudal(u0, h, permeabilidad, t, x4)
        U(x, u0, longitud, Ti, s_max, t, x3)
        files(t, x, u0, x2)

def files(t, x, u0, x2):
    with open(x2, 'a') as file:
        file.write(f'{t:.3f}\t\n')
        file.write('m\t\tkPa\n')
        for j in range(len(x)):
            file.write(f'{x[j]:.2f}  {u0[j]:.5f}\n')

def U(x, u0, longitud, Ti, s_max, t, x3):
    uajuste = np.polyfit(x, u0, 2)
    sumasimpson = 0
    for ix in range(len(x) - 1):
        sumasimpson += ((x[ix + 1] - x[ix]) / 6) * (u0[ix + 1] + u0[ix] +
                        4 * np.polyval(uajuste, (x[ix + 1] + x[ix]) * 0.5))

    area_total = longitud * Ti
    grado_consolidacion = (area_total - sumasimpson) / area_total
    asiento = s_max * grado_consolidacion

    with open(x3, 'a') as file:
        file.write(f'{t:.2f}  {grado_consolidacion:.5f}  {asiento * 100:.2f}\n')

def representaPresiones(x, u, t, x2):
    plt.figure()
    plt.plot(x, u, label=f't = {t:.2f} días')
    plt.xlabel('Profundidad (m)')
    plt.ylabel('Presión (kPa)')
    plt.title('Disipación de Presiones')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'presiones_t_{t:.2f}.png')
    plt.close()

# Programa principal
longitud = float(input('Espesor del estrato [m] = '))
Ti = float(input('Carga exterior [kPa] = '))
T0 = 0
TL = 0

c = float(input('Coeficiente de consolidación [m2/día] = '))
mv = float(input('Coeficiente de compresibilidad volumétrico [m2/kN] = '))

s_max = longitud * mv * Ti
permeabilidad = c * mv * 10

h = float(input('Incremento de x [m] = '))
k = float(input('Incremento de t [días] = '))

alfa = c * k / h**2
if alfa > 0.5:
    print('El modelo no es convergente alfa > 0.5')
    exit()

print(f'alfa = {alfa:.3f}')

x2, x3, x4 = genera_archivo(longitud, Ti, c, mv, s_max, h, k, permeabilidad)

nx = int(np.floor(longitud / h))
if longitud / h != nx:
    print('División no entera del intervalo x')
else:
    print('División entera del intervalo x')

u0 = np.ones(nx + 1) * Ti
x = np.arange(0, longitud + h, h)

max_U = float(input('Máximo grado de consolidación a calcular [%] = '))

doble_drenaje(T0, Ti, TL, alfa, u0, max_U, longitud, s_max, k, x2, x3, x4)

def representa_1():
    print("Obteniendo gráficas de los asientos en función del tiempo y de la consolidación")

representa_1()

print("Cerrando archivos abiertos y terminando el programa")
