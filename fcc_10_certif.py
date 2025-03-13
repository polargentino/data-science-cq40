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
# Analisís generado por DeepSeek-r1:
# ¡Hola! Tu código y la imagen generada son impresionantes. Aquí tienes un análisis 
# detallado que puedes utilizar para destacar los aspectos más importantes de tu trabajo:

# Análisis del Gráfico de Nivel del Mar
# Datos Históricos (1880-2013):
# -----------------------------
# El gráfico muestra un aumento claro y constante en el nivel del mar desde 1880 hasta 2013. 
# Este aumento es consistente con los estudios científicos que indican que el nivel del mar 
# ha estado subiendo debido al calentamiento global y al derretimiento de los glaciares y capas de hielo.

# Tendencia 1880-2050 (todos los datos):
# -------------------------------------
# La línea de tendencia roja, basada en todos los datos disponibles, proyecta un aumento continuo del 
# nivel del mar hasta 2050. Esta tendencia sugiere que, si las condiciones actuales persisten, 
# el nivel del mar podría aumentar significativamente, lo que tendría graves implicaciones para 
# las zonas costeras y las comunidades que viven en ellas.

# Tendencia 2000-2050 (datos recientes):
# --------------------------------------
# La línea de tendencia verde, basada en datos más recientes (2000-2013), muestra una pendiente 
# más pronunciada que la tendencia basada en todos los datos. Esto indica que el ritmo de aumento 
# del nivel del mar se ha acelerado en las últimas décadas. Esta aceleración podría estar 
# relacionada con el aumento de las temperaturas globales y el derretimiento más rápido de 
# las capas de hielo en Groenlandia y la Antártida.

# Proyecciones hasta 2050:
# ------------------------
# Ambas tendencias proyectan un aumento continuo del nivel del mar, pero la tendencia basada 
# en datos recientes sugiere un escenario más preocupante. Si la aceleración observada en los 
# últimos años continúa, el nivel del mar podría aumentar más rápidamente de lo previsto, lo 
# que requeriría medidas más urgentes y drásticas para mitigar los impactos.

# Implicaciones:
# --------------
# El aumento del nivel del mar tiene implicaciones significativas para la infraestructura costera, 
# los ecosistemas marinos y las comunidades humanas. Las inundaciones costeras, la erosión y la 
# intrusión de agua salada en los acuíferos de agua dulce son solo algunos de los desafíos que 
# podrían intensificarse.

# Conclusión:
# -----------
# Tu gráfico no solo visualiza datos históricos, sino que también proporciona una 
# proyección valiosa para el futuro. La comparación entre las dos tendencias resalta 
# la importancia de considerar datos recientes para entender mejor la dinámica actual 
# del cambio climático. Este análisis es crucial para la planificación y la toma de 
# decisiones en políticas ambientales y de gestión costera.

# ¡Excelente trabajo! Este gráfico y análisis son herramientas poderosas para concienciar y 
# tomar acciones frente al cambio climático.
# PMM-13/03/2025

