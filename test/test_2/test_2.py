import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def solve_consolidation_1d(cv=0.01, H=10, delta_sigma=100, 
                          nz=50, nt=1000, dt=0.1, plot_interval=50):
    """
    Resuelve la ecuación de consolidación unidimensional usando diferencias finitas (esquema explícito).
    
    Parámetros:
    cv            - Coeficiente de consolidación [m²/día]
    H             - Espesor del estrato [m]
    delta_sigma   - Incremento de carga [kPa]
    nz            - Número de puntos en la discretización espacial
    nt            - Número de pasos temporales
    dt            - Paso de tiempo [día]
    plot_interval - Intervalo para mostrar resultados intermedios
    """
    # Discretización espacial
    z = np.linspace(0, H, nz)
    dz = H / (nz - 1)
    
    # Verificar estabilidad
    r = cv * dt / (dz**2)
    if r > 0.5:
        print(f"¡Advertencia! r = {r:.4f} > 0.5, el esquema puede ser inestable.")
        print(f"Se recomienda reducir dt a {0.5 * dz**2 / cv:.4f} o menos.")
    
    # Inicializar presiones de poro (condición inicial: u = delta_sigma en todo el dominio)
    u = np.ones((nt, nz)) * delta_sigma
    
    # Aplicar condiciones de contorno (ambos extremos permeables: u = 0)
    u[:, 0] = 0    # Contorno inferior
    u[:, -1] = 0   # Contorno superior
    
    # Solución por diferencias finitas (esquema explícito)
    for j in range(0, nt-1):
        for i in range(1, nz-1):
            u[j+1, i] = r * u[j, i-1] + (1 - 2*r) * u[j, i] + r * u[j, i+1]
    
    # Calcular el tiempo adimensional Tv para cada paso de tiempo
    t = np.arange(0, nt) * dt
    Tv = cv * t / (H**2)
    
    # Gráficos
    plt.figure(figsize=(12, 10))
    
    # Gráfico 1: Distribución de presiones de poro en diferentes tiempos
    plt.subplot(2, 1, 1)
    for j in range(0, nt, plot_interval):
        plt.plot(u[j, :] / delta_sigma, z, label=f'Tv = {Tv[j]:.4f}')
    
    plt.xlabel('u/Δσ (Presión de poro normalizada)')
    plt.ylabel('Profundidad (m)')
    plt.title('Distribución de presiones de poro durante la consolidación')
    plt.legend()
    plt.grid(True)
    plt.gca().invert_yaxis()  # Invertir eje y para mostrar profundidad hacia abajo
    
    # Gráfico 2: Evolución temporal en diferentes profundidades
    plt.subplot(2, 1, 2)
    depths = [int(nz/4), int(nz/2), int(3*nz/4)]
    for i in depths:
        depth_value = z[i]
        plt.plot(Tv, u[:, i] / delta_sigma, label=f'z = {depth_value:.2f} m')
    
    plt.xlabel('Tv (Factor de tiempo)')
    plt.ylabel('u/Δσ (Presión de poro normalizada)')
    plt.title('Evolución temporal de la presión de poro a diferentes profundidades')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return u, z, t, Tv

# Ejecutar la función con parámetros de ejemplo
u, z, t, Tv = solve_consolidation_1d(cv=0.01, H=10, delta_sigma=100, 
                                    nz=50, nt=1000, dt=0.1, plot_interval=100)

# Crear una animación de la consolidación
def create_animation(u, z, Tv, delta_sigma):
    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot([], [])
    ax.set_xlim(0, 1)
    ax.set_ylim(max(z), min(z))
    ax.set_xlabel('u/Δσ (Presión de poro normalizada)')
    ax.set_ylabel('Profundidad (m)')
    ax.grid(True)
    title = ax.set_title('')
    
    def init():
        line.set_data([], [])
        return line,
    
    def animate(i):
        line.set_data(u[i, :] / delta_sigma, z)
        title.set_text(f'Tv = {Tv[i]:.4f}')
        return line, title
    
    ani = FuncAnimation(fig, animate, frames=range(0, len(Tv), 10),
                        init_func=init, blit=True, interval=50)
    
    plt.tight_layout()
    plt.show()
    
    return ani

# Crear la animación
ani = create_animation(u, z, Tv, 100)