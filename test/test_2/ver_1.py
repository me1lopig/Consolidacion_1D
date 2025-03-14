import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def consolidacion_diferencias_finitas(H, cv, delta_sigma, N, dt, tiempo_final):
    """
    Solución numérica por diferencias finitas (esquema explícito) para la ecuación de consolidación
    
    Parámetros:
    H: Espesor del estrato (m)
    cv: Coeficiente de consolidación (m²/año)
    delta_sigma: Incremento de tensión aplicado (kPa)
    N: Número de divisiones espaciales
    dt: Paso de tiempo (años)
    tiempo_final: Tiempo de simulación total (años)
    """
    # Discretización espacial
    dz = H / N
    z = np.linspace(0, H, N+1)
    
    # Discretización temporal
    pasos_tiempo = int(tiempo_final / dt) + 1
    t = np.linspace(0, tiempo_final, pasos_tiempo)
    
    # Matriz de resultados (filas: profundidad, columnas: tiempo)
    u = np.zeros((N+1, pasos_tiempo))
    
    # Condición inicial (presión de poro inicial = delta_sigma)
    u[1:N, 0] = delta_sigma
    
    # Condiciones de contorno (drenaje bidireccional)
    u[0, :] = 0  # Superficie superior drenante
    u[N, :] = 0  # Superficie inferior drenante
    
    # Número de Fourier (criterio de estabilidad: F <= 0.5)
    F = cv * dt / (dz**2)
    print(f"Número de Fourier: {F:.4f} {'(estable)' if F <= 0.5 else '(INESTABLE)'}")
    
    # Esquema iterativo (método explícito)
    for j in range(pasos_tiempo-1):
        for i in range(1, N):
            u[i, j+1] = u[i, j] + F * (u[i+1, j] - 2*u[i, j] + u[i-1, j])
    
    return z, t, u

