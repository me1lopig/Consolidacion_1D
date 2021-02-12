# ajuste a una funcion desde una lista de puntos
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])
pol = np.polyfit(x,y,len(x)-1)  # coeficientes del polinomio

xx = np.linspace(min(x),max(x))
yy = np.polyval(pol,xx)         # valor del polinomio en los puntos de la matriz xx

plt.plot(xx, yy, '-',x, y, 'ro')
#plt.axis([min(xx)-d, max(xx)+d, min(yy)-d, max(yy)+d])