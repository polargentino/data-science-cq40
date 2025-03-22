"""
Los métodos especiales de Python se llaman en respuesta a operaciones específicas y 
le permiten personalizar el comportamiento de sus objetos de una manera detallada y efectiva.

En este proyecto, explorarás algunos de los métodos especiales más comunes mientras 
aprendes sobre los vectores mediante la construcción de un espacio vectorial.
"""
"""
Clase R2Vector: Representa un vector en un espacio bidimensional (R²).
Esta clase incluye métodos para operaciones básicas de vectores, como suma, resta,
producto punto, norma (magnitud), comparaciones y representación en cadena.
"""

class R2Vector:
    def __init__(self, *, x, y):
        """
        Inicializa un vector en R² con componentes x e y.
        :param x: Componente en el eje x.
        :param y: Componente en el eje y.
        """
        self.x = x  # Asigna el valor de x al atributo x del vector.
        self.y = y  # Asigna el valor de y al atributo y del vector.

    def norm(self):
        """
        Calcula la norma (magnitud) del vector.
        :return: La norma del vector, calculada como la raíz cuadrada de la suma de los 
        cuadrados de sus componentes.
        """
        return sum(val**2 for val in vars(self).values())**0.5  # Usa comprensión de listas para calcular la norma.

    def __str__(self):
        """
        Representación en cadena del vector, útil para imprimir.
        :return: Una cadena que representa el vector como una tupla (x, y).
        """
        return str(tuple(getattr(self, i) for i in vars(self)))  # Convierte el vector en una tupla y luego en cadena.

    def __repr__(self):
        """
        Representación formal del vector, útil para depuración.
        :return: Una cadena que muestra cómo se crearía el vector.
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]  # Crea una lista de argumentos en formato clave=valor.
        args = ', '.join(arg_list)  # Une los argumentos en una cadena.
        return f'{self.__class__.__name__}({args})'  # Devuelve una cadena que representa la creación del objeto.

    def __add__(self, other):
        """
        Suma dos vectores.
        :param other: Otro vector de la misma clase.
        :return: Un nuevo vector que es la suma de self y other.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}  # Suma componente a componente.
        return self.__class__(**kwargs)  # Crea y devuelve un nuevo vector con los resultados.

    def __sub__(self, other):
        """
        Resta dos vectores.
        :param other: Otro vector de la misma clase.
        :return: Un nuevo vector que es la resta de self y other.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}  # Resta componente a componente.
        return self.__class__(**kwargs)  # Crea y devuelve un nuevo vector con los resultados.

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o calcula el producto punto con otro vector.
        :param other: Un escalar (int o float) o otro vector de la misma clase.
        :return: Un nuevo vector (si es multiplicación por escalar) o un escalar (si es producto punto).
        """
        if type(other) in (int, float):  # Si other es un escalar.
            kwargs = {i: getattr(self, i) * other for i in vars(self)}  # Multiplica cada componente por el escalar.
            return self.__class__(**kwargs)  # Devuelve un nuevo vector.
        elif type(self) == type(other):  # Si other es otro vector.
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]  # Multiplica componente a componente.
            return sum(args)  # Devuelve la suma de los productos (producto punto).
        return NotImplemented  # Si no es un caso válido, devuelve NotImplemented.

    def __eq__(self, other):
        """
        Compara si dos vectores son iguales.
        :param other: Otro vector de la misma clase.
        :return: True si todos los componentes son iguales, False en caso contrario.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))  # Compara componente a componente.

    def __ne__(self, other):
        """
        Compara si dos vectores son diferentes.
        :param other: Otro vector de la misma clase.
        :return: True si al menos un componente es diferente, False en caso contrario.
        """
        return not self == other  # Usa el método __eq__ para determinar la desigualdad.

    def __lt__(self, other):
        """
        Compara si la norma de self es menor que la norma de other.
        :param other: Otro vector de la misma clase.
        :return: True si la norma de self es menor, False en caso contrario.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        return self.norm() < other.norm()  # Compara las normas de los vectores.

    def __gt__(self, other):
        """
        Compara si la norma de self es mayor que la norma de other.
        :param other: Otro vector de la misma clase.
        :return: True si la norma de self es mayor, False en caso contrario.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        return self.norm() > other.norm()  # Compara las normas de los vectores.

    def __le__(self, other):
        """
        Compara si la norma de self es menor o igual que la norma de other.
        :param other: Otro vector de la misma clase.
        :return: True si la norma de self es menor o igual, False en caso contrario.
        """
        return not self > other  # Usa el método __gt__ para determinar si es menor o igual.

    def __ge__(self, other):
        """
        Compara si la norma de self es mayor o igual que la norma de other.
        :param other: Otro vector de la misma clase.
        :return: True si la norma de self es mayor o igual, False en caso contrario.
        """
        return not self < other  # Usa el método __lt__ para determinar si es mayor o igual.

"""
Clase R3Vector: Representa un vector en un espacio tridimensional (R³).
Hereda de R2Vector y añade funcionalidad para el componente z.
Además, incluye un método para calcular el producto cruz entre dos vectores en R³.
"""
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        """
        Inicializa un vector en R³ con componentes x, y y z.
        :param x: Componente en el eje x.
        :param y: Componente en el eje y.
        :param z: Componente en el eje z.
        """
        super().__init__(x=x, y=y)  # Llama al constructor de R2Vector para inicializar x e y.
        self.z = z  # Asigna el valor de z al atributo z del vector.

    def cross(self, other):
        """
        Calcula el producto cruz entre dos vectores en R³.
        :param other: Otro vector de la misma clase.
        :return: Un nuevo vector que es el producto cruz de self y other.
        """
        if type(self) != type(other):  # Verifica que ambos vectores sean del mismo tipo.
            return NotImplemented  # Si no lo son, devuelve NotImplemented.
        kwargs = {
            'x': self.y * other.z - self.z * other.y,  # Calcula la componente x del producto cruz.
            'y': self.z * other.x - self.x * other.z,  # Calcula la componente y del producto cruz.
            'z': self.x * other.y - self.y * other.x   # Calcula la componente z del producto cruz.
        }
        return self.__class__(**kwargs)  # Crea y devuelve un nuevo vector con los resultados.

# Ejemplo de uso:
v1 = R3Vector(x=2, y=3, z=1)  # Crea un vector v1 en R³.
v2 = R3Vector(x=0.5, y=1.25, z=2)  # Crea un vector v2 en R³.
print(f'v1 = {v1}')  # Imprime el vector v1.
print(f'v2 = {v2}')  # Imprime el vector v2.
v3 = v1 + v2  # Suma v1 y v2.
print(f'v1 + v2 = {v3}')  # Imprime el resultado de la suma.
v4 = v1 - v2  # Resta v2 de v1.
print(f'v1 - v2 = {v4}')  # Imprime el resultado de la resta.
v5 = v1 * v2  # Calcula el producto punto entre v1 y v2.
print(f'v1 * v2 = {v5}')  # Imprime el resultado del producto punto.
v6 = v1.cross(v2)  # Calcula el producto cruz entre v1 y v2.
print(f'v1 x v2 = {v6}')  # Imprime el resultado del producto cruz.

# Salidas: 
# v1 = (2, 3, 1)
# v2 = (0.5, 1.25, 2)
# v1 + v2 = (2.5, 4.25, 3)
# v1 - v2 = (1.5, 1.75, -1)
# v1 * v2 = 6.75
# v1 x v2 = (4.75, -3.5, 1.0)

# Ayuda de DeepSeek-r1(22/03/2025):
# --------------------------------
# Áreas de la ciencia donde se usa este tipo de código:
# -----------------------------------------------------

# Física: Para calcular fuerzas, velocidades, aceleraciones y otros fenómenos físicos en 2D y 3D.

# Ingeniería: En diseño mecánico, análisis estructural y simulaciones de fluidos.

# Computación gráfica: Para renderizar objetos en 3D, animaciones y videojuegos.

# Robótica: Para modelar movimientos y trayectorias de robots.

# Matemáticas aplicadas: En álgebra lineal, geometría y cálculo vectorial.

# Machine Learning: En la manipulación de datos multidimensionales y operaciones matriciales.