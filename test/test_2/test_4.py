import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def solve_consolidation_1d(cv=0.01, H=10, delta_sigma=100, 
                          nz=50, nt=1000, dt=0.1, max_time=None):
    """
    Resuelve la ecuación de consolidación unidimensional usando diferencias finitas.
    
    Parámetros:
    cv            - Coeficiente de consolidación [m²/día]
    H             - Espesor del estrato [m]
    delta_sigma   - Incremento de carga [kPa]
    nz            - Número de puntos en la discretización espacial
    nt            - Número de pasos temporales
    dt            - Paso de tiempo [día]
    max_time      - Tiempo máximo de simulación [día] (opcional)
    """
    # Ajustar nt si se especifica max_time
      
    
    if max_time is not None:
        nt = int(max_time / dt) + 1
    
    # Discretización espacial
    z = np.linspace(0, H, nz)
    dz = H / (nz - 1)
    
    # Tiempos
    t = np.arange(0, nt) * dt  # tiempo en días
    
    # Verificar estabilidad
    r = cv * dt / (dz**2)
    if r > 0.5:
        print(f"¡Advertencia! r = {r:.4f} > 0.5, el esquema puede ser inestable.")
        print(f"Se recomienda reducir dt a {0.5 * dz**2 / cv:.4f} días o menos.")
        print(f"Continuando con la solución, pero los resultados pueden ser inexactos.")
    else:
        print(f"Esquema estable (r = {r:.4f} <= 0.5)")
    
    # Inicializar presiones de poro
    u = np.ones((nt, nz)) * delta_sigma
    
    # Aplicar condiciones de contorno (ambos extremos permeables)
    u[:, 0] = 0    # Contorno inferior
    u[:, -1] = 0   # Contorno superior
    
    # Solución por diferencias finitas (esquema explícito)
    for j in range(0, nt-1):
        for i in range(1, nz-1):
            u[j+1, i] = r * u[j, i-1] + (1 - 2*r) * u[j, i] + r * u[j, i+1]
    
    # Calcular el grado de consolidación para cada paso de tiempo
    U = np.zeros(nt)
    
    for j in range(nt):
        # Integración numérica para calcular el área bajo la curva u(z)
        # Usamos trapezoid en lugar de trapz (que está obsoleto)
        u_avg = np.trapezoid(u[j, :], z) / H
        u_avg_initial = np.trapezoid(u[0, :], z) / H
        
        # Grado de consolidación
        if u_avg_initial > 0:  # Evitar división por cero
            U[j] = 1 - (u_avg / u_avg_initial)
        else:
            U[j] = 1.0
    
    # Determinar tiempos para las gráficas (distribución logarítmica)
    if nt > 5:
        plot_times = [0]  # Siempre incluir t=0
        
        # Añadir puntos logarítmicamente espaciados
        log_times = np.logspace(0, np.log10(nt-1), 6).astype(int)
        for idx in log_times:
            if idx > 0 and idx < nt and idx not in plot_times:
                plot_times.append(idx)
        
        # Asegurar que tengamos el último punto
        if nt-1 not in plot_times:
            plot_times.append(nt-1)
    else:
        plot_times = list(range(nt))
    
    # GRÁFICO 1: Distribución de presiones de poro en diferentes tiempos (VENTANA 1)
    plt.figure(figsize=(8, 7))
    for j in plot_times:
        plt.plot(u[j, :] / delta_sigma, z, 
                 label=f't = {t[j]:.1f} días (U = {U[j]:.2f})')
    
    plt.xlabel('u/Δσ (Presión de poro normalizada)')
    plt.ylabel('Profundidad (m)')
    plt.title('Distribución de presiones de poro durante la consolidación')
    plt.legend()
    plt.grid(True)
    plt.gca().invert_yaxis()  # Invertir eje y
    plt.tight_layout()
    plt.show()
    
    # GRÁFICO 2: Evolución temporal en diferentes profundidades (VENTANA 2)
    plt.figure(figsize=(8, 7))
    
    # Elegir profundidades para mostrar (evitar los bordes)
    if nz >= 7:  # Si tenemos suficientes puntos
        depth_indices = [
            max(1, int(nz/6)),            # cerca del borde inferior
            int(nz/3),                    # primer tercio
            int(nz/2),                    # medio
            min(int(5*nz/6), nz-2)        # cerca del borde superior
        ]
    else:  # Si tenemos pocos puntos
        depth_indices = [max(1, nz//2)]   # punto medio
    
    for i in depth_indices:
        depth_value = z[i]
        plt.plot(t, u[:, i] / delta_sigma, 
                 label=f'z = {depth_value:.2f} m')
    
    plt.xlabel('Tiempo (días)')
    plt.ylabel('u/Δσ (Presión de poro normalizada)')
    plt.title('Evolución temporal de la presión de poro a diferentes profundidades')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # GRÁFICO 3: Grado de consolidación vs tiempo (VENTANA 3)
    plt.figure(figsize=(8, 7))
    plt.plot(t, U * 100, 'r-', linewidth=2)  # Mostrar como porcentaje
    plt.xlabel('Tiempo (días)')
    plt.ylabel('U (Grado de consolidación) [%]')
    plt.title('Evolución del grado de consolidación')
    plt.grid(True)
    plt.ylim(0, 105)
    
    # Marcar hitos importantes de consolidación
    for percent in [50, 90]:
        # Encontrar el primer tiempo donde se alcanza este porcentaje
        percent_decimal = percent / 100.0
        indices = np.where(U >= percent_decimal)[0]
        
        if len(indices) > 0:
            idx = indices[0]
            plt.plot(t[idx], U[idx] * 100, 'bo', markersize=6)
            plt.text(t[idx]*1.05, U[idx] * 100, 
                    f'U = {percent}%, t = {t[idx]:.1f} días')
    
    plt.tight_layout()
    plt.show()
    
    # Mostrar tiempos importantes en consola
    print("\nHitos de consolidación:")
    for percent in [50, 80, 90, 95]:
        percent_decimal = percent / 100.0
        indices = np.where(U >= percent_decimal)[0]
        
        if len(indices) > 0:
            idx = indices[0]
            print(f"Tiempo para alcanzar U = {percent}%: {t[idx]:.2f} días")
        else:
            print(f"No se alcanzó U = {percent}% en el tiempo simulado")
    
    return u, z, t, U

# Ejecutar con parámetros ajustados para asegurar resultados claros
u, z, t, U = solve_consolidation_1d(
    cv=0.005,       # Coeficiente de consolidación [m²/día]
    H=10,           # Espesor del estrato [m]
    delta_sigma=100,# Incremento de carga [kPa]
    nz=50,          # Puntos en espacio
    dt=0.5,         # Paso de tiempo [día]
    max_time=6000   # Tiempo máximo [día]
)

# Animación independiente que muestra la evolución del proceso
def create_animation(u, z, t, U, delta_sigma):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico de presión vs profundidad
    line, = ax1.plot([], [])
    ax1.set_xlim(0, 1)
    ax1.set_ylim(max(z), min(z))
    ax1.set_xlabel('u/Δσ (Presión de poro normalizada)')
    ax1.set_ylabel('Profundidad (m)')
    ax1.grid(True)
    title1 = ax1.set_title('')
    
    # Gráfico de grado de consolidación vs tiempo
    line2, = ax2.plot([], [], 'r-', linewidth=2)
    point, = ax2.plot([], [], 'bo', markersize=6)
    ax2.set_xlim(0, max(t))
    ax2.set_ylim(0, 105)
    ax2.set_xlabel('Tiempo (días)')
    ax2.set_ylabel('U (Grado de consolidación) [%]')
    ax2.grid(True)
    
    # Determinar el número de frames para la animación
    n_frames = min(100, len(t))
    frame_indices = np.linspace(0, len(t)-1, n_frames).astype(int)
    
    def init():
        line.set_data([], [])
        line2.set_data([], [])
        point.set_data([], [])
        return line, line2, point
    