def graficar_resultados(z, t, u, H, cv, delta_sigma):
    """
    Función para graficar los resultados de la solución por diferencias finitas
    """
    # Graficar perfiles de presión de poro a diferentes tiempos
    plt.figure(figsize=(12, 10))
    
    # Convertir tiempos a factor de tiempo adimensional
    Tv_valores = [0, 0.1, 0.2, 0.5, 0.8]
    tiempos_reales = [tv * (H/2)**2 / cv for tv in Tv_valores]
    
    for k, tiempo in enumerate(tiempos_reales):
        # Encontrar el índice de tiempo más cercano
        idx = np.argmin(np.abs(t - tiempo))
        
        plt.subplot(2, 3, k+1)
        plt.plot(u[:, idx]/delta_sigma, z, 'bo-', label='Diferencias Finitas')
        plt.xlabel('u/Δσ')
        plt.ylabel('Profundidad z (m)')
        plt.ylim(H, 0)  # Invertir eje y para mostrar profundidad
        plt.title(f'Tv = {Tv_valores[k]:.2f}, t = {t[idx]:.2f} años')
        plt.grid(True)
    
    # Graficar evolución temporal en diferentes puntos del estrato
    plt.subplot(2, 3, 6)
    
    # Seleccionar puntos representativos en el estrato
    puntos = [N//4, N//2, 3*N//4]  # 1/4, 1/2 y 3/4 de la altura
    etiquetas = ['1/4 H', 'Centro', '3/4 H']
    
    for idx, label in zip(puntos, etiquetas):
        plt.plot(t, u[idx, :]/delta_sigma, '-', label=label)
    
    plt.xlabel('Tiempo (años)')
    plt.ylabel('u/Δσ')
    plt.title('Evolución temporal en diferentes puntos')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('consolidacion_diferencias_finitas.png', dpi=300)
    plt.show()

def crear_animacion(z, t, u, H, delta_sigma):
    """
    Crear una animación que muestre la evolución del proceso de consolidación
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    line, = ax.plot([], [], 'bo-', label='Diferencias Finitas')
    
    ax.set_xlabel('u/Δσ')
    ax.set_ylabel('Profundidad z (m)')
    ax.set_ylim(H, 0)  # Invertir eje y para mostrar profundidad
    ax.set_xlim(0, 1.1)
    ax.grid(True)
    ax.legend()
    
    texto_tiempo = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    
    def init():
        line.set_data([], [])
        texto_tiempo.set_text('')
        return line, texto_tiempo
    
    def update(frame):
        idx = frame
        
        # Actualizar datos
        line.set_data(u[:, idx]/delta_sigma, z)
        
        # Calcular factor de tiempo adimensional
        Tv = cv * t[idx] / ((H/2)**2)
        texto_tiempo.set_text(f'Tiempo: {t[idx]:.2f} años (Tv = {Tv:.3f})')
        
        return line, texto_tiempo
    
    # Seleccionar un subconjunto de frames para la animación
    num_frames = min(50, len(t))
    frames = np.linspace(0, len(t)-1, num_frames, dtype=int)
    
    ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=200)
    
    # Guardar la animación (opcional)
    # ani.save('consolidacion_animacion.gif', writer='pillow', fps=5)
    
    plt.tight_layout()
    plt.show()

def calcular_grado_consolidacion(u, delta_sigma):
    """
    Calcula el grado de consolidación promedio en función del tiempo
    """
    # Inicializar arreglo para el grado de consolidación
    U = np.zeros(u.shape[1])
    
    # Integración numérica del exceso de presión inicial
    u_inicial = np.trapz(u[:, 0], axis=0)
    
    # Para cada paso de tiempo, calcular el grado de consolidación
    for j in range(u.shape[1]):
        # Exceso de presión en el tiempo t_j
        u_actual = np.trapz(u[:, j], axis=0)
        
        # Grado de consolidación (0 a 1)
        U[j] = 1.0 - (u_actual / u_inicial)
    
    return U

# Parámetros del problema
H = 10.0             # Espesor del estrato (m)
cv = 0.1             # Coeficiente de consolidación (m²/año)
delta_sigma = 100.0  # Incremento de tensión (kPa)

# Parámetros numéricos
N = 40               # Número de divisiones espaciales
tiempo_final = 25.0   # Tiempo final de simulación (años)

# Calcular paso de tiempo basado en criterio de estabilidad (F <= 0.5)
dz = H / N
dt_max = 0.5 * dz**2 / cv
dt = min(0.1, dt_max*0.8)  # Usar un paso de tiempo seguro

print("=== Simulación de Consolidación Unidimensional por Diferencias Finitas ===")
print(f"Estrato de espesor: {H} m")
print(f"Coeficiente de consolidación (cv): {cv} m²/año")
print(f"Incremento de tensión: {delta_sigma} kPa")
print(f"Discretización espacial (N): {N}")
print(f"Paso espacial (dz): {dz:.3f} m")
print(f"Paso de tiempo máximo permitido: {dt_max:.4f} años")
print(f"Paso de tiempo utilizado: {dt:.4f} años")

# Solución por diferencias finitas
z, t, u = consolidacion_diferencias_finitas(H, cv, delta_sigma, N, dt, tiempo_final)

# Calcular el grado de consolidación promedio
U = calcular_grado_consolidacion(u, delta_sigma)

# Graficar grado de consolidación
plt.figure(figsize=(10, 5))
plt.plot(t, U*100, 'b-', linewidth=2)
plt.xlabel('Tiempo (años)')
plt.ylabel('Grado de Consolidación U (%)')
plt.title('Evolución del Grado de Consolidación')
plt.grid(True)
plt.xlim(0, tiempo_final)
plt.ylim(0, 100)
plt.savefig('grado_consolidacion.png', dpi=300)
plt.show()

# Graficar resultados
graficar_resultados(z, t, u, H, cv, delta_sigma)

# Animar la solución (opcional - comentar si causa problemas de rendimiento)
crear_animacion(z, t, u, H, delta_sigma)