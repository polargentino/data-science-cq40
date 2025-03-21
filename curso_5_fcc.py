"""
Ayuda de Balckbox AI

Los métodos numéricos se utilizan para aproximar soluciones a problemas matemáticos que son
 difíciles o imposibles de resolver analíticamente.

En este proyecto, explorará el método numérico de bisección para encontrar la raíz 
cuadrada de un número reduciendo iterativamente el rango posible de valores que contienen 
la raíz cuadrada.
"""
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
# def square_root_bisection():
    # pass  # Aquí dejaremos la función vacía por ahora
# 1-Definición de la función: Hemos creado una función llamada square_root_bisection. 
# En Python, las funciones se definen utilizando la palabra clave def, 
# seguida del nombre de la función y paréntesis. En este caso, no hemos 
# agregado parámetros, ya que el paso indica que debemos dejarlos vacíos por ahora.

# 2-Uso de pass: La palabra clave pass se utiliza en Python como un marcador de 
# posición. Indica que no se ha implementado nada en este punto, pero la función 
# está definida y no generará un error si se llama.

# Siguiente paso:
# Una vez que tengamos la estructura básica de la función, el siguiente paso será 
# definir los parámetros que necesitaremos para el método de bisección, como el 
# número del cual queremos encontrar la raíz cuadrada y la tolerancia deseada. 
# ¿Te gustaría continuar con el siguiente paso?

# Paso 2
#Dale a la función square_root_bisection los siguientes parámetros:

# square_target: El número para el cual deseas encontrar la raíz cuadrada.
# tolerance (opcional): La diferencia aceptable entre el cuadrado del valor 
# aproximado de la raíz y el valor objetivo real (el valor predeterminado es 1e-7). 
# La tolerancia 1e-7 implica que la solución será precisa dentro de 0.0000001 del 
# valor verdadero y es una buena opción predeterminada que equilibra precisión y rendimiento.
# max_iterations (opcional): El número máximo de iteraciones a realizar (el valor 
# predeterminado es 100). Si el método no converge dentro de este límite, asumirás 
# que la solución no se ha encontrado
# def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):

# Explicación
# Parámetros de la función:

# square_target: Este es el número del cual queremos encontrar la raíz cuadrada.
# tolerance: Este es un parámetro opcional que tiene un valor predeterminado de 1e-7. 
# Esto significa que si no se proporciona un valor al llamar a la función, 
# se utilizará 1e-7 como tolerancia.
# max_iterations: Este es otro parámetro opcional que tiene un valor predeterminado de 100. 
# Si no se proporciona un valor, la función intentará encontrar la raíz cuadrada hasta un 
# máximo de 100 iteraciones.
# Uso de pass: Al igual que antes, hemos dejado la función vacía por ahora con pass, ya 
# que aún no hemos implementado la lógica del método de bisección.
# Siguiente paso
# El siguiente paso será implementar la lógica del método de bisección dentro de la 
# función para encontrar la raíz cuadrada del número dado. ¿Te gustaría que continuemos con eso?

# Paso 3
# Si el número para el cual deseas encontrar la raíz cuadrada es negativo, el código 
# debe generar un error, ya que la raíz cuadrada de un número negativo no está definida 
# en los números reales.

# Elimina la declaración pass y crea una declaración if para verificar si square_target 
# es menor que 0.

# Implementación en Python
# Ahora, vamos a actualizar la función square_root_bisection para incluir la verificación 
# del número negativo.

 # Verificar si el número es negativo
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Aquí se implementará la lógica del método de bisección más adelante

# Explicación
# Verificación de número negativo:

# Hemos agregado una declaración if que verifica si square_target es menor que 0.
# Si square_target es negativo, se genera un error utilizando raise ValueError, que 
# es una forma de indicar que ha ocurrido un error en el valor proporcionado. El mensaje 
# de error explica que la raíz cuadrada de un número negativo no está definida en los números 
# reales.
# Eliminación de pass: Hemos eliminado la declaración pass, ya que ahora hemos comenzado a 
# implementar la lógica de la función.

# Paso 5
# Crearás casos separados para cuando square_target es 0 o 1.

