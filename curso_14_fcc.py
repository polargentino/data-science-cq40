"""
La encapsulación es un principio fundamental de la programación orientada a objetos basado 
en la escritura de código que limita el acceso directo a los datos.

En este proyecto, descubrirás nuevos conceptos relacionados con la encapsulación, como getters, 
setters y manipulación de nombres, y los usarás junto con lo que ya aprendiste para crear un 
programa que calcule la trayectoria de un proyectil.
"""
import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s
    
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'


class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph


def projectile_helper(speed, height, angle):
    """
    Función de utilidad para mostrar detalles, tabla de coordenadas y gráfico de la trayectoria de un proyectil.

    Parámetros:
    - speed: Velocidad inicial del proyectil (en m/s).
    - height: Altura inicial del proyectil (en metros).
    - angle: Ángulo de lanzamiento (en grados).
    """
    ball = Projectile(speed, height, angle)
    print(ball)
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())


# Llamar a projectile_helper con valores de ejemplo.
projectile_helper(15, 5, 60)

# Ayuda de Gemini 2.0 Flash: 
# Projectile details:
# speed: 15 m/s
# height: 5 m
# angle: 60°
# displacement: 22.4 m


#   x      y
#   0   5.00
#   1   6.64
#   2   8.12
#   3   9.41
#   4  10.53
#   5  11.48
#   6  12.25
#   7  12.85
#   8  13.28
#   9  13.53
#  10  13.60
#  11  13.50
#  12  13.23
#  13  12.78
#  14  12.16
#  15  11.36
#  16  10.39
#  17   9.24
#  18   7.92
#  19   6.43
#  20   4.76
#  21   2.92
#  22   0.90


# ⊣         ∙∙∙           
# ⊣       ∙∙   ∙∙         
# ⊣      ∙       ∙        
# ⊣    ∙∙         ∙       
# ⊣                ∙      
# ⊣   ∙             ∙     
# ⊣  ∙               ∙    
# ⊣ ∙                     
# ⊣                   ∙   
# ⊣∙                   ∙  
# ⊣                       
# ⊣                     ∙ 
# ⊣                       
# ⊣                      ∙
# ⊣                       
#  TTTTTTTTTTTTTTTTTTTTTTT


