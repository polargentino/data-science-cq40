"""
Las clases y los objetos son conceptos importantes de programación. Estas herramientas de 
programación orientada a objetos ayudan a los desarrolladores a lograr modularidad, 
abstracción y legibilidad del código. Además, promueven la reutilización.

En este proyecto de resolución de Sudoku, aprenderá a utilizar clases y objetos para 
construir una cuadrícula de Sudoku y resolver un rompecabezas de Sudoku.

"""
# Ayuda de DeepSeek-r1: Explicación Paso a Paso
# Clase Board:

# Representa el tablero de Sudoku.

# El método __init__ inicializa el tablero.

# El método __str__ devuelve una representación legible del tablero, mostrando * para celdas vacías.

# Método find_empty_cell:

# Busca la primera celda vacía (valor 0) en el tablero.

# Devuelve la posición (fila, columna) de la celda vacía o None si no hay celdas vacías.

# Métodos de Validación:

# valid_in_row: Verifica si un número es válido en una fila.

# valid_in_col: Verifica si un número es válido en una columna.

# valid_in_square: Verifica si un número es válido en el cuadrado 3x3 que contiene la celda.

# Método is_valid:

# Combina las validaciones de fila, columna y cuadrado para determinar si un número es válido en una celda.

# Método solver:

# Utiliza backtracking para resolver el Sudoku.

# Si no hay celdas vacías, el Sudoku está resuelto.

# Prueba números del 1 al 9 en cada celda vacía y retrocede si no lleva a una solución.

# Función solve_sudoku:

# Crea una instancia de Board con el tablero proporcionado.

# Muestra el tablero inicial.

# Intenta resolver el Sudoku y muestra el resultado.

# Tablero Inicial (puzzle):

# Representa el Sudoku inicial, donde 0 indica celdas vacías.

# Llamada a solve_sudoku:

# Resuelve el Sudoku y muestra el tablero antes y después de resolverlo.



class Board:
    """
    Clase que representa un tablero de Sudoku.

    Atributos:
        board (list): Una lista de listas que representa el tablero de Sudoku.
    """

    def __init__(self, board):
        """
        Inicializa una instancia de la clase Board.

        Parámetros:
            board (list): Una lista de listas que representa el tablero de Sudoku.
        """
        self.board = board

    def __str__(self):
        """
        Devuelve una representación legible del tablero.

        Returns:
            str: Una cadena que representa el tablero, donde los números 0 se muestran como '*'.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]  # Reemplaza 0 con '*' para celdas vacías
            board_str += ' '.join(row_str)  # Une los elementos de la fila con espacios
            board_str += '\n'  # Agrega un salto de línea al final de cada fila
        return board_str

    def find_empty_cell(self):
        """
        Encuentra la primera celda vacía (valor 0) en el tablero.

        Returns:
            tuple: Una tupla (fila, columna) que representa la posición de la celda vacía.
                  Si no hay celdas vacías, devuelve None.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)  # Busca la primera celda con valor 0 en la fila
                return row, col
            except ValueError:
                pass  # Si no hay 0 en la fila, continúa con la siguiente
        return None

    def valid_in_row(self, row, num):
        """
        Verifica si un número es válido en una fila específica.

        Parámetros:
            row (int): Índice de la fila.
            num (int): Número a verificar.

        Returns:
            bool: True si el número no está en la fila, False en caso contrario.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Verifica si un número es válido en una columna específica.

        Parámetros:
            col (int): Índice de la columna.
            num (int): Número a verificar.

        Returns:
            bool: True si el número no está en la columna, False en caso contrario.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Verifica si un número es válido en el cuadrado 3x3 que contiene la celda (row, col).

        Parámetros:
            row (int): Índice de la fila.
            col (int): Índice de la columna.
            num (int): Número a verificar.

        Returns:
            bool: True si el número no está en el cuadrado, False en caso contrario.
        """
        row_start = (row // 3) * 3  # Encuentra el inicio del cuadrado 3x3 en filas
        col_start = (col // 3) * 3  # Encuentra el inicio del cuadrado 3x3 en columnas
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Verifica si un número es válido en una celda específica.

        Parámetros:
            empty (tuple): Una tupla (fila, columna) que representa la celda vacía.
            num (int): Número a verificar.

        Returns:
            bool: True si el número es válido en la fila, columna y cuadrado, False en caso contrario.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        Resuelve el Sudoku utilizando backtracking.

        Returns:
            bool: True si el Sudoku tiene solución, False en caso contrario.
        """
        if (next_empty := self.find_empty_cell()) is None:  # Si no hay celdas vacías, el Sudoku está resuelto
            return True
        for guess in range(1, 10):  # Prueba números del 1 al 9
            if self.is_valid(next_empty, guess):  # Verifica si el número es válido
                row, col = next_empty
                self.board[row][col] = guess  # Coloca el número en la celda
                if self.solver():  # Llama recursivamente a solver
                    return True
                self.board[row][col] = 0  # Si no lleva a una solución, retrocede (backtracking)
        return False


def solve_sudoku(board):
    """
    Resuelve un Sudoku dado y muestra el tablero antes y después de resolverlo.

    Parámetros:
        board (list): Una lista de listas que representa el tablero de Sudoku.

    Returns:
        Board: Una instancia de la clase Board con el Sudoku resuelto.
    """
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')  # Muestra el tablero inicial
    if gameboard.solver():  # Intenta resolver el Sudoku
        print(f'Solved puzzle:\n{gameboard}')  # Muestra el tablero resuelto
    else:
        print('The provided puzzle is unsolvable.')  # Mensaje si no tiene solución
    return gameboard


# Tablero de Sudoku inicial (0 representa celdas vacías)
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Llamada a la función para resolver el Sudoku
solve_sudoku(puzzle)

# Salidas: 

# Puzzle to solve:
# * * 2 * * 8 * * *
# * * * * * 3 7 6 2
# 4 3 * * * * 8 * *
# * 5 * * 3 * * 9 *
# * 4 * * * * * 2 6
# * * * 4 6 7 * * *
# * 8 6 7 * 4 * * *
# * * * 5 1 9 * * 8
# 1 7 * * * 6 * * 5

# Solved puzzle:
# 6 1 2 9 5 8 3 4 7
# 5 9 8 1 4 3 7 6 2
# 4 3 7 6 2 5 8 1 9
# 7 5 1 8 3 2 6 9 4
# 3 4 9 5 7 1 2 8 6
# 2 6 8 4 6 7 5 3 1
# 9 8 6 7 2 4 1 5 3
# 2 3 4 5 1 9 6 7 8
# 1 7 3 2 8 6 4 9 5