import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
Lx = 10.0          # Longitud en la dirección x (m)
Lz = 10.0          # Longitud en la dirección z (m)
cvx = 1.0          # Coeficiente de consolidación en x (m^2/año)
cvz = 1.0          # Coeficiente de consolidación en z (m^2/año)
Nx = 50            # Número de puntos en la dirección x (mallado más fino)
Nz = 50            # Número de puntos en la dirección z (mallado más fino)
dx = Lx / (Nx - 1) # Tamaño del paso en x
dz = Lz / (Nz - 1) # Tamaño del paso en z
dt = 0.01          # Paso de tiempo inicial (años)

# Condición inicial: presión de poro uniforme
u0 = 100.0  # Presión de poro inicial (kPa)

# Inicialización de la presión de poro
u = np.ones((Nx, Nz)) * u0  # Matriz de presión de poro en cada punto (x, z)
u_new = np.copy(u)          # Matriz para almacenar la solución en el siguiente paso de tiempo

# Condiciones de contorno
u[:, 0] = 0.0  # Contorno superior (drenaje libre)
u[:, -1] = 0.0 # Contorno inferior (drenaje libre)
u[0, :] = 0.0  # Contorno izquierdo (drenaje libre)
u[-1, :] = 0.0 # Contorno derecho (drenaje libre)

# Factores de estabilidad
alphax = cvx * dt / (dx ** 2)
alphaz = cvz * dt / (dz ** 2)
print(f"Factores de estabilidad iniciales: alpha_x = {alphax}, alpha_z = {alphaz}")

# Ajustar el paso de tiempo para garantizar estabilidad
if alphax + alphaz > 0.5:
    dt = 0.5 * min((dx ** 2) / cvx, (dz ** 2) / cvz)  # Nuevo paso de tiempo
    print(f"Se ajustó el paso de tiempo a dt = {dt} para garantizar estabilidad.")
    alphax = cvx * dt / (dx ** 2)
    alphaz = cvz * dt / (dz ** 2)
    print(f"Nuevos factores de estabilidad: alpha_x = {alphax}, alpha_z = {alphaz}")

# Número de pasos de tiempo
Nt = 400  # Número total de pasos de tiempo

# Solución numérica
for n in range(Nt):
    for i in range(1, Nx - 1):
        for j in range(1, Nz - 1):
            u_new[i, j] = u[i, j] + alphax * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) + alphaz * (u[i, j+1] - 2*u[i, j] + u[i, j-1])
    
    # Aplicar condiciones de contorno en cada paso de tiempo
    u_new[:, 0] = 0.0  # Contorno superior
    u_new[:, -1] = 0.0 # Contorno inferior
    u_new[0, :] = 0.0  # Contorno izquierdo
    u_new[-1, :] = 0.0 # Contorno derecho

    # Actualizar la solución
    u = np.copy(u_new)

    # Graficar la solución en ciertos pasos de tiempo
    if n % 40 == 0:
        plt.figure()
        plt.imshow(u, extent=[0, Lx, 0, Lz], origin="lower", cmap="viridis", vmin=0, vmax=u0)
        plt.colorbar(label="Presión de poro (kPa)")
        plt.xlabel("x (m)")
        plt.ylabel("z (m)")
        plt.title(f"Consolidación bidimensional (t = {n * dt:.2f} años)")
        plt.show()