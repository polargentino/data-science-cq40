"""
https://chat.qwenlm.ai/

Explicación del Código

1-Entrada y Extracción de Datos :
---------------------------------

Se divide la hora de inicio (start_time) en horas, minutos y período (AM/PM).
Se convierte la hora de inicio a formato de 24 horas para facilitar los cálculos.
Se extrae la duración en horas y minutos.

2-Cálculo del Tiempo Total :
----------------------------

Se calcula el tiempo total en minutos sumando los minutos de la hora de inicio y la duración.

3-Conversión a Horas y Minutos :
--------------------------------

Se calculan las nuevas horas y minutos utilizando operaciones de división y módulo.
Se determina si el período es AM o PM basado en las nuevas horas.

4-Días Pasados :
----------------

Se calcula cuántos días han pasado dividiendo el tiempo total en minutos entre el número de 
minutos en un día (1440).

4-Formateo del Resultado :
--------------------------
Se construye el resultado con el formato adecuado.
Si se proporciona un día de inicio, se calcula el nuevo día de la semana.
Se agrega información sobre los días pasados si es necesario.

*-Conclusión:
-------------
Esta implementación cumple con todas las reglas y condiciones especificadas. 
Es robusta, maneja correctamente los cambios de día y los días de la semana, 
y produce el formato deseado. ¡Espero que esta solución sea útil! 😊

"""


def add_time(start_time, duration, start_day=None):
    # Diccionario para mapear días de la semana (en minúsculas)
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Extraer la hora de inicio y el período (AM/PM)
    time, period = start_time.split()
    start_hour, start_minute = map(int, time.split(":"))
    
    # Convertir a formato de 24 horas
    if period.upper() == "PM" and start_hour != 12:
        start_hour += 12
    elif period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Extraer la duración
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Calcular el tiempo total en minutos
    total_minutes = start_hour * 60 + start_minute + duration_hours * 60 + duration_minutes

    # Calcular las nuevas horas y minutos
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Determinar si es AM o PM
    period = "AM"
    if new_hour >= 12:
        period = "PM"
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Calcular el número de días pasados
    days_passed = total_minutes // (24 * 60)

    # Formatear el resultado
    result = f"{new_hour}:{new_minute:02d} {period}"

    # Agregar el día de la semana si se proporciona
    if start_day:
        start_day = start_day.lower()
        if start_day in days_of_week:
            current_day_index = days_of_week.index(start_day)
            new_day_index = (current_day_index + days_passed) % 7
            new_day = days_of_week[new_day_index].capitalize()
            result += f", {new_day}"

    # Agregar información sobre los días pasados
    if days_passed == 1:
        result += " (next day)"
    elif days_passed > 1:
        result += f" ({days_passed} days later)"

    return result

# Ejemplos de Uso:

# Ejemplo 1: Sin Día de Inicio
print(add_time("3:00 PM", "3:10"))
# Salidas: 
# 6:10 PM

# Ejemplo 2: Con Día de Inicio
print(add_time("11:30 AM", "2:32", "Monday"))
# Salidas:
# 2:02 PM, Monday

# Ejemplo 3: Cambio de Día
print(add_time("10:10 PM", "3:30"))
# Salidas:
# 1:40 AM (next day)

# Ejemplo 4: Múltiples Días y Día de Inicio
print(add_time("11:43 PM", "24:20", "tueSday"))
# Salidas:
# 12:03 AM, Thursday (2 days later)

# Ejemplo 5: Gran Duración
print(add_time("6:30 PM", "205:12"))
# Salidas:
# 7:42 AM (9 days later)

# Manejo de Errores
# El código asume que las entradas son válidas según las reglas del 
# problema. No se realizan validaciones adicionales porque no es necesario 
# importar bibliotecas ni manejar casos inválidos.
