"""
Módulo para calcular y visualizar la trayectoria de un proyectil.

Este programa utiliza principios de programación orientada a objetos (POO) para modelar
la trayectoria de un proyectil en un entorno de simulación física. Se aplican conceptos
como encapsulación, getters, setters y manipulación de nombres para garantizar un código
limpio, seguro y fácil de mantener.

Aplicaciones en la ciencia:
- Física: Simulación de movimientos parabólicos, cálculo de alcance y altura máxima.
- Ingeniería: Diseño de trayectorias para cohetes, balística y sistemas de lanzamiento.
- Educación: Herramienta didáctica para enseñar conceptos de cinemática y dinámica.
- Videojuegos: Simulación de movimientos de proyectiles en entornos virtuales.

Autor: Pablo Monsalvo
Fecha: 22/03/2025
Ayuda de : DeepSeek-r1 y Gemini 2.0 Flash
"""

import math  # Importa el módulo math para operaciones matemáticas.

# Constantes globales
GRAVITATIONAL_ACCELERATION = 9.81  # Aceleración gravitacional en m/s².
PROJECTILE = "∙"  # Símbolo que representa el proyectil en el gráfico.
x_axis_tick = "T"  # Símbolo para el eje x en el gráfico.
y_axis_tick = "⊣"  # Símbolo para el eje y en el gráfico.


class Projectile:
    """
    Clase que representa un proyectil y calcula su trayectoria.

    Atributos privados:
    - __speed: Velocidad inicial del proyectil (en m/s).
    - __height: Altura inicial del proyectil (en metros).
    - __angle: Ángulo de lanzamiento (en radianes).

    Métodos públicos:
    - calculate_all_coordinates: Calcula las coordenadas (x, y) de la trayectoria.
    - Propiedades (getters y setters): Acceden y modifican los atributos privados.
    """

    __slots__ = ('__speed', '__height', '__angle')  # Optimiza el uso de memoria.

    def __init__(self, speed, height, angle):
        """
        Inicializa un proyectil con velocidad, altura y ángulo de lanzamiento.

        Parámetros:
        - speed: Velocidad inicial (en m/s).
        - height: Altura inicial (en metros).
        - angle: Ángulo de lanzamiento (en grados).
        """
        self.__speed = speed  # Velocidad inicial del proyectil.
        self.__height = height  # Altura inicial del proyectil.
        self.__angle = math.radians(angle)  # Convierte el ángulo a radianes.

    def __str__(self):
        """
        Devuelve una representación en cadena de los detalles del proyectil.

        Retorna:
        - Cadena formateada con los detalles del proyectil.
        """
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        """
        Calcula el desplazamiento horizontal máximo del proyectil.

        Retorna:
        - Desplazamiento horizontal máximo (en metros).
        """
        horizontal_component = self.__speed * math.cos(self.__angle)  # Componente horizontal de la velocidad.
        vertical_component = self.__speed * math.sin(self.__angle)  # Componente vertical de la velocidad.
        squared_component = vertical_component**2  # Cuadrado de la componente vertical.
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height  # Término relacionado con la altura inicial.
        sqrt_component = math.sqrt(squared_component + gh_component)  # Raíz cuadrada del término combinado.
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION  # Desplazamiento máximo.

    def __calculate_y_coordinate(self, x):
        """
        Calcula la coordenada y para un valor dado de x.

        Parámetros:
        - x: Coordenada horizontal.

        Retorna:
        - Coordenada vertical y.
        """
        height_component = self.__height  # Altura inicial.
        angle_component = math.tan(self.__angle) * x  # Término relacionado con el ángulo.
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)  # Término relacionado con la gravedad.
        y_coordinate = height_component + angle_component - acceleration_component  # Coordenada y.

        return y_coordinate
    
    def calculate_all_coordinates(self):
        """
        Calcula todas las coordenadas (x, y) de la trayectoria del proyectil.

        Retorna:
        - Lista de tuplas (x, y) que representan la trayectoria.
        """
        return [
            (x, self.__calculate_y_coordinate(x))  # Calcula y para cada x.
            for x in range(math.ceil(self.__calculate_displacement()))  # Itera sobre el rango de x.
        ]

    @property
    def height(self):
        """Getter para la altura inicial del proyectil."""
        return self.__height

    @property
    def angle(self):
        """Getter para el ángulo de lanzamiento (en grados)."""
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        """Getter para la velocidad inicial del proyectil."""
        return self.__speed

    @height.setter
    def height(self, n):
        """Setter para la altura inicial del proyectil."""
        self.__height = n

    @angle.setter
    def angle(self, n):
        """Setter para el ángulo de lanzamiento (en grados)."""
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
        """Setter para la velocidad inicial del proyectil."""
        self.__speed = s  # Asigna el nuevo valor de velocidad.
    
    def __repr__(self):
        """Representación formal del objeto Projectile."""
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'


