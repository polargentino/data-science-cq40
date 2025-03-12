import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
#import matplotlib
#matplotlib.use('TkAgg')  # Cambia a un backend interactivo

def draw_plot():
    """
    Genera un gráfico de nivel del mar con proyecciones de tendencia.
    
    Esta función realiza las siguientes operaciones:
    1. Importa datos históricos del nivel del mar desde un archivo CSV.
    2. Crea un diagrama de dispersión con los datos originales.
    3. Calcula y traza dos líneas de tendencia:
       - Una usando todos los datos disponibles (1880-2013)
       - Otra usando solo datos recientes (2000-2013)
    4. Proyecta ambas tendencias hasta el año 2050.
    5. Guarda y muestra el gráfico resultante.

    Returns:
        matplotlib.figure.Figure: Objeto figura con el gráfico generado
        
    Archivo generado:
        sea_level_plot.png: Gráfico combinado con datos y tendencias
    """
    
    # 1. Cargar datos
    df = pd.read_csv('epa-sea-level.csv')
    
    # Configurar figura
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # 2. Diagrama de dispersión
    ax.scatter(
        x='Year', 
        y='CSIRO Adjusted Sea Level', 
        data=df, 
        color='#1f77b4', 
        alpha=0.7,
        label='Datos históricos (1880-2013)'
    )

    # 3. Regresión lineal para todos los datos
    slope_all, intercept_all, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(1880, 2051))
    ax.plot(
        years_all, 
        slope_all * years_all + intercept_all, 
        color='#d62728', 
        linewidth=2.5,
        label='Tendencia 1880-2050 (todos los datos)'
    )

    # 4. Regresión lineal para datos recientes
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(
        df_recent['Year'], 
        df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent, 
        slope_recent * years_recent + intercept_recent, 
        color='#2ca02c', 
        linewidth=2.5,
        linestyle='--',
        label='Tendencia 2000-2050 (datos recientes)'
    )

    # 5. Configuración estética
    ax.set_title(
        'Aumento del nivel del mar\nProyecciones de tendencia hasta 2050',
        fontsize=14,
        fontweight='bold',
        pad=20
    )
    
    ax.set_xlabel(
        'Año', 
        fontsize=12, 
        labelpad=10
    )
    
    ax.set_ylabel(
        'Nivel del mar (pulgadas)', 
        fontsize=12, 
        labelpad=10
    )
    
    ax.legend(
        frameon=True, 
        facecolor='white', 
        edgecolor='none',
        loc='upper left'
    )
    
    ax.grid(True, alpha=0.4)
    
    # 6. Guardar y mostrar resultados
    plt.tight_layout()
    plt.savefig('sea_level_plot.png', dpi=300)
    plt.show()
    
    return fig

# Ejecutar solo si es el script principal
if __name__ == "__main__":
    generated_figure = draw_plot()
    print("Análisis completado. Gráfico guardado como: sea_level_plot.png")
# Salidas: 
# Análisis completado. Gráfico guardado como: sea_level_plot.png