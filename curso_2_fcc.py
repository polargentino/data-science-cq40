def verify_card_number(card_number):
    """
    Verifica si un número de tarjeta es válido utilizando el algoritmo de Luhn.

    Parámetros:
        card_number (str): El número de tarjeta a verificar.

    Retorna:
        bool: True si el número de tarjeta es válido, False en caso contrario.
    """
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    # Se eliminó la llamada a print(total)
    return total % 10 == 0

def main():
    """
    Función principal que verifica si un número de tarjeta es válido.
    """
    # Cambiar el número de tarjeta a uno válido
    card_number = '4111-1111-4555-1142'  # Número de tarjeta válido
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Llamar a la función principal
main()

# Salidas: 
# VALID!