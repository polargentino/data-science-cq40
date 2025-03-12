"""
Qwen2.5-Max
11:43 am
¡Vamos a resolver este proyecto paso a paso! Vamos a implementar el visualizador 
de datos médicos utilizando Pandas, Matplotlib y Seaborn. A continuación, te muestro 
cómo completar cada instrucción en el archivo


Explicación del Código:
-----------------------
Paso 1: Importar los Datos
---------------------------
Usamos `pd.read_csv` para cargar los datos desde el archivo `medical_examination.csv` y 
asignarlos a la variable `df`.

Paso 2: Agregar la Columna 'overweight'
-----------------------------------------
Calculamos el Índice de Masa Corporal (BMI) dividiendo el peso en kilogramos por el 
cuadrado de la altura en metros. 
Clasificamos a las personas como sobrepeso (`overweight = 1`) si su BMI es mayor que 25, 
y como no sobrepeso (`overweight = 0`) en caso contrario.

Paso 3: Normalizar los Datos
------------------------------
Para las columnas `cholesterol` y `gluc`, convertimos los valores:
--------------------------------------------------------------
- Si el valor es 1, lo normalizamos a 0 (bueno).
- Si el valor es 2 o 3, lo normalizamos a 1 (malo).

Paso 4: Crear el Gráfico Categórico
-------------------------------------
Reformatear los Datos:
----------------------
Usamos `pd.melt` para transformar los datos en un formato largo, donde cada fila 
representa una combinación de `cardio`, una variable categórica (`cholesterol`, `gluc`, etc.), y su valor.
Agrupamos los datos por `cardio`, `variable` y `value` para contar las frecuencias.

Dibujar el Gráfico:
--------------------
Usamos `sns.catplot` para crear un gráfico de barras que muestre los recuentos de cada característica.
El gráfico se divide en dos paneles según el valor de `cardio`.

Retornar la Figura:
--------------------
Guardamos la figura en la variable `fig` y la retornamos.

Paso 5: Crear el Mapa de Calor
--------------------------------
Limpiar los Datos:
-------------------
Filtramos los datos para eliminar valores atípicos:
---------------------------------------------------
- La presión diastólica (`ap_lo`) debe ser menor o igual que la sistólica (`ap_hi`).
- La altura y el peso deben estar dentro del rango percentil [2.5%, 97.5%].

Calcular la Matriz de Correlación:
-----------------------------------
Usamos `df_heat.corr()` para calcular la matriz de correlación.

Generar la Máscara:
--------------------
Creamos una máscara para ocultar la mitad superior de la matriz de correlación.

Dibujar el Mapa de Calor:
---------------------------
Usamos `sns.heatmap` para visualizar la matriz de correlación con anotaciones y una 
paleta de colores (`coolwarm`).

Retornar la Figura:
--------------------
Guardamos la figura en la variable `fig` y la retornamos.

Ejemplo de Uso:
---------------
if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
"""





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar datos
df = pd.read_csv('medical_examination.csv')

# 2. Calcular sobrepeso
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalizar variables
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Función para gráfico categórico
def draw_cat_plot():
    # Preparar datos
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Crear gráfico
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=5,
        aspect=1.2
    )
    
    # Guardar y cerrar figura
    g.savefig('categorical_plot.png', dpi=300, bbox_inches='tight')
    plt.close(g.fig)
    return g.fig

# 5. Función para mapa de calor
def draw_heat_map():
    # Filtrar datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))) &
        (df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975)))
    ]
    
    # Calcular correlación
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(
        corr,
        annot=True,
        fmt='.1f',
        mask=mask,
        cmap='coolwarm',
        square=True,
        cbar_kws={'shrink': 0.8},
        annot_kws={'size': 8}
    )
    
    # Guardar y cerrar figura
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    return fig

# Ejecutar análisis
if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    print("¡Análisis completado! Gráficos guardados como:")
    print("- categorical_plot.png")
    print("- correlation_heatmap.png")

# Salidas:(https://www.perplexity.ai/)
# ¡Análisis completado! Gráficos guardados como:
# - categorical_plot.png
# - correlation_heatmap.png
                           
