import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros mejorados ---
H = 4.0
drenaje_doble = True
cv = 0.8
u0 = 100
n_terms = 200  # Aumentamos de 50 a 200 términos
z_points = 500  # Más puntos para suavizar curvas
tiempos = [0, 0.01,0.1, 0.2, 1, 2, 5]

# Ajustar longitud de drenaje
H_drenaje = H / 2 if drenaje_doble else H

# --- Función mejorada ---
def calcular_presion_poro(z, t, n_terms):
    if t == 0:  # Forzar presión inicial exacta
        return u0
    u = 0.0
    for n in range(1, n_terms + 1):
        M = (np.pi / 2) * (2 * n - 1)
        termino = (2 * u0 / M) * np.sin(M * z / H_drenaje) * np.exp(-M**2 * (cv * t) / H_drenaje**2)
        u += termino
    return u

# --- Generar datos y graficar ---
z = np.linspace(0, H, z_points)

plt.figure(figsize=(12, 7))
for t in tiempos:
    u = [calcular_presion_poro(zi, t, n_terms) for zi in z]
    plt.plot(u, -z, linewidth=1.5, label=f't = {t} años')

plt.xlabel('Exceso de presión de poro, u (kPa)', fontsize=12)
plt.ylabel('Profundidad, z (m)', fontsize=12)
plt.title('Disipación de presión de poro en consolidación unidimensional', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()