# Comienza creando una declaración if para verificar si square_target es igual a 1.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para incluir la verificación de 
# si square_target es igual a 1.

    # Caso cuando square_target es 1
    if square_target == 1:
        #return 1.0  # La raíz cuadrada de 1 es 1

# Explicación
# Verificación de square_target igual a 1:

# Hemos agregado una declaración if que verifica si square_target es igual a 1.
# Si es así, la función devuelve 1.0, ya que la raíz cuadrada de 1 es 1.
# Manejo de otros casos: Aunque no hemos implementado la lógica para otros casos 
# (como cuando square_target es 0 o un número mayor que 1), hemos preparado la 
# función para manejar el caso específico de square_target igual a 1.

# Paso 6
# Si square_target es igual a 1, declara una variable root y asígnale el valor 1. 
# Además, imprime el mensaje 'La raíz cuadrada de {square_target} es 1'. Recuerda 
# formatear el mensaje utilizando una f-string.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para incluir la declaración 
# de la variable root y el mensaje formateado.

        root = 1
        print(f'The square root of {square_target} is 1')

# Paso 7
# Crea una declaración elif para verificar si square_target es igual a 0. Si es así, 
# asigna el valor 0 a la variable root. Además, imprime el mensaje 'La raíz cuadrada 
# de {square_target} es 0'. Recuerda formatear el mensaje utilizando una f-string.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para incluir la verificación 
# de si square_target es igual a 0.

    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

# Paso 8
# A continuación, vas a trabajar en los casos donde square_target es un número positivo, 
# aparte de 1 o 0.

# Crea una cláusula else para manejar estos casos.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para incluir la cláusula 
# else que manejará los casos donde square_target es un número positivo distinto de 1 o 0.

    else:
        #pass

# Paso 9
# En Python, la función max() devuelve el mayor de los valores de entrada.
# Las variables low y high se utilizarán para definir el intervalo inicial donde 
# se encuentra la raíz cuadrada.

# Dentro de la cláusula else, inicializa la variable low a 0 y la variable high 
# para que sea el máximo entre 1 o square_target, ya que la raíz cuadrada de un 
# número siempre es menor o igual al número mismo.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para inicializar las 
# variables low y high dentro de la cláusula else.

        low = 0  # Inicializar low a 0
        high = max(1, square_target)  # Inicializar high al máximo entre 1 y square_target

# Explicación
# Inicialización de low: La variable low se inicializa a 0.0, que es el límite inferior del 
# intervalo donde se buscará la raíz cuadrada.

# Inicialización de high: La variable high se inicializa utilizando la función max(1.0, 
# square_target), lo que significa que high será el mayor valor entre 1.0 y square_target. 
# Esto asegura que el intervalo inicial sea correcto, ya que la raíz cuadrada de un número 
# siempre es menor o igual al número mismo.

# Placeholder: Hemos dejado un comentario indicando que aquí se implementará la lógica 
# del método de bisección más adelante.

# Paso 10
# Establece el valor de root en None, ya que en este punto no tienes un valor aproximado todavía.

# Implementación en Python
# Ahora, actualizaremos la función square_root_bisection para establecer el valor de root 
# en None dentro de la cláusula else.

        root = None  # Establecer root en None, ya que aún no tenemos un valor aproximado

# Paso 11
# Ahora reducirás repetidamente el intervalo encontrando el punto medio del intervalo actual 
# y comparando el cuadrado del punto medio con el valor objetivo.

# Para eso, dentro del bloque else, crea un bucle for que se ejecute hasta max_iterations veces.

# Para tu bucle, utiliza la función range, que genera una secuencia de números sobre 
# la que puedes iterar. La sintaxis es range(start, stop, step), donde start es el entero 
# inicial (inclusivo), stop es el último entero (no inclusivo), y step es la diferencia 
# entre un número y el anterior en la secuencia.

# Además, utiliza _ como variable de bucle. El _ actúa como un marcador de posición y es 
# útil cuando necesitas usar una variable pero no necesitas su valor.

        for _ in range(max_iterations):
            #pass

# Explicación
# Bucle for: Se ha añadido un bucle for que itera hasta max_iterations veces, 
# utilizando _ como variable de bucle. En este caso, el cuerpo del bucle está vacío (pass), 
# lo que indica que aún no hemos implementado la lógica del método de bisección.

