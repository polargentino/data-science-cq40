"""
Módulo para resolver y graficar ecuaciones lineales y cuadráticas.

Este módulo define clases para representar, resolver y graficar ecuaciones lineales y cuadráticas.
Incluye métodos para calcular soluciones, analizar propiedades, formatear la salida y mostrar gráficos.

Dependencias:
- matplotlib: Para graficar las ecuaciones.
"""

from abc import ABC, abstractmethod
import re
import matplotlib.pyplot as plt
import numpy as np


class Equation(ABC):
    """
    Clase abstracta que representa una ecuación algebraica.

    Atributos:
    - degree: Grado de la ecuación (debe ser definido por las subclases).
    - type: Tipo de ecuación (debe ser definido por las subclases).
    """

    degree: int  # Grado de la ecuación (por ejemplo, 1 para lineal, 2 para cuadrática).
    type: str  # Tipo de ecuación (por ejemplo, "Linear Equation" o "Quadratic Equation").

    def __init__(self, *args):
        """
        Inicializa la ecuación con coeficientes.

        Parámetros:
        - args: Coeficientes de la ecuación.

        Lanza:
        - TypeError: Si el número de coeficientes no coincide con el grado de la ecuación.
        - TypeError: Si los coeficientes no son números (int o float).
        - ValueError: Si el coeficiente de mayor grado es cero.
        """
        if (self.degree + 1) != len(args):  # Verifica si el número de coeficientes es correcto.
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):  # Verifica si los coeficientes son números.
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:  # Verifica que el coeficiente de mayor grado no sea cero.
            raise ValueError("Highest degree coefficient must be different from zero")
        # Almacena los coeficientes en un diccionario con su grado correspondiente.
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):
        """
        Verifica que las subclases tengan los atributos requeridos (degree y type).
        """
        if not hasattr(cls, "degree"):  # Verifica si la subclase tiene el atributo 'degree'.
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):  # Verifica si la subclase tiene el atributo 'type'.
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    def __str__(self):
        """
        Devuelve la ecuación en formato de cadena.

        Ejemplo:
        - Para una ecuación cuadrática: "x**2 + 2x + 1 = 0".
        """
        terms = []  # Lista para almacenar los términos de la ecuación.
        for n, coefficient in self.coefficients.items():  # Itera sobre los coeficientes.
            if not coefficient:  # Si el coeficiente es cero, se omite el término.
                continue
            if n == 0:  # Término independiente (sin x).
                terms.append(f'{coefficient:+}')
            elif n == 1:  # Término lineal (x).
                terms.append(f'{coefficient:+}x')
            else:  # Términos de grado superior (x**n).
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = ' '.join(terms) + ' = 0'  # Une los términos y añade "= 0".
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))  # Elimina coeficientes "1" innecesarios.

    @abstractmethod
    def solve(self):
        """
        Método abstracto para resolver la ecuación.
        Debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def analyze(self):
        """
        Método abstracto para analizar propiedades de la ecuación.
        Debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def plot(self, x_range=(-10, 10)):
        """
        Método abstracto para graficar la ecuación.
        Debe ser implementado por las subclases.
        """
        pass


class LinearEquation(Equation):
    """
    Clase que representa una ecuación lineal (grado 1).
    Hereda de Equation.
    """

    degree = 1  # Grado de la ecuación.
    type = 'Linear Equation'  # Tipo de ecuación.

    def solve(self):
        """
        Resuelve la ecuación lineal.

        Retorna:
        - Lista con la solución de la ecuación.
        """
        a, b = self.coefficients.values()  # Obtiene los coeficientes.
        x = -b / a  # Calcula la solución.
        return [x]

    def analyze(self):
        """
        Analiza propiedades de la ecuación lineal.

        Retorna:
        - Diccionario con la pendiente (slope) y el intercepto (intercept).
        """
        slope, intercept = self.coefficients.values()  # Obtiene los coeficientes.
        return {'slope': slope, 'intercept': intercept}  # Devuelve las propiedades.

    def plot(self, x_range=(-10, 10)):
        """
        Grafica la ecuación lineal.

        Parámetros:
        - x_range: Rango de valores de x para graficar (por defecto de -10 a 10).
        """
        a, b = self.coefficients.values()  # Obtiene los coeficientes.
        x = np.linspace(x_range[0], x_range[1], 400)  # Genera 400 puntos en el rango de x.
        y = a * x + b  # Calcula los valores de y.
        plt.plot(x, y, label=f'{self}')  # Grafica la ecuación.
        plt.axhline(0, color='black', linewidth=0.5)  # Eje x.
        plt.axvline(0, color='black', linewidth=0.5)  # Eje y.
        plt.title("Gráfico de la Ecuación Lineal")  # Título del gráfico.
        plt.xlabel("x")  # Etiqueta del eje x.
        plt.ylabel("y")  # Etiqueta del eje y.
        plt.legend()  # Muestra la leyenda.
        plt.grid(True)  # Muestra la cuadrícula.
        plt.show()  # Muestra el gráfico.


