"""
https://chat.qwenlm.ai/

Explicación del Código

1-Validaciones Iniciales :
-------------------------
Se verifica que no haya más de 5 problemas.
Cada problema se divide en operandos y operador.
Se asegura que el operador sea '+' o '-'.
Se valida que los operandos contengan solo dígitos.
Se comprueba que los operandos no tengan más de 4 dígitos.

2-Formateo de Líneas :
-------------------
Para cada problema, se calcula la longitud máxima necesaria para alinear los números.
Se construyen las tres líneas principales: la primera línea (operando superior), la 
segunda línea (operador y operando inferior), y la línea de guiones.
Si show_answers es True, se calcula y agrega la cuarta línea con las respuestas.

3-Unión de Problemas :
----------------------
Las líneas se unen con 4 espacios (' ') entre problemas para mantener el formato correcto.

4-Retorno del Resultado :
-------------------------
El resultado final incluye las líneas formateadas y, opcionalmente, las respuestas si show_answers es True.

*-Conclusión:
--------------
Esta implementación cumple con todas las reglas y condiciones especificadas. Es robusta, maneja 
errores correctamente y produce el formato deseado tanto para problemas sin respuestas como para 
aquellos donde se muestran las soluciones. ¡Espero que esta solución sea útil! 😊

"""

def arithmetic_arranger(problems, show_answers=False):
    # Regla 1: No más de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Variables para almacenar las líneas del resultado
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        # Dividir el problema en sus componentes
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem should have exactly two operands and one operator."
        
        operand1, operator, operand2 = parts

        # Regla 2: Solo operadores '+' o '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Regla 3: Operandos deben contener solo dígitos
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Regla 4: Operandos no pueden tener más de 4 dígitos
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcular la longitud máxima para alinear los números
        max_length = max(len(operand1), len(operand2)) + 2  # +2 para el operador y el espacio

        # Construir cada línea
        first_line.append(operand1.rjust(max_length))
        second_line.append(operator + operand2.rjust(max_length - 1))
        dashes_line.append('-' * max_length)

        # Si se solicitan las respuestas, calcularlas
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answers_line.append(answer.rjust(max_length))

    # Unir las líneas con 4 espacios entre problemas
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dashes_line)

    # Agregar las respuestas si es necesario
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_line)

    return arranged_problems

# Ejemplo 1: Sin Mostrar Respuestas
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) 
# Salidas:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----


# Ejemplo 2: Mostrando Respuestas
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474


# Manejo de Errores:

# 1-Demasiados Problemas :
print(arithmetic_arranger(["1 + 2", "3 + 4", "5 + 6", "7 + 8", "9 + 10", "11 + 12"]))
# Salidas:
# Error: Too many problems.

# 2-Operador Inválido :
print(arithmetic_arranger(["1 * 2"]))
# Salidas:
# Error: Operator must be '+' or '-'.

# 3-Operandos No Numéricos :
print(arithmetic_arranger(["1 + abc"]))
# Salidas:
# Error: Numbers must only contain digits.

# 4-Operandos Demasiado Largos :
print(arithmetic_arranger(["12345 + 6"]))
# Salidas:
# Error: Numbers cannot be more than four digits.