# paso 12
# Estructura general: El resto del código permanece igual, manejando los casos de 
# números negativos, 0 y 1.

            mid = (low + high) / 2  # Calcular el punto medio
            square_mid = mid ** 2    # Calcular el cuadrado del punto medio

# Explicación de la Implementación
# Cálculo del punto medio: Dentro del bucle for, se calcula el punto medio del intervalo 
# actual utilizando la fórmula (low + high) / 2 y se asigna a la variable mid.

# Cálculo del cuadrado del punto medio: Se calcula el cuadrado del punto medio 
# con mid ** 2 y se almacena en la variable square_mid.

# Placeholder: Hemos dejado un comentario indicando que aquí se implementará la 
# lógica para comparar square_mid con square_target más adelante.

# Paso 13:
#           # Verificar si la diferencia está dentro de la tolerancia
            if abs(square_mid - square_target) < tolerance:
                root = mid  # Si está dentro de la tolerancia, hemos encontrado la raíz
                break  # Salir del bucle (paso 14)

# Explicación de la Implementación
# Verificación de la tolerancia: Se ha agregado una declaración if que verifica si 
# el valor absoluto de la diferencia entre square_mid y square_target está dentro de 
# la tolerancia especificada. Esto se hace utilizando la función abs().

# Asignación de root: Si la diferencia está dentro de la tolerancia, se asigna mid a root, 
# indicando que hemos encontrado una raíz cuadrada aproximada.

# Salida del bucle: Si se encuentra la raíz, se utiliza break para salir del bucle.

# Placeholder: Hemos dejado un comentario indicando que aquí se implementará la 
# lógica para ajustar el intervalo más adelante.
# paso 15
            # Ajustar el intervalo
            elif square_mid < square_target:
                low = mid  # La raíz está entre low y mid
            else:
                high = mid  # La raíz está entre mid y high

# Explicación de la Implementación
# Ajuste del intervalo: Se ha agregado una declaración elif que verifica si 
# square_mid es menor que square_target. Si es así, se asigna mid a low, lo que 
# significa que la raíz cuadrada se encuentra entre low y mid.

# Ajuste alternativo: Si square_mid no es menor que square_target, se asume que 
# square_mid es mayor, y se asigna mid a high, lo que significa que la raíz cuadrada 
# se encuentra entre mid y high.

# Resultado final: Después del bucle, se imprime el resultado final, ya sea la 
# raíz aproximada o un mensaje indicando que no se encontró una raíz cuadrada dentro 
# de los límites especificados.

# Paso 16:
         # Verificar si root es None después del bucle
        if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')

# Explicación de la Implementación
# Verificación de root: Después del bucle for, se ha agregado una declaración if que verifica si root es None. Esto se hace utilizando el operador is para comprobar la identidad del objeto.

# Mensaje de error: Si root es None, se imprime el mensaje: Failed to converge within {max_iterations} iterations. utilizando una f-string para formatear el mensaje.

# Resultado final: Si root no es None, se imprime el valor aproximado de la raíz cuadrada.

# Paso 18:
        else:
            print(f'The square root of {square_target} is approximately {root}')

# Explicación de la Implementación
# Cláusula else: Se ha agregado una cláusula else que se ejecuta si root no es None, 
# lo que indica que se ha encontrado una raíz.

# Mensaje de éxito: Dentro de esta cláusula, se imprime el mensaje: The square root 
# of {square_target} is approximately {root}., utilizando una f-string para formatear el mensaje.

# Paso 19:

    return root  # Devolver el valor de root

# Instrucción return: Al final de la función, se ha añadido return root. 
# Esto permite que la función devuelva el valor de root, que puede ser None 
# si no se encontró una raíz, o el valor aproximado de la raíz cuadrada si se encontró.

# Crear la variable N y asignarle el valor de 16
N = 16

# Variable N: Se ha creado la variable N fuera de la función y se le ha asignado el valor de 16.

# Llamar a la función con la variable N
square_root_bisection(N)

# Salidas: 
# The square root of 16 is approximately 4.0

# Código completo en limpio:
"""
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None

        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")

        else:   
            print(f'The square root of {square_target} is approximately {root}')

    return root

N = 16
# Llamar a la función con la variable N
square_root_bisection(N)
"""