class QuadraticEquation(Equation):
    """
    Clase que representa una ecuación cuadrática (grado 2).
    Hereda de Equation.
    """

    degree = 2  # Grado de la ecuación.
    type = 'Quadratic Equation'  # Tipo de ecuación.

    def __init__(self, *args):
        """
        Inicializa la ecuación cuadrática y calcula el discriminante (delta).
        """
        super().__init__(*args)  # Llama al constructor de la clase base.
        a, b, c = self.coefficients.values()  # Obtiene los coeficientes.
        self.delta = b**2 - 4 * a * c  # Calcula el discriminante.

    def solve(self):
        """
        Resuelve la ecuación cuadrática.

        Retorna:
        - Lista con las soluciones de la ecuación.
        """
        if self.delta < 0:  # Si el discriminante es negativo, no hay soluciones reales.
            return []
        a, b, _ = self.coefficients.values()  # Obtiene los coeficientes.
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)  # Calcula la primera solución.
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)  # Calcula la segunda solución.
        if self.delta == 0:  # Si el discriminante es cero, hay una única solución.
            return [x1]
        return [x1, x2]  # Devuelve las soluciones.

    def analyze(self):
        """
        Analiza propiedades de la ecuación cuadrática.

        Retorna:
        - Diccionario con el vértice, concavidad y tipo de extremo (mínimo o máximo).
        """
        a, b, c = self.coefficients.values()  # Obtiene los coeficientes.
        x = -b / (2 * a)  # Calcula la coordenada x del vértice.
        y = a * x**2 + b * x + c  # Calcula la coordenada y del vértice.
        if a > 0:  # Determina la concavidad y el tipo de extremo.
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}  # Devuelve las propiedades.

    def plot(self, x_range=(-10, 10)):
        """
        Grafica la ecuación cuadrática.

        Parámetros:
        - x_range: Rango de valores de x para graficar (por defecto de -10 a 10).
        """
        a, b, c = self.coefficients.values()  # Obtiene los coeficientes.
        x = np.linspace(x_range[0], x_range[1], 400)  # Genera 400 puntos en el rango de x.
        y = a * x**2 + b * x + c  # Calcula los valores de y.
        plt.plot(x, y, label=f'{self}')  # Grafica la ecuación.
        plt.axhline(0, color='black', linewidth=0.5)  # Eje x.
        plt.axvline(0, color='black', linewidth=0.5)  # Eje y.
        plt.title("Gráfico de la Ecuación Cuadrática")  # Título del gráfico.
        plt.xlabel("x")  # Etiqueta del eje x.
        plt.ylabel("y")  # Etiqueta del eje y.
        plt.legend()  # Muestra la leyenda.
        plt.grid(True)  # Muestra la cuadrícula.
        plt.show()  # Muestra el gráfico.


def solver(equation):
    """
    Función para resolver, mostrar detalles y graficar una ecuación.

    Parámetros:
    - equation: Objeto de tipo Equation (LinearEquation o QuadraticEquation).

    Retorna:
    - Cadena formateada con la solución y detalles de la ecuación.
    """
    if not isinstance(equation, Equation):  # Verifica si el argumento es una ecuación válida.
        raise TypeError("Argument must be an Equation object")

    output_string = f'\n{equation.type:-^24}'  # Título centrado.
    output_string += f'\n\n{equation!s:^24}\n\n'  # Ecuación centrada.
    output_string += f'{"Solutions":-^24}\n\n'  # Sección de soluciones.
    results = equation.solve()  # Resuelve la ecuación.
    match results:
        case []:
            result_list = ['No real roots']  # Si no hay soluciones reales.
        case [x]:
            result_list = [f'x = {x:+.3f}']  # Si hay una solución.
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']  # Si hay dos soluciones.
    for result in result_list:
        output_string += f'{result:^24}\n'  # Añade las soluciones a la cadena de salida.
    output_string += f'\n{"Details":-^24}\n\n'  # Sección de detalles.
    details = equation.analyze()  # Analiza las propiedades de la ecuación.
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']  # Detalles para ecuaciones lineales.
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'  # Coordenadas del vértice.
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']  # Detalles para ecuaciones cuadráticas.
    for detail in details_list:
        output_string += f'{detail}\n'  # Añade los detalles a la cadena de salida.

    equation.plot()  # Grafica la ecuación.
    return output_string  # Devuelve la cadena formateada.


# Ejemplo de uso:
lin_eq = LinearEquation(2, 3)  # Crea una ecuación lineal.
quadr_eq = QuadraticEquation(1, 2, 1)  # Crea una ecuación cuadrática.
print(solver(quadr_eq))  # Resuelve, muestra detalles y grafica la ecuación cuadrática.

# Salidas: + ecuación_cuadrática_1.png
# Ayuda de DeepSeek-r1
# ---Quadratic Equation---

#     x**2 +2x +1 = 0     

# -------Solutions--------

#        x = -1.000       

# --------Details---------

# concavity =      upwards
# min =    (-1.000, 0.000)


# Explicación de los cambios:
# Método plot:

# Se añadió un método abstracto plot en la clase Equation para que todas las subclases lo implementen.

# En LinearEquation, se grafica una línea recta usando la ecuación 
# y = ax + b


# En QuadraticEquation, se grafica una parábola usando la ecuación 
# y = ax2 + bx + c


# Uso de Matplotlib:

# Se utiliza matplotlib.pyplot para crear gráficos.

# Se generan 400 puntos en el rango de x para suavizar la curva.

# Se añaden ejes, título, etiquetas, leyenda y cuadrícula para mejorar la visualización.

# Integración en solver:

# Después de resolver y mostrar los detalles de la ecuación, se llama al método plot para graficarla.