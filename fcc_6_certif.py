"""
Qwen2.5-Max
7:34 pm
¡Vamos a resolver este proyecto paso a paso! Vamos a implementar la función calculate() 
en Python utilizando NumPy para calcular las estadísticas requeridas. La función tomará 
una lista de 9 números, los convertirá en una matriz de 3x3 y calculará las estadísticas 
a lo largo de ambos ejes y para la matriz aplanada.

Explicación del Código:
-----------------------
1-Verificación de Entrada :
--------------------------
Se verifica que la lista tenga exactamente 9 elementos. Si no, se lanza una excepción ValueError con el 
mensaje especificado.

2-Conversión a Matriz :
-----------------------
La lista se convierte en una matriz de 3x3 usando np.array(lst).reshape(3, 3).

3-Cálculo de Estadísticas :
---------------------------
Para cada estadística (mean, variance, standard deviation, max, min, sum), se calculan los valores a lo largo de los 
ejes 0 (columnas), 1 (filas) y para la matriz aplanada.
Los resultados se convierten a listas usando .tolist() para cumplir con el formato requerido.

4-Estructura del Diccionario :
------------------------------
El diccionario retornado sigue el formato especificado, con claves para cada estadística y listas 
de resultados para los ejes y la matriz aplanada.

*-Conclusión:
-------------
Esta implementación cumple con todas las reglas y condiciones especificadas. La función calculate() 
maneja correctamente la entrada, realiza los cálculos necesarios y devuelve un diccionario con el 
formato requerido. ¡Espero que esta solución sea útil! 😊
"""
import numpy as np

def calculate(lst):
    # Verificar que la lista tenga exactamente 9 elementos
    if len(lst) != 9:
        raise ValueError("La lista debe contener nueve números.")
    
    # Convertir la lista en una matriz de 3x3
    matrix = np.array(lst).reshape(3, 3)
    
    # Calcular las estadísticas
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Media a lo largo del eje 0 (columnas)
            matrix.mean(axis=1).tolist(),  # Media a lo largo del eje 1 (filas)
            matrix.mean()                 # Media de la matriz aplanada
        ],
        'variance': [
            matrix.var(axis=0).tolist(),  # Varianza a lo largo del eje 0 (columnas)
            matrix.var(axis=1).tolist(),  # Varianza a lo largo del eje 1 (filas)
            matrix.var()                 # Varianza de la matriz aplanada
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),  # Desviación estándar a lo largo del eje 0 (columnas)
            matrix.std(axis=1).tolist(),  # Desviación estándar a lo largo del eje 1 (filas)
            matrix.std()                 # Desviación estándar de la matriz aplanada
        ],
        'max': [
            matrix.max(axis=0).tolist(),  # Máximo a lo largo del eje 0 (columnas)
            matrix.max(axis=1).tolist(),  # Máximo a lo largo del eje 1 (filas)
            matrix.max()                 # Máximo de la matriz aplanada
        ],
        'min': [
            matrix.min(axis=0).tolist(),  # Mínimo a lo largo del eje 0 (columnas)
            matrix.min(axis=1).tolist(),  # Mínimo a lo largo del eje 1 (filas)
            matrix.min()                 # Mínimo de la matriz aplanada
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),  # Suma a lo largo del eje 0 (columnas)
            matrix.sum(axis=1).tolist(),  # Suma a lo largo del eje 1 (filas)
            matrix.sum()                 # Suma de la matriz aplanada
        ]
    }
    
    return calculations

# Ejemplo de Uso:
# Importar la función calculate
from fcc_6_certif import calculate

# Probar la función con una lista de 9 números
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)

# Salidas: 
# {'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], np.float64(4.0)], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], np.float64(6.666666666666667)], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], np.float64(2.581988897471611)], 'max': [[6, 7, 8], [2, 5, 8], np.int64(8)], 'min': [[0, 1, 2], [0, 3, 6], np.int64(0)], 'sum': [[9, 12, 15], [3, 12, 21], np.int64(36)]}
# {'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], np.float64(4.0)], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], np.float64(6.666666666666667)], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], np.float64(2.581988897471611)], 'max': [[6, 7, 8], [2, 5, 8], np.int64(8)], 'min': [[0, 1, 2], [0, 3, 6], np.int64(0)], 'sum': [[9, 12, 15], [3, 12, 21], np.int64(36)]}
