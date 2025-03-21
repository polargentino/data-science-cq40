def convert_to_snake_case(pascal_or_camel_cased_string):
    """
La comprensión de listas es una forma de construir una nueva lista de Python a partir 
de tipos iterables: listas, tuplas y cadenas. Todo ello sin usar un bucle for ni el 
método de lista `.append()`.

En este proyecto, escribirás un programa que toma una cadena formateada en Camel Case o 
Pascal Case y luego la convierte a Snake Case.

El proyecto consta de dos fases: primero, usarás un bucle for para implementar el programa. 
Luego, aprenderás a usar la comprensión de listas en lugar de un bucle para lograr los mismos 
resultados.


    Convierte una cadena de texto de Pascal Case o Camel Case a Snake Case.
    
    Esta función toma una cadena en formato Pascal Case (ej. 'PascalCase') o
    Camel Case (ej. 'camelCase') y la convierte a formato Snake Case (ej. 'snake_case').
    
    El proceso de conversión incluye:
    1. Identificar las letras mayúsculas en la cadena de entrada
    2. Reemplazar cada letra mayúscula con un guión bajo seguido de su versión en minúscula
    3. Eliminar cualquier guión bajo al inicio o final de la cadena
    
    Args:
        pascal_or_camel_cased_string (str): Una cadena en formato Pascal Case o Camel Case
        
    Returns:
        str: La cadena de entrada convertida a formato Snake Case
        
    Ejemplos:
        >>> convert_to_snake_case('camelCaseString')
        'camel_case_string'
        >>> convert_to_snake_case('PascalCaseString')
        'pascal_case_string'
    """
    # Usar comprensión de lista para procesar cada carácter en la cadena de entrada
    # Para cada carácter en mayúscula, añadir un guión bajo antes de él y convertirlo a minúscula
    # Para todos los demás caracteres, mantenerlos como están
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Si el carácter está en mayúscula, añadir '_' y convertir a minúscula
        else char                            # De lo contrario, mantener el carácter como está
        for char in pascal_or_camel_cased_string  # Iterar a través de cada carácter en la cadena de entrada
    ]
    
    # Unir todos los caracteres de la lista en una sola cadena
    # Eliminar cualquier guión bajo al inicio o final para limpiar el resultado
    # (Esto maneja casos donde la cadena de entrada comienza con una letra mayúscula)
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # Probar la función con una cadena en Pascal Case
    # La cadena 'IAmAPascalCasedString' debe convertirse a 'i_am_a_pascal_cased_string'
    print(convert_to_snake_case('IAmAPascalCasedString'))


# Ejecutar la función principal cuando se ejecuta el script
main()

# Salidas: 
# i_am_a_pascal_cased_string
# Ayuda de Claude 3.7 Sonnet