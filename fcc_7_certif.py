"""
Qwen2.5-Max
7:39 pm
¡Vamos a resolver este proyecto paso a paso! Usaremos Pandas para analizar el conjunto de 
datos demográficos y responder a las preguntas planteadas. A continuación, te muestro cómo 
implementar cada cálculo en el archivo

Explicación del Código
Cargar el Conjunto de Datos :
Usamos pd.read_csv para cargar el archivo adult.data.csv.
Pregunta 1: Número de Personas por Raza :
Usamos value_counts() en la columna race para contar el número de personas por raza.
Pregunta 2: Edad Promedio de los Hombres :
Filtramos el DataFrame para incluir solo hombres (sex == 'Male') y calculamos la media de la columna age.
Pregunta 3: Porcentaje de Personas con Licenciatura :
Contamos cuántas personas tienen education == 'Bachelors' y dividimos entre el total de personas.
Preguntas 4 y 5: Educación Avanzada y Salario :
Filtramos el DataFrame para personas con educación avanzada (Bachelors, Masters, Doctorate) y calculamos el porcentaje que gana más de 50k.
Repetimos el proceso para personas sin educación avanzada.
Pregunta 6: Mínimo Número de Horas Trabajadas :
Usamos .min() en la columna hours-per-week.
Pregunta 7: Porcentaje de Personas que Trabajan el Mínimo de Horas y Ganaron >50k :
Filtramos el DataFrame para personas que trabajan el mínimo de horas y calculamos el porcentaje que gana más de 50k.
Pregunta 8: País con Mayor Porcentaje de Personas que Ganaron >50k :
Agrupamos por native-country y calculamos el porcentaje de personas que ganan más de 50k usando .groupby() y .apply().
Pregunta 9: Ocupación Más Popular en India para Quienes Ganaron >50k :
Filtramos el DataFrame para personas de India que ganan más de 50k y usamos .mode() para encontrar la ocupación más común.
"""

import pandas as pd

def calculate_demographic_data(print_data=True):
    # Cargar el conjunto de datos desde un archivo CSV
    df = pd.read_csv('/home/pol/Escritorio/data-science-cq40/adult.data.csv')
    # 1. ¿Cuántas personas de cada raza están representadas en este set de datos?
    race_counts = df['race'].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. ¿Qué porcentaje de personas con una educación avanzada (Bachelors, Masters o Doctorate) generan más de 50k?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # 5. ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # 6. ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tienen un salario de más de 50k?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. ¿Qué país tiene el más alto porcentaje de personas que ganan >50k y cuál es ese porcentaje?
    country_salary = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # 9. Identifica la ocupación más popular de aquellos que ganan >50k en India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_salary['occupation'].mode()[0]

    # Imprimir los resultados si print_data es True
    if print_data:
        print("Número de personas por raza:\n", race_counts)
        print("Edad promedio de los hombres:", average_age_men)
        print("Porcentaje de personas con licenciatura:", percentage_bachelors)
        print("Porcentaje de personas con educación avanzada que ganan >50K:", higher_education_rich)
        print("Porcentaje de personas sin educación avanzada que ganan >50K:", lower_education_rich)
        print("Mínimo número de horas trabajadas por semana:", min_work_hours)
        print("Porcentaje de personas que trabajan el mínimo de horas y ganan >50K:", rich_percentage)
        print("País con el mayor porcentaje de personas que ganan >50K:", highest_earning_country)
        print("Porcentaje de personas que ganan >50K en ese país:", highest_earning_country_percentage)
        print("Ocupación más popular en India para quienes ganan >50K:", top_IN_occupation)

    # Retornar los resultados como un diccionario
    return {
        'race_count': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

