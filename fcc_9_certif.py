import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Necesario para evitar advertencias al trabajar con fechas en Matplotlib
register_matplotlib_converters()

# 1. Importar datos (Asegúrate de analizar las fechas. Considera establecer la columna 'date' como índice)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Asegurarse de que 'value' sea de tipo float
df['value'] = df['value'].astype(float)

# 2. Limpiar datos
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    """
    Dibuja un gráfico de líneas que muestra las vistas diarias del foro.
    """
    # Crear una copia de los datos limpios
    df_line = df.copy()

    # Configurar el gráfico de líneas
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_line.index, df_line['value'].astype(float), color='r', linewidth=1)

    # Etiquetas y título
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Guardar imagen y devolver fig (no cambies esta parte)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    """
    Dibuja un gráfico de barras que muestra el número promedio de vistas diarias por mes y año.
    """
    # Copiar y modificar datos para el gráfico de barras mensual
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Definir el orden correcto de los meses
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Calcular el promedio de vistas agrupado por año y mes
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reorganizar las columnas según el orden de los meses
    df_bar_grouped = df_bar_grouped[month_order]

    # Dibujar el gráfico de barras
    fig = df_bar_grouped.astype(float).plot(kind='bar', figsize=(14, 8)).figure

    # Personalizar el gráfico
    plt.title("Average Daily Page Views by Month and Year")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Guardar imagen y devolver fig (no cambies esta parte)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    """
    Dibuja dos diagramas de caja: uno por año y otro por mes.
    """
    # Preparar datos para los diagramas de caja
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    
    # Crear columnas para año y mes
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).strftime('%b')

    # Dibujar los diagramas de caja usando Seaborn
    fig, axes = plt.subplots(1, 2, figsize=(20, 8), sharey=True)

    # Diagrama de caja por año
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Diagrama de caja por mes
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    
    # Guardar imagen y devolver fig (no cambies esta parte)
    fig.savefig('box_plot.png')
    
    return fig

# Bloque principal para ejecutar las funciones
if __name__ == "__main__":
    # Generar todos los gráficos
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    
    # Mensaje de confirmación
    print("¡Visualizaciones creadas exitosamente!")
    print("Archivos generados:")
    print("- line_plot.png")
    print("- bar_plot.png")
    print("- box_plot.png")

# Salidas: 
# ¡Visualizaciones creadas exitosamente!
# Archivos generados:
# - line_plot.png
# - bar_plot.png
# - box_plot.png
              
