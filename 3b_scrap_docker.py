import requests
from bs4 import BeautifulSoup

# URL del sitio web que queremos scrapear
url = "https://dockerlabs.es"

try:
    # Hacemos una solicitud GET a la URL
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()  # Lanza una excepción si el código de estado no es 200
    respuesta.encoding = 'utf-8'  # Forzar la codificación UTF-8 para manejar caracteres especiales

    # Parseamos el contenido HTML de la respuesta usando BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Buscamos todos los elementos <div> que tengan un atributo 'onclick'
    maquinas = soup.find_all('div', onclick=True)
    
    # Iteramos sobre cada máquina encontrada
    for maquina in maquinas:
        # Extraemos el valor del atributo 'onclick'
        onclick_text = maquina['onclick']
        
        # Dividimos el texto del atributo 'onclick' usando comillas simples (') como separador
        # Esto nos dará una lista de valores, donde los valores útiles están en las posiciones impares
        valores = onclick_text.split("'")
        
        # Extraemos los valores específicos:
        # - nombre_maquina: Segundo valor en la lista (índice 1)
        # - dificultad: Cuarto valor en la lista (índice 3)
        # - color: Sexto valor en la lista (índice 5) -> Este no lo usamos
        # - autor: Octavo valor en la lista (índice 7)
        # - enlace_autor: Décimo valor en la lista (índice 9) -> Este no lo usamos
        # - fecha: Duodécimo valor en la lista (índice 11)
        nombre_maquina = valores[1]
        dificultad = valores[3]
        autor = valores[7]
        fecha = valores[11]
        
        # Imprimimos la información de la máquina
        print(f"Nombre: {nombre_maquina}, Dificultad: {dificultad}, Autor: {autor}, Fecha: {fecha}")

except requests.exceptions.RequestException as e:
    # Manejo de errores relacionados con la solicitud HTTP
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    # Manejo de cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}") # salidas: 
# Nombre: Psycho, Dificultad: Fácil, Autor: Luisillo_o, Fecha: 10/08/2024
# Nombre: Dance-Samba, Dificultad: Medio, Autor: d1se0, Fecha: 26/08/2024
# Nombre: Pequeñas-Mentirosas, Dificultad: Fácil, Autor: beafn28, Fecha: 26/09/2024
# Nombre: Veneno, Dificultad: Medio, Autor: firstatack, Fecha: 30/06/2024
# Nombre: Grandma, Dificultad: Difícil, Autor: Pylon, Fecha: 13/08/2024
# Nombre: Apolos, Dificultad: Medio, Autor: Luisillo_o, Fecha: 06/09/2024
# Nombre: Report, Dificultad: Medio, Autor: TLuisillo_o, Fecha: 20/10/2024
# Nombre: Swiss, Dificultad: Medio, Autor: darksblack, Fecha: 17/11/2024
# Nombre: WhereIsMyWebShell, Dificultad: Fácil, Autor: El Pingüino de Mario, Fecha: 12/04/2024
# Nombre: Inclusion, Dificultad: Medio, Autor: El Pingüino de Mario, Fecha: 12/05/2024
# Nombre: Collections, Dificultad: Medio, Autor: El Pingüino de Mario, Fecha: 27/06/2024
# Nombre: Trust, Dificultad: Muy Fácil, Autor: El Pingüino de Mario, Fecha: 02/04/2024
# Nombre: Crackoff, Dificultad: Difícil, Autor: d1se0, Fecha: 26/08/2024
# Nombre: Predictable (Muy Difícil), Dificultad: Difícil, Autor: C4rta, Fecha: 25/06/2024
# Nombre: BreakMySSH, Dificultad: Muy Fácil, Autor: El Pingüino de Mario, Fecha: 29/05/2024
# Nombre: NodeClimb, Dificultad: Fácil, Autor: El Pingüino de Mario, Fecha: 05/07/2024
# Nombre: Library, Dificultad: Fácil, Autor: El Pingüino de Mario, Fecha: 13/05/2024
# Nombre: ConsoleLog, Dificultad: Fácil, Autor: El Pingüino de Mario, Fecha: 29/07/2024
# Nombre: HackZones, Dificultad: Medio, Autor: d1se0, Fecha: 17/11/2024
# Nombre: PingPong, Dificultad: Medio, Autor: El Pingüino de Mario, Fecha: 23/06/2024
# Nombre: FirstHacking, Dificultad: Muy Fácil, Autor: El Pingüino de Mario, Fecha: 14/06/2024   

import csv

with open('maquinas.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Dificultad', 'Autor', 'Fecha'])  # Escribir encabezados
    for maquina in maquinas:
        onclick_text = maquina['onclick']
        valores = onclick_text.split("'")
        if len(valores) >= 12:
            escritor.writerow([valores[1], valores[3], valores[7], valores[11]])