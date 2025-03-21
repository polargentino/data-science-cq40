# Texto cifrado y clave personalizada
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'  # Clave modificada a 'happycoding'

def vigenere(message, key, direction=1):
    """
Python es un lenguaje de programación poderoso y popular ampliamente utilizado 
para la ciencia de datos, visualización de datos, desarrollo web, desarrollo de juegos, 
aprendizaje automático y más.

En este proyecto, aprenderás conceptos fundamentales de programación en Python, 
como variables, funciones, bucles y sentencias condicionales. Los usarás para codificar 
tus primeros programas.


    Implementa el cifrado o descifrado de Vigenère.(Herramienta para decodificar / 
    codificar Vigenere automáticamente. El Cifrado de Vigenere es un sistema de cifrado 
    de sustitución polialfabético que utiliza una clave y una tabla de doble entrada. 
    https://www.dcode.fr/cifrado-vigenere)

    Parámetros:
        message (str): El mensaje a cifrar o descifrar.
        key (str): La clave utilizada para el cifrado/descifrado.
        direction (int): 1 para cifrar, -1 para descifrar.

    Retorna:
        str: El mensaje cifrado o descifrado.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Alfabeto utilizado para el cifrado
    final_message = ''

    for char in message.lower():  # Convertir el mensaje a minúsculas para uniformidad
        if not char.isalpha():  # Si el carácter no es una letra, añadirlo sin cambios
            final_message += char
        else:
            # Obtener el carácter de la clave correspondiente
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calcular el desplazamiento basado en la clave
            offset = alphabet.index(key_char)
            # Encontrar la posición del carácter en el alfabeto
            index = alphabet.find(char)
            # Calcular la nueva posición después de aplicar el cifrado/descifrado
            new_index = (index + offset * direction) % len(alphabet)
            # Añadir el nuevo carácter al mensaje final
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    """
    Cifra un mensaje utilizando el cifrado de Vigenère.

    Parámetros:
        message (str): El mensaje a cifrar.
        key (str): La clave para el cifrado.

    Retorna:
        str: El mensaje cifrado.
    """
    return vigenere(message, key)

def decrypt(message, key):
    """
    Descifra un mensaje utilizando el cifrado de Vigenère.

    Parámetros:
        message (str): El mensaje a descifrar.
        key (str): La clave para el descifrado.

    Retorna:
        str: El mensaje descifrado.
    """
    return vigenere(message, key, -1)

def check_decryption(encrypted_text, key, correct_key):
    """
    Verifica si la clave es correcta y realiza el descifrado.

    Parámetros:
        encrypted_text (str): El texto cifrado.
        key (str): La clave proporcionada para el descifrado.
        correct_key (str): La clave correcta para el descifrado.

    Retorna:
        None: Imprime el resultado del descifrado o un mensaje de error.
    """
    if key == correct_key:  # Verificar si la clave es correcta
        decryption = decrypt(encrypted_text, key)
        print(f'\nDecrypted text: {decryption}\n')
        print("Paso 96 Aprobado")
        print("With that, your cipher project is complete.")
    else:
        print("\nWait a minute! You cannot decrypt anything with the wrong key. Try with 'happycoding'.")

# Clave correcta para el descifrado
correct_key = 'happycoding'

# Proceso de descifrado
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
check_decryption(text, custom_key, correct_key)

# Intentar con una clave incorrecta para demostrar el mensaje de error
wrong_key = 'python'
print("\nTrying with the wrong key...")
print(f'Key: {wrong_key}')
check_decryption(text, wrong_key, correct_key)

# Salidas:(DeepSeek-r1)
# Encrypted text: mrttaqrhknsw ih puggrur
# Key: happycoding

# Decrypted text: freecodecamp is awesome

# Paso 96 Aprobado
# With that, your cipher project is complete.

# Trying with the wrong key...
# Key: python

# Wait a minute! You cannot decrypt anything with the wrong key. Try with 'happycoding'.
                                                                                      