class Graph:
    """
    Clase para representar gráficamente la trayectoria del proyectil.

    Atributos privados:
    - __coordinates: Lista de coordenadas (x, y) de la trayectoria.

    Métodos públicos:
    - create_coordinates_table: Crea una tabla de coordenadas.
    - create_trajectory: Genera un gráfico ASCII de la trayectoria.
    """

    __slots__ = ('__coordinates')  # Optimiza el uso de memoria.

    def __init__(self, coord):
        """
        Inicializa un gráfico con las coordenadas de la trayectoria.

        Parámetros:
        - coord: Lista de coordenadas (x, y).
        """
        self.__coordinates = coord  # Almacena las coordenadas.

    def __repr__(self):
        """Representación formal del objeto Graph."""
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        """
        Crea una tabla de coordenadas (x, y) de la trayectoria.

        Retorna:
        - Cadena formateada con la tabla de coordenadas.
        """
        table = '\n  x      y\n'  # Encabezado de la tabla.
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'  # Añade cada coordenada a la tabla.

        return table

    def create_trajectory(self):
        """
        Genera un gráfico ASCII de la trayectoria del proyectil.

        Retorna:
        - Cadena formateada con el gráfico ASCII.
        """
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]  # Redondea las coordenadas.

        x_max = max(rounded_coords, key=lambda i: i[0])[0]  # Máximo valor de x.
        y_max = max(rounded_coords, key=lambda j: j[1])[1]  # Máximo valor de y.

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]  # Crea una matriz vacía.

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE  # Coloca el proyectil en la posición (x, y).

        matrix = ["".join(line) for line in matrix_list]  # Convierte la matriz en una lista de cadenas.

        matrix_axes = [y_axis_tick + row for row in matrix]  # Añade el eje y.
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))  # Añade el eje x.

        graph = "\n" + "\n".join(matrix_axes) + "\n"  # Une todo en una cadena.

        return graph


def projectile_helper(speed, height, angle):
    """
    Función de utilidad para mostrar detalles, tabla de coordenadas y gráfico de la trayectoria de un proyectil.

    Parámetros:
    - speed: Velocidad inicial del proyectil (en m/s).
    - height: Altura inicial del proyectil (en metros).
    - angle: Ángulo de lanzamiento (en grados).
    """
    ball = Projectile(speed, height, angle)  # Crea un proyectil.
    print(ball)  # Muestra los detalles del proyectil.
    coordinates = ball.calculate_all_coordinates()  # Calcula las coordenadas de la trayectoria.
    graph = Graph(coordinates)  # Crea un gráfico con las coordenadas.
    print(graph.create_coordinates_table())  # Muestra la tabla de coordenadas.
    print(graph.create_trajectory())  # Muestra el gráfico de la trayectoria.


# Llamar a projectile_helper con valores de ejemplo.
projectile_helper(15, 5, 60)

# Salidas: 
"""
Projectile details:
speed: 15 m/s
height: 5 m
angle: 60°
displacement: 22.4 m


  x      y
  0   5.00
  1   6.64
  2   8.12
  3   9.41
  4  10.53
  5  11.48
  6  12.25
  7  12.85
  8  13.28
  9  13.53
 10  13.60
 11  13.50
 12  13.23
 13  12.78
 14  12.16
 15  11.36
 16  10.39
 17   9.24
 18   7.92
 19   6.43
 20   4.76
 21   2.92
 22   0.90


⊣         ∙∙∙           
⊣       ∙∙   ∙∙         
⊣      ∙       ∙        
⊣    ∙∙         ∙       
⊣                ∙      
⊣   ∙             ∙     
⊣  ∙               ∙    
⊣ ∙                     
⊣                   ∙   
⊣∙                   ∙  
⊣                       
⊣                     ∙ 
⊣                       
⊣                      ∙
⊣                       
 TTTTTTTTTTTTTTTTTTTTTTT"
 """

