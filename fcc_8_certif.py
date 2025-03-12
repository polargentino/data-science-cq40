"""
Qwen2.5-Max
11:43 am
¡Vamos a resolver este proyecto paso a paso! Vamos a implementar el visualizador 
de datos médicos utilizando Pandas, Matplotlib y Seaborn. A continuación, te muestro 
cómo completar cada instrucción en el archivo

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column to the data.
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize the data by making 0 always good and 1 always bad.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    df_cat.rename(columns={'value': 'variable_value'}, inplace=True)
    
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='variable_value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig
    
    return fig

# 5. Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Clean the data in the df_heat variable by filtering out incorrect data.
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Drop the BMI column as it is not needed for the correlation matrix
    df_heat = df_heat.drop(columns=['BMI'], errors='ignore')
    
    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot the correlation matrix using sns.heatmap().
    sns.heatmap(
        corr,
        annot=True,
        fmt='.1f',
        mask=mask,
        cmap='coolwarm',
        square=True,
        cbar_kws={'shrink': 0.8}
    )
    
    # Return the figure for the output.
    return fig

# Imprimir la matriz de correlación
#print("Matriz de Correlación:")
#print(corr)

# Imprimir los datos limpios
#print("Datos Limpios:")
#print(df_heat.head())

