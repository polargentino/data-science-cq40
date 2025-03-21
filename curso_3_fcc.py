def add_expense(expenses, amount, category):
    """
Las funciones lambda le brindan una manera concisa de escribir funciones pequeñas y 
descartables en su código.

En este proyecto, explorarás el potencial de las Funciones Lambda mediante la creación 
de un sistema de seguimiento de gastos. La aplicación resultante demostrará cómo usar 
las Funciones Lambda para optimizar y optimizar las operaciones.

    Agrega un gasto a la lista de gastos.

    Parámetros:
        expenses (list): Lista de gastos.
        amount (float): Monto del gasto.
        category (str): Categoría del gasto.
    """
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    """
    Imprime todos los gastos en la lista.

    Parámetros:
        expenses (list): Lista de gastos.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calcula el total de todos los gastos.

    Parámetros:
        expenses (list): Lista de gastos.

    Retorna:
        float: Suma total de los montos de los gastos.
    """
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filtra los gastos por una categoría específica.

    Parámetros:
        expenses (list): Lista de gastos.
        category (str): Categoría para filtrar.

    Retorna:
        filter object: Objeto filtrado que contiene los gastos de la categoría especificada.
    """
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    """
    Función principal que ejecuta el rastreador de gastos.

    Permite al usuario agregar gastos, listar todos los gastos, mostrar el total de gastos,
    filtrar gastos por categoría y salir del programa.
    """
    expenses = []  # Lista para almacenar los gastos
    while True:
        # Menú de opciones
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')  # Solicitar la elección del usuario

        if choice == '1':
            # Agregar un gasto
            amount = float(input('Enter amount: '))  # Solicitar el monto del gasto
            category = input('Enter category: ')  # Solicitar la categoría del gasto
            add_expense(expenses, amount, category)  # Llamar a la función para agregar el gasto

        elif choice == '2':
            # Listar todos los gastos
            print('\nAll Expenses:')
            print_expenses(expenses)  # Llamar a la función para imprimir los gastos
    
        elif choice == '3':
            # Mostrar el total de gastos
            print('\nTotal Expenses: ', total_expenses(expenses))  # Llamar a la función para calcular el total
    
        elif choice == '4':
            # Filtrar gastos por categoría
            category = input('Enter category to filter: ')  # Solicitar la categoría para filtrar
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)  # Filtrar gastos
            print_expenses(expenses_from_category)  # Imprimir los gastos filtrados
    
        elif choice == '5':
            # Salir del programa
            print('Exiting the program.')
            break  # Terminar el bucle while

# Llamar a la función principal para ejecutar el programa
main()

# Explicación Paso a Paso
# Función add_expense:

# Propósito: Agrega un gasto a la lista de gastos.

# Parámetros:

# expenses: Lista de gastos.

# amount: Monto del gasto.

# category: Categoría del gasto.

# Funcionamiento: Añade un diccionario con el monto y la categoría a la lista expenses.

# Función print_expenses:

# Propósito: Imprime todos los gastos en la lista.

# Parámetros:

# expenses: Lista de gastos.

# Funcionamiento: Itera sobre la lista de gastos e imprime cada uno en un formato legible.

# Función total_expenses:

# Propósito: Calcula el total de todos los gastos.

# Parámetros:

# expenses: Lista de gastos.

# Retorno: Suma total de los montos de los gastos.

# Funcionamiento: Usa map() para extraer los montos y sum() para calcular el total.

# Función filter_expenses_by_category:

# Propósito: Filtra los gastos por una categoría específica.

# Parámetros:

# expenses: Lista de gastos.

# category: Categoría para filtrar.

# Retorno: Objeto filtrado que contiene los gastos de la categoría especificada.

# Funcionamiento: Usa filter() para seleccionar los gastos que coinciden con la categoría.

# Función main:

# Propósito: Función principal que ejecuta el rastreador de gastos.

# Funcionamiento:

# Muestra un menú de opciones al usuario.

# Permite agregar gastos, listar todos los gastos, mostrar el total de gastos, filtrar gastos por categoría y salir del programa.

# Usa un bucle while para mantener el programa en ejecución hasta que el usuario elija salir.

# Llamada a main:

# Inicia el programa llamando a la función main().


# Opción 1: Agregar un gasto
# Selecciona la opción 1 y presiona Enter.

# Ingresa el monto del gasto (por ejemplo, 50).

# Ingresa la categoría del gasto (por ejemplo, Comida).

# El gasto se agregará a la lista.

# Opción 2: Listar todos los gastos
# Selecciona la opción 2 y presiona Enter.

# Verás una lista de todos los gastos que has agregado, con su monto y categoría.

# Opción 3: Mostrar el total de gastos
# Selecciona la opción 3 y presiona Enter.

# Verás el total de todos los gastos que has agregado.

# Opción 4: Filtrar gastos por categoría
# Selecciona la opción 4 y presiona Enter.

# Ingresa la categoría que deseas filtrar (por ejemplo, Comida).

# Verás una lista de los gastos que pertenecen a esa categoría.

# Opción 5: Salir del programa
# Selecciona la opción 5 y presiona Enter.

# El programa se cerrará.

# Ejemplo de Uso
# Aquí tienes un ejemplo de cómo interactuar con el programa:

# Agregar gastos:

# Selecciona 1 y agrega un gasto de 50 en la categoría Comida.

# Selecciona 1 nuevamente y agrega un gasto de 30 en la categoría Transporte.

# Listar todos los gastos:

# Selecciona 2 y verás:

# Copy
# Amount: 50.0, Category: Comida
# Amount: 30.0, Category: Transporte
# Mostrar el total de gastos:

# Selecciona 3 y verás:

# Copy
# Total Expenses: 80.0
# Filtrar gastos por categoría:

# Selecciona 4 y filtra por Comida. Verás:

# Copy
# Expenses for Comida:
# Amount: 50.0, Category: Comida
# Salir del programa:

# Selecciona 5 para salir.

# Preguntas Frecuentes
# ¿Qué pasa si ingreso un valor no válido?

# Si ingresas un valor no válido (por ejemplo, texto en lugar de un número para el monto), el programa mostrará un error. Asegúrate de ingresar valores correctos.

# ¿Cómo puedo mejorar el programa?

# Puedes agregar validaciones para manejar entradas incorrectas.

# También puedes guardar los gastos en un archivo para que no se pierdan al cerrar el programa.

# ¿Qué hago si no tengo Python instalado?

# Descarga e instala Python desde python.org.

# Conclusión
# ¡Ahora sabes cómo ejecutar y usar el rastreador de gastos! Es una herramienta sencilla pero poderosa para llevar un registro de tus gastos. Si tienes más preguntas o necesitas más ayuda, ¡no dudes en pedírmelo! 😊