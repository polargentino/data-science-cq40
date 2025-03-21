"""
Un árbol de búsqueda binaria (BST) es una estructura de datos común donde los datos se 
ordenan jerárquicamente.

En este proyecto, aprenderás a construir tu propia BST y a realizar un recorrido en orden. 
También aprenderás operaciones clave como inserción, búsqueda y eliminación.
"""
class TreeNode:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.

    Atributos:
        key (int): El valor almacenado en el nodo.
        left (TreeNode): Referencia al hijo izquierdo del nodo.
        right (TreeNode): Referencia al hijo derecho del nodo.
    """

    def __init__(self, key):
        """
        Inicializa un nodo con un valor específico.

        Parámetros:
            key (int): El valor que se almacenará en el nodo.
        """
        self.key = key  # Valor del nodo
        self.left = None  # Hijo izquierdo (inicialmente vacío)
        self.right = None  # Hijo derecho (inicialmente vacío)

    def __str__(self):
        """
        Devuelve una representación en cadena del nodo.

        Returns:
            str: El valor del nodo convertido a cadena.
        """
        return str(self.key)


class BinarySearchTree:
    """
    Clase que representa un árbol binario de búsqueda (BST).

    Un BST es una estructura de datos que permite almacenar y organizar datos de manera eficiente.
    Cada nodo tiene un valor y dos hijos: izquierdo (menor) y derecho (mayor).
    Esto permite realizar operaciones como inserción, búsqueda y eliminación en tiempo logarítmico.

    Atributos:
        root (TreeNode): La raíz del árbol.
    """

    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.root = None  # La raíz del árbol (inicialmente vacía)

    def _insert(self, node, key):
        """
        Método auxiliar para insertar un valor en el árbol.

        Parámetros:
            node (TreeNode): El nodo actual en el que se está trabajando.
            key (int): El valor que se desea insertar.

        Returns:
            TreeNode: El nodo actualizado.
        """
        if node is None:  # Si el nodo actual está vacío, crea un nuevo nodo
            return TreeNode(key)

        if key < node.key:  # Si el valor es menor, inserta en el subárbol izquierdo
            node.left = self._insert(node.left, key)
        elif key > node.key:  # Si el valor es mayor, inserta en el subárbol derecho
            node.right = self._insert(node.right, key)

        return node  # Devuelve el nodo actualizado

    def insert(self, key):
        """
        Inserta un valor en el árbol.

        Parámetros:
            key (int): El valor que se desea insertar.
        """
        self.root = self._insert(self.root, key)  # Llama al método auxiliar

    def _search(self, node, key):
        """
        Método auxiliar para buscar un valor en el árbol.

        Parámetros:
            node (TreeNode): El nodo actual en el que se está trabajando.
            key (int): El valor que se desea buscar.

        Returns:
            TreeNode: El nodo que contiene el valor, o None si no se encuentra.
        """
        if node is None or node.key == key:  # Si el nodo está vacío o contiene el valor
            return node

        if key < node.key:  # Si el valor es menor, busca en el subárbol izquierdo
            return self._search(node.left, key)
        return self._search(node.right, key)  # Si el valor es mayor, busca en el subárbol derecho

    def search(self, key):
        """
        Busca un valor en el árbol.

        Parámetros:
            key (int): El valor que se desea buscar.

        Returns:
            TreeNode: El nodo que contiene el valor, o None si no se encuentra.
        """
        return self._search(self.root, key)  # Llama al método auxiliar

    def _delete(self, node, key):
        """
        Método auxiliar para eliminar un valor del árbol.

        Parámetros:
            node (TreeNode): El nodo actual en el que se está trabajando.
            key (int): El valor que se desea eliminar.

        Returns:
            TreeNode: El nodo actualizado.
        """
        if node is None:  # Si el nodo está vacío, no hay nada que eliminar
            return node

        if key < node.key:  # Si el valor es menor, elimina en el subárbol izquierdo
            node.left = self._delete(node.left, key)
        elif key > node.key:  # Si el valor es mayor, elimina en el subárbol derecho
            node.right = self._delete(node.right, key)
        else:  # Si se encuentra el valor
            if node.left is None:  # Si no tiene hijo izquierdo, reemplaza con el derecho
                return node.right
            elif node.right is None:  # Si no tiene hijo derecho, reemplaza con el izquierdo
                return node.left

            # Si tiene dos hijos, encuentra el mínimo en el subárbol derecho
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)  # Elimina el mínimo

        return node  # Devuelve el nodo actualizado

    def delete(self, key):
        """
        Elimina un valor del árbol.

        Parámetros:
            key (int): El valor que se desea eliminar.
        """
        self.root = self._delete(self.root, key)  # Llama al método auxiliar

    def _min_value(self, node):
        """
        Encuentra el valor mínimo en un subárbol.

        Parámetros:
            node (TreeNode): El nodo raíz del subárbol.

        Returns:
            int: El valor mínimo.
        """
        while node.left is not None:  # Recorre hacia la izquierda hasta encontrar el mínimo
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        """
        Método auxiliar para recorrer el árbol en orden (inorden).

        Parámetros:
            node (TreeNode): El nodo actual en el que se está trabajando.
            result (list): Una lista para almacenar los valores en orden.
        """
        if node:
            self._inorder_traversal(node.left, result)  # Recorre el subárbol izquierdo
            result.append(node.key)  # Agrega el valor del nodo actual
            self._inorder_traversal(node.right, result)  # Recorre el subárbol derecho

    def inorder_traversal(self):
        """
        Recorre el árbol en orden (inorden) y devuelve una lista con los valores.

        Returns:
            list: Una lista con los valores del árbol en orden ascendente.
        """
        result = []
        self._inorder_traversal(self.root, result)  # Llama al método auxiliar
        return result


# Crear el árbol binario de búsqueda
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insertar nodos en el árbol
for node in nodes:
    bst.insert(node)

# Buscar un nodo en el árbol
print('Search for 80:', bst.search(80))

# Recorrido inorden antes de eliminar
print("Inorder traversal:", bst.inorder_traversal())

# Eliminar el nodo con valor 40
bst.delete(40)

# Buscar el nodo eliminado
print("Search for 40:", bst.search(40))

# Imprimir el recorrido inorden después de eliminar 40
print('Inorder traversal after deleting 40:', bst.inorder_traversal())

# Salidas: 
# -------
# Search for 80: 80
# Inorder traversal: [20, 30, 40, 50, 60, 70, 80]
# Search for 40: None
# Inorder traversal after deleting 40: [20, 30, 50, 60, 70, 80]

# Ayuda de DeepSeek-r1:(21/03/2025)
# --------------------
# Explicación Detallada
# 1. Clase TreeNode:
# -----------------
# Representa un nodo en el árbol binario de búsqueda.

# Cada nodo tiene:

# Un valor (key).

# Un hijo izquierdo (left).

# Un hijo derecho (right).

# 2. Clase BinarySearchTree:
# --------------------------
# Representa el árbol binario de búsqueda.

# Contiene métodos para:

# Insertar valores (insert).

# Buscar valores (search).

# Eliminar valores (delete).

# Recorrer el árbol en orden (inorder_traversal).

# 3. Métodos Principales:
# -----------------------
# insert: Añade un valor al árbol.

# search: Busca un valor en el árbol.

# delete: Elimina un valor del árbol.

# inorder_traversal: Devuelve una lista con los valores del árbol en orden ascendente.

# 4. ¿Para qué sirve un árbol binario de búsqueda?
# ------------------------------------------------
# Es una estructura de datos eficiente para almacenar y organizar datos.

# Se utiliza en aplicaciones como:

# Bases de datos para indexar información.

# Motores de búsqueda para organizar palabras clave.

# Algoritmos de compresión de datos.

# 5. ¿Cómo nos ayuda la inteligencia artificial?
# -----------------------------------------------
# La IA puede ayudarnos a escribir código incluso si no sabemos todo sobre Python.

# Con el tiempo, al practicar y usar herramientas como esta, aprendemos más y mejoramos nuestras habilidades.

