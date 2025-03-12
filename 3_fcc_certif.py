"""
Qwen2.5-Max
7:19 pm
¡Vamos a resolver este proyecto paso a paso! Este proyecto implica crear una clase Category 
que maneje transacciones financieras y una función create_spend_chart que genere un gráfico 
de barras basado en los gastos de cada categoría.

Explicación del Código:

Clase Category:
--------------
1-Constructor (__init__) :
--------------------------
Inicializa el nombre de la categoría y una lista vacía llamada ledger.

2-Método deposit :
------------------
Agrega un depósito al ledger como un diccionario con la cantidad y la descripción.

3-Método withdraw :
-------------------
Realiza un retiro si hay suficientes fondos. El retiro se almacena como un número negativo 
en el ledger.

4-Método get_balance :
----------------------
Calcula el saldo actual sumando todos los valores en el ledger.

5-Método transfer :
-------------------
Transfiere fondos a otra categoría. Si hay suficientes fondos, realiza un retiro en la 
categoría actual y un depósito en la categoría de destino.

6-Método check_funds :
--------------------
Verifica si hay suficientes fondos para realizar una transacción.

7-Método __str__ :
-------------------
Genera una representación en cadena del objeto, incluyendo el título, las transacciones 
y el saldo total.

Función create_spend_chart:
---------------------------
1-Calcular Gastos :
-------------------
Para cada categoría, calcula el total gastado sumando los valores negativos en el ledger.

2-Calcular Porcentajes :
------------------------
Calcula el porcentaje gastado por categoría respecto al total gastado. Redondea hacia abajo 
al múltiplo de 10 más cercano.

3-Construir el Gráfico :
------------------------
Crea una cuadrícula donde cada fila representa un intervalo de 10%.
Agrega una línea horizontal debajo de las barras.
Escribe los nombres de las categorías verticalmente debajo del gráfico.

"""
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Agrega un depósito al ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Realiza un retiro si hay suficientes fondos."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Devuelve el saldo actual."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        """Transfiere fondos a otra categoría."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Verifica si hay suficientes fondos para una transacción."""
        return amount <= self.get_balance()

    def __str__(self):
        """Representación en cadena del objeto Category."""
        # Título centrado con asteriscos
        title = self.name.center(30, "*") + "\n"
        items = ""
        total = 0

        # Formatear cada entrada del ledger
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
            total += entry["amount"]

        # Total final
        output = title + items + f"Total: {total:.2f}"
        return output
    

def create_spend_chart(categories):
    """Crea un gráfico de barras que muestra el porcentaje gastado por categoría."""
    # Calcular el total gastado por cada categoría
    spending = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spending.append(spent)

    # Calcular el porcentaje gastado (redondeado hacia abajo al 10 más cercano)
    total_spent = sum(spending)
    percentages = [(spent / total_spent) * 100 if total_spent > 0 else 0 for spent in spending]
    percentages = [int(p // 10) * 10 for p in percentages]

    # Construir el gráfico
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Línea horizontal debajo de las barras
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Etiquetas de las categorías escritas verticalmente
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")

# Ejemplo de Uso:
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(150)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
# ***********Clothing***********
# Transfer from Food       50.00
#                         -25.55
# Total: 24.45
# *************Auto*************
# initial deposit        1000.00
#                        -150.00
# Total: 850.00
# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60|          
#  50|       o  
#  40|       o  
#  30| o     o  
#  20| o     o  
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g     