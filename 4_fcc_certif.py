"""
Qwen2.5-Max
7:22 pm
¡Vamos a resolver este proyecto paso a paso! Vamos a implementar las clases Rectangle y Square 
según las especificaciones proporcionadas. La clase Square será una subclase de Rectangle y 
heredará sus métodos y atributos.

Explicación del Código:
-----------------------
*-Clase Rectangle:
-----------------
1-Constructor (__init__) :
-------------------------
Inicializa los atributos width y height.

2-Métodos set_width y set_height :
----------------------------------
Permiten modificar el ancho y alto del rectángulo.

3-Método get_area :
------------------
Calcula el área multiplicando el ancho por el alto.

4-Método get_perimeter :
-----------------------
Calcula el perímetro sumando dos veces el ancho y dos veces el alto.

5-Método get_diagonal :
-----------------------
Calcula la diagonal usando el teorema de Pitágoras.

6-Método get_picture :
---------------------
Genera una representación gráfica del rectángulo usando asteriscos (*). Si el ancho o alto es 
mayor que 50, devuelve un mensaje indicando que es demasiado grande.

7-Método get_amount_inside :
---------------------------
Calcula cuántas veces cabe otra forma dentro del rectángulo dividiendo las dimensiones enteras.

8-Método __str__ :
------------------
Devuelve una representación en cadena del objeto rectángulo.

*-Clase Square:
--------------
1-Constructor (__init__) :
--------------------------
Llama al constructor de la clase base (Rectangle) y establece tanto el ancho como el alto al valor del lado.

2-Método set_side :
-------------------
Establece tanto el ancho como el alto al valor del lado.

3-Métodos set_width y set_height :
----------------------------------
Sobrescriben los métodos de la clase base para asegurarse de que el ancho y el alto siempre sean iguales.

4-Método __str__ :
------------------
Devuelve una representación en cadena del objeto cuadrado.


*-Conclusión
Esta implementación cumple con todas las reglas y condiciones especificadas. 
La clase Rectangle maneja correctamente los cálculos y representaciones, mientras que 
la clase Square hereda y extiende su funcionalidad. ¡Espero que esta solución sea útil! 😊

"""

class Rectangle:
    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y alto."""
        self.width = width
        self.height = height

    def set_width(self, width):
        """Establece el ancho del rectángulo."""
        self.width = width

    def set_height(self, height):
        """Establece la altura del rectángulo."""
        self.height = height

    def get_area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def get_perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Calcula la diagonal del rectángulo."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Devuelve una representación gráfica del rectángulo usando '*'."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        """Calcula cuántas veces cabe otra forma dentro de este rectángulo."""
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        """Representación en cadena del rectángulo."""
        return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):
    def __init__(self, side):
        """Inicializa un cuadrado con un lado dado."""
        super().__init__(side, side)

    def set_side(self, side):
        """Establece el lado del cuadrado."""
        self.width = side
        self.height = side

    def set_width(self, width):
        """Establece el ancho y alto del cuadrado."""
        self.width = width
        self.height = width

    def set_height(self, height):
        """Establece el ancho y alto del cuadrado."""
        self.width = height
        self.height = height

    def __str__(self):
        """Representación en cadena del cuadrado."""
        return f"Square(side={self.width})"
    
# Ejemplo de Uso:

rect = Rectangle(10, 5)
print(rect.get_area())  # Salida: 50
rect.set_height(3)
print(rect.get_perimeter())  # Salida: 26
print(rect)  # Salida: Rectangle(width=10, height=3)
print(rect.get_picture())
# Salida:
# **********
# **********
# **********

sq = Square(9)
print(sq.get_area())  # Salida: 81
sq.set_side(4)
print(sq.get_diagonal())  # Salida: 5.656854249492381
print(sq)  # Salida: Square(side=4)
print(sq.get_picture())
# Salida:
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Salida: 8

# Salidas:
# 50 (Área del rectángulo)
# 26 (Perímetro del rectángulo después de ajustar la altura)
# Rectangle(width=10, height=3) (Representación en cadena del rectángulo)
# ********** (Representación gráfica del rectángulo)
# **********
# **********

# 81 (Área del cuadrado)
# 5.656854249492381 (Diagonal del cuadrado después de ajustar el lado)
# Square(side=4) (Representación en cadena del cuadrado)
# **** (Representación gráfica del cuadrado)
# ****
# ****
# ****

# 8
         