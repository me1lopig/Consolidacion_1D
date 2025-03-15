import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
H = 10.0          # Espesor del estrato de suelo (m)
cv = 1.0           # Coeficiente de consolidación (m^2/año)
Nz = 20            # Número de puntos en la discretización espacial
Nt = 200           # Número de pasos de tiempo
dz = H / (Nz - 1)  # Tamaño del paso espacial
dt = 0.01          # Tamaño del paso temporal (años)

# Condición inicial: presión de poro uniforme
u0 = 100.0  # Presión de poro inicial (kPa)

# Inicialización de la presión de poro
u = np.ones(Nz) * u0  # Vector de presión de poro en cada punto z
u_new = np.copy(u)    # Vector para almacenar la solución en el siguiente paso de tiempo

# Condiciones de contorno
u[0] = 0.0  # Contorno superior (drenaje libre)
# Contorno inferior: flujo nulo (derivada espacial igual a cero)

# Factor de estabilidad
alpha = cv * dt / (dz ** 2)
print(f"Factor de estabilidad (alpha): {alpha}")

# Verificación de la condición de estabilidad
if alpha > 0.5:
    print("¡Advertencia! El paso de tiempo no cumple la condición de estabilidad.")

# Solución numérica
for n in range(Nt):
    for i in range(1, Nz - 1):
        u_new[i] = u[i] + alpha * (u[i+1] - 2*u[i] + u[i-1])
    
    # Aplicar condición de contorno inferior (flujo nulo)
    u_new[-1] = u_new[-2]

    # Actualizar la solución
    u = np.copy(u_new)

    # Aplicar condición de contorno superior en cada paso de tiempo
    u[0] = 0.0

    # Graficar la solución en ciertos pasos de tiempo
    if n % 40 == 0:
        plt.plot(np.linspace(0, H, Nz), u, label=f"t = {n * dt:.2f} años")

# Configuración de la gráfica
plt.xlabel("Profundidad (m)")
plt.ylabel("Presión de poro (kPa)")
plt.title("Consolidación unidimensional con un solo contorno drenante")
plt.legend()
plt.grid()
plt.show()