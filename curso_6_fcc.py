import re  # Importa el módulo re para trabajar con expresiones regulares
import secrets  # Importa el módulo secrets para generar números aleatorios seguros
import string  # Importa el módulo string para acceder a constantes de caracteres

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Genera una contraseña aleatoria segura basada en criterios especificados.

    Parámetros:
    length (int): La longitud total de la contraseña. Por defecto es 16.
    nums (int): El número mínimo de dígitos requeridos en la contraseña. Por defecto es 1.
    special_chars (int): El número mínimo de caracteres especiales requeridos en la contraseña. 
    Por defecto es 1.
    uppercase (int): El número mínimo de letras mayúsculas requeridas en la contraseña. 
    Por defecto es 1.
    lowercase (int): El número mínimo de letras minúsculas requeridas en la contraseña. 
    Por defecto es 1.

    Retorna:
    str: Una contraseña generada aleatoriamente que cumple con los criterios especificados.
    """
    
    # Define los posibles caracteres para la contraseña
    letters = string.ascii_letters  # Contiene tanto letras mayúsculas como minúsculas
    digits = string.digits           # Contiene los dígitos del 0 al 9
    symbols = string.punctuation     # Contiene caracteres especiales (por ejemplo, !, @, #, etc.)

    # Combina todos los caracteres en una sola cadena
    all_characters = letters + digits + symbols

    while True:  # Inicia un bucle que continuará hasta que se genere una contraseña válida
        password = ''  # Inicializa una cadena vacía para la contraseña
        
        # Genera la contraseña seleccionando caracteres aleatorios
        for _ in range(length):  # Repite el proceso 'length' veces
            password += secrets.choice(all_characters)  # Elige un carácter aleatorio de todos los caracteres

        # Define las restricciones para la contraseña
        constraints = [
            (nums, r'\d'),  # Verifica la cantidad de dígitos
            (special_chars, fr'[{symbols}]'),  # Verifica la cantidad de caracteres especiales
            (uppercase, r'[A-Z]'),  # Verifica la cantidad de letras mayúsculas
            (lowercase, r'[a-z]')   # Verifica la cantidad de letras minúsculas
        ]

        # Verifica si la contraseña generada cumple con todas las restricciones
        if all(
            constraint <= len(re.findall(pattern, password))  # Cuenta las ocurrencias de cada tipo
            for constraint, pattern in constraints
        ):
            break  # Si se cumplen todas las restricciones, sale del bucle

    return password  # Devuelve la contraseña generada

# Este bloque solo se ejecutará si el script se ejecuta directamente
if __name__ == '__main__':
    new_password = generate_password()  # Genera una nueva contraseña
    print('Generated password:', new_password)  # Imprime la contraseña generada

# Salidas: 
# Generated password: -Uh<`&6`h5p_C(8g
# Generated password: !jq0'XJg.GkE-;-B 
# Generated password: 8Lh^mh2ozdDQP<zA
# Generated password: Q!icG^/qhiMv3m|d
# Generated password: 6UW;?YBLvorT9MWi