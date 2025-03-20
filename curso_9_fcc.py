def merge_sort(array):
    """
    Ordena un arreglo utilizando el algoritmo de ordenamiento por mezcla (merge sort).

    Parámetros:
        array (list): El arreglo que se desea ordenar.

    Descripción:
        Este algoritmo divide el arreglo en dos mitades, ordena cada mitad recursivamente
        y luego combina las dos mitades ordenadas en un solo arreglo ordenado.

        Arreglo desordenado: 
[4, 10, 6, 14, 2, 1, 8, 5]
Arreglo ordenado: [1, 2, 4, 5, 6, 8, 10, 14]
    """
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(array) <= 1:
        return
    
    # Paso 1: Dividir el arreglo en dos mitades
    middle_point = len(array) // 2  # Encontrar el punto medio del arreglo
    left_part = array[:middle_point]  # Mitad izquierda del arreglo
    right_part = array[middle_point:]  # Mitad derecha del arreglo

    # Paso 2: Ordenar recursivamente las dos mitades
    merge_sort(left_part)  # Ordenar la mitad izquierda
    merge_sort(right_part)  # Ordenar la mitad derecha

    # Paso 3: Combinar las dos mitades ordenadas
    left_array_index = 0  # Índice para recorrer la mitad izquierda
    right_array_index = 0  # Índice para recorrer la mitad derecha
    sorted_index = 0  # Índice para recorrer el arreglo original

    # Combinar las dos mitades mientras haya elementos en ambas
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            # Si el elemento de la mitad izquierda es menor, colocarlo en el arreglo original
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1  # Mover al siguiente elemento de la mitad izquierda
        else:
            # Si el elemento de la mitad derecha es menor, colocarlo en el arreglo original
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1  # Mover al siguiente elemento de la mitad derecha
        sorted_index += 1  # Mover al siguiente índice del arreglo original

    # Paso 4: Copiar los elementos restantes de la mitad izquierda (si los hay)
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Paso 5: Copiar los elementos restantes de la mitad derecha (si los hay)
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Arreglo inicial desordenado
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Imprimir el arreglo desordenado
    print('Arreglo desordenado: ')
    print(numbers)
    
    # Llamar a la función merge_sort para ordenar el arreglo
    merge_sort(numbers)
    
    # Imprimir el arreglo ordenado
    print('Arreglo ordenado: ' + str(numbers))

# Salidas:
# Arreglo desordenado: 
# [4, 10, 6, 14, 2, 1, 8, 5]
# Arreglo ordenado: [1, 2, 4, 5, 6, 8, 10, 14]

# Ayuda de : DeepSeek-r1 20/03/2025