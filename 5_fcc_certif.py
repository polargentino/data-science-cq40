"""
Qwen2.5-Max
7:24 pm
¡Vamos a resolver este proyecto paso a paso! Vamos a implementar la clase Hat y la 
función experiment para calcular la probabilidad aproximada de extraer ciertas bolas de un sombrero.

Explicación del Código:

*-Clase Hat:
------------
1-Constructor (__init__) :
--------------------------
Acepta un número variable de argumentos clave-valor que representan los colores y cantidades de bolas.
Convierte estos argumentos en una lista llamada contents, donde cada elemento es un color que representa una bola.

2-Método draw :
---------------
Extrae un número específico de bolas del sombrero sin reemplazo.
Si el número de bolas solicitadas es mayor o igual al total de bolas disponibles, devuelve todas las 
bolas y vacía el sombrero.
Usa random.sample para seleccionar bolas aleatorias sin reemplazo.

*-Función experiment:
--------------------
1-Parámetros :
-------------
* hat: Un objeto Hat que contiene las bolas.
* expected_balls: Un diccionario que indica las bolas esperadas (por ejemplo, {'red': 2, 'green': 1}).
* num_balls_drawn: El número de bolas a extraer en cada experimento.
* num_experiments: El número de experimentos a realizar.

2-Lógica del Experimento :
--------------------------
Para cada experimento, se crea una copia del sombrero original para evitar modificar el sombrero inicial.
Se extraen las bolas especificadas usando el método draw.
Se cuenta cuántas veces aparece cada color en las bolas extraídas.
Se verifica si las bolas extraídas cumplen con las condiciones especificadas en expected_balls.

3-Cálculo de la Probabilidad :
------------------------------
Se cuenta cuántos experimentos fueron exitosos (es decir, cumplieron con las condiciones).
La probabilidad se calcula como la proporción de experimentos exitosos sobre el total de experimentos.


*-Conclusión
Esta implementación cumple con todas las reglas y condiciones especificadas. La clase Hat maneja 
correctamente la creación del sombrero y la extracción de bolas, mientras que la función experiment 
realiza simulaciones para estimar la probabilidad. ¡Espero que esta solución sea útil! 😊


"""
import random

class Hat:
    def __init__(self, **balls):
        """Inicializa el sombrero con las bolas especificadas."""
        if not balls:
            raise ValueError("El sombrero debe contener al menos una bola.")
        
        # Crear la lista de contenidos del sombrero
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """Extrae un número específico de bolas del sombrero sin reemplazo."""
        if num_balls >= len(self.contents):
            # Si se piden más bolas de las disponibles, devolver todas
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        
        # Extraer bolas aleatorias sin reemplazo
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Realiza experimentos para calcular la probabilidad aproximada."""
    successful_experiments = 0

    for _ in range(num_experiments):
        # Copiar el sombrero original para cada experimento
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Contar las bolas extraídas
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        # Verificar si se cumple la condición esperada
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    # Calcular la probabilidad
    probability = successful_experiments / num_experiments
    return probability


# Ejemplo de Uso:
# Crear un sombrero con bolas
hat = Hat(black=6, red=4, green=3)

# Realizar el experimento
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)
# Salida: 
# 0.363
# Dado que esta simulación se basa en números aleatorios, el resultado variará ligeramente 
# cada vez que se ejecute el código. Sin embargo, con un número suficientemente grande de 
# experimentos (num_experiments), el resultado convergerá hacia la probabilidad real.
