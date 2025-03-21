NUMBER_OF_DISKS = 5  # Número de discos en la Torre de Hanoi
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Torre A: Contiene los discos iniciales [5, 4, 3, 2, 1]
B = []  # Torre B: Torre auxiliar, inicialmente vacía
C = []  # Torre C: Torre objetivo, inicialmente vacía

def move(n, source, auxiliary, target):
    """
La recursión es un enfoque de programación que permite resolver problemas computacionales 
complicados con solo un poco de código.

En este proyecto, comenzarás con un enfoque basado en bucles para resolver el rompecabezas 
matemático de la Torre de Hanói. Después, aprenderás a implementar una solución recursiva.


    Mueve n discos desde la torre de origen (source) a la torre de destino (target),
    utilizando una torre auxiliar (auxiliary), siguiendo las reglas de la Torre de Hanoi.

    Parámetros:
        n (int): Número de discos a mover.
        source (list): Torre de origen (lista que representa los discos).
        auxiliary (list): Torre auxiliar (lista que representa los discos).
        target (list): Torre de destino (lista que representa los discos).

    La función utiliza recursividad para resolver el problema de la Torre de Hanoi.

    # Estado inicial:
[5, 4, 3, 2, 1] [] [] 

# Después de mover el disco 1 de A a C:
[5, 4, 3, 2] [] [1] 

# Después de mover el disco 2 de A a B:
[5, 4, 3] [2] [1] 

# Después de mover el disco 1 de C a B:
[5, 4, 3] [2, 1] [] 

# Después de mover el disco 3 de A a C:
[5, 4] [2, 1] [3] 

# Después de mover el disco 1 de B a A:
[5, 4, 1] [2] [3] 

# Después de mover el disco 2 de B a C:
[5, 4, 1] [] [3, 2] 

# Después de mover el disco 1 de A a C:
[5, 4] [] [3, 2, 1] 

# ... (y así sucesivamente hasta que todos los discos estén en C)
    """
    # Caso base: Si no hay discos para mover, retornar sin hacer nada
    if n <= 0:
        return
    
    # Paso 1: Mover n-1 discos de la torre de origen (source) a la torre auxiliar (auxiliary),
    # utilizando la torre de destino (target) como auxiliar temporal.
    # Esto deja el disco más grande (el enésimo disco) en la torre de origen.
    move(n - 1, source, target, auxiliary)
    
    # Paso 2: Mover el enésimo disco (el más grande) de la torre de origen (source) a la torre de destino (target).
    # Esto se hace simplemente moviendo el último elemento de la lista `source` a la lista `target`.
    target.append(source.pop())
    
    # Paso 3: Mostrar el progreso actual de las torres.
    # Esto permite visualizar cómo se mueven los discos en cada paso.
    print(A, B, C, '\n')
    
    # Paso 4: Mover los n-1 discos que quedaron en la torre auxiliar (auxiliary) a la torre de destino (target),
    # utilizando la torre de origen (source) como auxiliar temporal.
    # Esto completa el movimiento de todos los discos.
    move(n - 1, auxiliary, source, target)
              
# Iniciar la llamada recursiva desde la torre A (origen) a la torre C (destino), utilizando B como auxiliar.
move(NUMBER_OF_DISKS, A, B, C)

# Explicación detallada de la recursividad: (Ayuda de DeepSeek-r1) 20/03/2025

# Caso base:

# Si n <= 0, la función retorna inmediatamente. Esto evita que la recursividad continúe indefinidamente.

# Es el punto de parada de la recursión.

# Paso 1: Mover n-1 discos de source a auxiliary:

# Para mover n discos de source a target, primero debemos mover n-1 discos de source a auxiliary.

# Esto se hace llamando recursivamente a move(n - 1, source, target, auxiliary).

# Aquí, target actúa como torre auxiliar temporal.

# Paso 2: Mover el enésimo disco de source a target:

# Una vez que los n-1 discos están en auxiliary, el disco más grande (el enésimo disco) se mueve directamente de source a target.

# Esto se hace con target.append(source.pop()).

# Paso 3: Mostrar el progreso:

# Después de mover el enésimo disco, se imprime el estado actual de las torres (A, B, C).

# Esto permite visualizar cómo se mueven los discos en cada paso.

# Paso 4: Mover n-1 discos de auxiliary a target:

# Finalmente, los n-1 discos que quedaron en auxiliary se mueven a target, utilizando source como torre auxiliar temporal.

# Esto se hace llamando recursivamente a move(n - 1, auxiliary, source, target).

# Salidas: 
# [5, 4, 3, 2] [] [1] 

# [5, 4, 3] [2] [1] 

# [5, 4, 3] [2, 1] [] 

# [5, 4] [2, 1] [3] 

# [5, 4, 1] [2] [3] 

# [5, 4, 1] [] [3, 2] 

# [5, 4] [] [3, 2, 1] 

# [5] [4] [3, 2, 1] 

# [5] [4, 1] [3, 2] 

# [5, 2] [4, 1] [3] 

# [5, 2, 1] [4] [3] 

# [5, 2, 1] [4, 3] [] 

# [5, 2] [4, 3] [1] 

# [5] [4, 3, 2] [1] 

# [5] [4, 3, 2, 1] [] 

# [] [4, 3, 2, 1] [5] 

# [1] [4, 3, 2] [5] 

# [1] [4, 3] [5, 2] 

# [] [4, 3] [5, 2, 1] 

# [3] [4] [5, 2, 1] 

# [3] [4, 1] [5, 2] 

# [3, 2] [4, 1] [5] 

# [3, 2, 1] [4] [5] 

# [3, 2, 1] [] [5, 4] 

# [3, 2] [] [5, 4, 1] 

# [3] [2] [5, 4, 1] 

# [3] [2, 1] [5, 4] 

# [] [2, 1] [5, 4, 3] 

# [1] [2] [5, 4, 3] 

# [1] [] [5, 4, 3, 2] 

# [] [] [5, 4, 3, 2, 1] 