import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Importar los datos desde "epa-sea-level.csv".
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Crear una figura y ejes para el gráfico.
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Diagrama de dispersión con los datos originales.
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Línea de mejor ajuste para todos los datos (1880-2013).
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(1880, 2051))
    sea_level_all = slope_all * years_all + intercept_all
    ax.plot(years_all, sea_level_all, color='red', label='Best Fit Line (1880-2050)')

    # Línea de mejor ajuste para los datos recientes (2000-2013).
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, sea_level_recent, color='green', label='Best Fit Line (2000-2050)')

    # Etiquetas y título.
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Guardar la imagen y devolver la figura.
    plt.savefig('sea_level_plot.png')
    return fig  # Devolver solo la figura