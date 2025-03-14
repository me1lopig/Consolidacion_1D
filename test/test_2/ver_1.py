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

def graficar_resultados_unificados(z, t, u, H, cv, delta_sigma):
    """
    Función para graficar todos los resultados en figuras unificadas con leyendas completas
    """
    # Crear figura con dos subfiguras: perfiles y evolución temporal
    fig = plt.figure(figsize=(14, 10))
    
    # 1. GRÁFICO DE PERFILES DE PRESIÓN A DIFERENTES TIEMPOS
    ax1 = fig.add_subplot(121)
    
    # Definir tiempos para mostrar (factores de tiempo adimensional)
    Tv_valores = [0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0]
    tiempos_reales = [tv * (H/2)**2 / cv for tv in Tv_valores]
    
    # Generar colores con un mapa de color para visualización más clara
    cmap = plt.cm.viridis
    colores = [cmap(i/len(Tv_valores)) for i in range(len(Tv_valores))]
    
    # Graficar perfiles para cada tiempo seleccionado
    for k, (tiempo, color, tv) in enumerate(zip(tiempos_reales, colores, Tv_valores)):
        # Encontrar el índice de tiempo más cercano
        idx = np.argmin(np.abs(t - tiempo))
        
        # Graficar el perfil con el color asignado
        ax1.plot(u[:, idx]/delta_sigma, z, '-', color=color, linewidth=2, 
                label=f'Tv = {tv:.2f}, t = {t[idx]:.2f} años')
    
    ax1.set_xlabel('Exceso de presión de poro normalizado (u/Δσ)', fontsize=10)
    ax1.set_ylabel('Profundidad (m)', fontsize=10)
    ax1.set_ylim(H, 0)  # Invertir eje y para mostrar profundidad
    ax1.set_xlim(0, 1.1)
    ax1.set_title('Perfiles de exceso de presión de poro', fontsize=12)
    ax1.grid(True)
    ax1.legend(loc='best', fontsize=9)
    
    # 2. GRÁFICO DE EVOLUCIÓN TEMPORAL EN DIFERENTES PUNTOS
    ax2 = fig.add_subplot(122)
    
    # Seleccionar puntos representativos en el estrato
    punto_indices = [0, N//5, N//4, N//3, N//2, 2*N//3, 3*N//4, 4*N//5, N]
    profundidades = [z[i] for i in punto_indices]
    etiquetas = [f'z = {prof:.1f} m' for prof in profundidades]
    
    # Generar colores para diferentes profundidades
    cmap_puntos = plt.cm.cool
    colores_puntos = [cmap_puntos(i/len(punto_indices)) for i in range(len(punto_indices))]
    
    # Graficar evolución temporal para cada profundidad
    for i, (idx, label, color) in enumerate(zip(punto_indices, etiquetas, colores_puntos)):
        ax2.plot(t, u[idx, :]/delta_sigma, '-', color=color, linewidth=2, label=label)
    
    ax2.set_xlabel('Tiempo (años)', fontsize=10)
    ax2.set_ylabel('Exceso de presión de poro normalizado (u/Δσ)', fontsize=10)
    ax2.set_title('Evolución temporal a diferentes profundidades', fontsize=12)
    ax2.grid(True)
    ax2.legend(loc='best', fontsize=9)
    
    # Ajustar espaciado entre subfiguras
    plt.tight_layout()
    plt.savefig('consolidacion_perfiles_unificados.png', dpi=300)
    plt.show()
    
    # 3. GRÁFICO DEL GRADO DE CONSOLIDACIÓN (U)
    plt.figure(figsize=(10, 6))
    
    # Calcular grado de consolidación
    U = calcular_grado_consolidacion(u, delta_sigma)
    
    # Graficar grado de consolidación vs tiempo
    plt.plot(t, U*100, 'b-', linewidth=2.5)
    
    # Añadir líneas de referencia para grados específicos
    grados_referencia = [0, 20, 40, 60, 80, 90, 95, 99, 100]
    for grado in grados_referencia:
        plt.axhline(y=grado, color='gray', linestyle='--', alpha=0.3)
        
    # Calcular Tv90 (tiempo para 90% de consolidación)
    idx_90 = np.argmin(np.abs(U - 0.9))
    t_90 = t[idx_90]
    Tv_90 = cv * t_90 / ((H/2)**2)
    
    # Añadir anotación para Tv90
    plt.annotate(f'U=90%: T₉₀={Tv_90:.3f}, t={t_90:.2f} años', 
                xy=(t_90, 90), xytext=(t_90*1.1, 85),
                arrowprops=dict(arrowstyle='->'))
    
    plt.xlabel('Tiempo (años)', fontsize=12)
    plt.ylabel('Grado de Consolidación U (%)', fontsize=12)
    plt.title('Evolución del Grado de Consolidación', fontsize=14)
    plt.grid(True)
    plt.xlim(0, tiempo_final)
    plt.ylim(0, 102)
    
    # Añadir ejes secundarios con Factor de Tiempo
    ax_sec = plt.gca().twiny()
    ax_sec.set_xlim(0, tiempo_final*cv/((H/2)**2))
    ax_sec.set_xlabel('Factor de Tiempo (Tv)', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('grado_consolidacion.png', dpi=300)
    plt.show()

def calcular_grado_consolidacion(u, delta_sigma):
    """
    Calcula el grado de consolidación promedio en función del tiempo
    """
    # Inicializar arreglo para el grado de consolidación
    U = np.zeros(u.shape[1])
    
    # Calcular área total bajo el perfil inicial (proporcional al asentamiento total)
    area_inicial = np.trapz(u[:, a0], dx=dz)
    
    # Para cada paso de tiempo, calcular el grado de consolidación
    for j in range(u.shape[1]):
        # Área bajo el perfil actual
        area_actual = np.trapz(u[:, j], dx=dz)
        
        # Grado de consolidación (0 a 1)
        U[j] = 1.0 - (area_actual / area_inicial)
    
    return U

def crear_animacion(z, t, u, H, delta_sigma):
    """
    Crear una animación que muestre la evolución del proceso de consolidación
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    line, = ax.plot([], [], 'b-', linewidth=2.5, label='Exceso de presión de poro')
    
    ax.set_xlabel('u/Δσ', fontsize=12)
    ax.set_ylabel('Profundidad z (m)', fontsize=12)
    ax.set_ylim(H, 0)  # Invertir eje y para mostrar profundidad
    ax.set_xlim(0, 1.1)
    ax.grid(True)
    ax.legend(loc='upper right')
    
    texto_tiempo = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12)
    
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
    
    plt.tight_layout()
    plt.show()
    
    # Opción para guardar la animación
    # ani.save('consolidacion_animacion.gif', writer='pillow', fps=5, dpi=100)

# Parámetros del problema
H = 10.0             # Espesor del estrato (m)
cv = 0.1             # Coeficiente de consolidación (m²/año)
delta_sigma = 100.0  # Incremento de tensión (kPa)

# Parámetros numéricos
N = 40               # Número de divisiones espaciales
tiempo_final = 5.0   # Tiempo final de simulación (años)

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

# Graficar resultados unificados
graficar_resultados_unificados(z, t, u, H, cv, delta_sigma)

# Crear animación (opcional)
crear_animacion(z, t, u, H, delta_sigma)