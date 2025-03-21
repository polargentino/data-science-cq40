"""
Los algoritmos son procedimientos paso a paso que los desarrolladores utilizan para realizar 
cálculos y resolver problemas computacionales.

En este proyecto, aprenderá a utilizar funciones, bucles, declaraciones condicionales y 
comprensiones de diccionario para implementar un algoritmo de ruta más corta.


En matemáticas y ciencias de la computación, un grafo (del griego grafos: dibujo, imagen)1​ 
es un conjunto de objetos llamados vértices o nodos unidos por enlaces llamados aristas 
o arcos, que permiten representar relaciones binarias entre elementos de un conjunto.
2​Son objeto de estudio de la teoría de grafos.3​
"""


# Definición del grafo como un diccionario
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],  # Desde A se puede ir a B (5), C (3) y E (11)
    'B': [('A', 5), ('C', 1), ('F', 2)],   # Desde B se puede ir a A (5), C (1) y F (2)
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],  # Desde C se puede ir a A (3), B (1), D (1) y E (5)
    'D': [('C', 1), ('E', 9), ('F', 3)],   # Desde D se puede ir a C (1), E (9) y F (3)
    'E': [('A', 11), ('C', 5), ('D', 9)],  # Desde E se puede ir a A (11), C (5) y D (9)
    'F': [('B', 2), ('D', 3)]               # Desde F se puede ir a B (2) y D (3)
}

def shortest_path(graph, start, target=''):
    """
    Calcula la ruta más corta en un grafo utilizando el algoritmo de Dijkstra.
    El algoritmo de Dijkstra, también llamado algoritmo de caminos mínimos, es 
    un algoritmo para la determinación del camino más corto, dado un vértice origen, 
    hacia el resto de los vértices en un grafo que tiene pesos en cada arista. 
    Su nombre alude a Edsger Dijkstra, científico de la computación de los Países Bajos 
    que lo concibió en 1956 y lo publicó por primera vez en 1959.1​2​

    Parámetros:
    graph (dict): Un diccionario que representa el grafo, donde las claves son nodos
                  y los valores son listas de tuplas (nodo vecino, distancia).
    start (str): El nodo de inicio desde el cual se calcularán las distancias.
    target (str): El nodo objetivo al que se desea llegar. Si se deja vacío, se imprimirán
                  las distancias a todos los nodos.

    Retorna:
    tuple: Un par que contiene dos diccionarios:
           - distancias: Un diccionario con la distancia más corta desde el nodo de inicio a cada nodo.
           - paths: Un diccionario con la ruta más corta desde el nodo de inicio a cada nodo.
    """
    
    # Lista de nodos no visitados
    unvisited = list(graph)
    
    # Inicializa las distancias: 0 para el nodo de inicio, infinito para los demás
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Inicializa las rutas: cada nodo tiene una lista vacía
    paths = {node: [] for node in graph}
    
    # Agrega el nodo de inicio a su propia ruta
    paths[start].append(start)
    
    # Mientras haya nodos no visitados
    while unvisited:
        # Encuentra el nodo no visitado con la distancia más corta
        current = min(unvisited, key=distances.get)
        
        # Itera sobre los nodos vecinos del nodo actual
        for node, distance in graph[current]:
            # Si se encuentra un camino más corto hacia el nodo vecino
            if distance + distances[current] < distances[node]:
                # Actualiza la distancia al nodo vecino
                distances[node] = distance + distances[current]
                
                # Si ya hay una ruta hacia el nodo vecino
                if paths[node] and paths[node][-1] == node:
                    # Copia la ruta actual
                    paths[node] = paths[current][:]
                else:
                    # Extiende la ruta hacia el nodo vecino
                    paths[node].extend(paths[current])
                
                # Agrega el nodo vecino a la ruta
                paths[node].append(node)
        
        # Marca el nodo actual como visitado
        unvisited.remove(current)
    
    # Determina qué nodos imprimir: solo el objetivo si se proporciona, o todos los nodos
    targets_to_print = [target] if target else graph
    
    # Itera sobre los nodos a imprimir
    for node in targets_to_print:
        if node == start:
            continue  # No imprimir la distancia al nodo de inicio
        # Imprime la distancia y la ruta hacia el nodo
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Retorna las distancias y las rutas
    return distances, paths

# Llamada a la función para calcular la ruta más corta desde 'A' hasta 'F'
shortest_path(my_graph, 'A', 'F')

# Salidas: 
# A-F distance: 6
# Path: A -> C -> B -> F