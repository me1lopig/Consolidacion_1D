import numpy as np
import matplotlib.pyplot as plt

# Parámetros modificados para contornos permeables y tiempo prolongado
L = 10.0  # Longitud del dominio (m)
T = 2.0  # Tiempo total prolongado (s)
c_v = 0.01  # Coeficiente de consolidación (m^2/s)

# Discretización
Nz = 50  # Número de divisiones en z
Nt = 200  # Número de divisiones en t (aumentado para tiempo prolongado)
Delta_z = L / Nz
Delta_t = T / Nt

# Inicialización
u = np.zeros((Nt, Nz))

# Condiciones iniciales y de contorno
u[0, :] = 1.0  # Presión inicial uniforme
u[:, 0] = 0.0  # Presión en z = 0 (permeable)
u[:, -1] = 0.0  # Presión en z = L (permeable)

# Método de diferencias finitas
alpha = c_v * Delta_t / (Delta_z ** 2)

for n in range(0, Nt - 1):
    for i in range(1, Nz - 1):
        u[n + 1, i] = u[n, i] + alpha * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

# Gráfica de la solución
z = np.linspace(0, L, Nz)
t = np.linspace(0, T, Nt)

plt.figure(figsize=(10, 6))

for i in range(0, Nt, Nt // 5):
    plt.plot(z, u[i, :], label=f't = {t[i]:.2f} s')

plt.title('Disipación del Exceso de Presión de Poros (Contornos Permeables)')
plt.xlabel('Profundidad (z)')
plt.ylabel('Presión de Poros (u)')
plt.legend()
plt.grid(True)
plt.show()
