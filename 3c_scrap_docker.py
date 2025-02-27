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
        valores = onclick_text.split("'")
        
        # Extraemos los valores específicos:
        # - nombre_maquina: Segundo valor en la lista (índice 1)
        # - dificultad: Cuarto valor en la lista (índice 3)
        # - autor: Octavo valor en la lista (índice 7)
        # - fecha: Duodécimo valor en la lista (índice 11)
        nombre_maquina = valores[1]
        dificultad = valores[3]
        autor = valores[7]
        fecha = valores[11]
        
        # Buscamos el botón de descarga dentro del <div>
        boton_descarga = maquina.find('button', class_='download')
        if boton_descarga and 'onclick' in boton_descarga.attrs:
            # Extraemos el enlace de descarga del atributo 'onclick' del botón
            onclick_descarga = boton_descarga['onclick']
            # El enlace está dentro de la función window.open('enlace')
            enlace_descarga = onclick_descarga.split("'")[1]
        else:
            enlace_descarga = "Enlace no disponible"
        
        # Imprimimos la información de la máquina
        print(f"Nombre: {nombre_maquina}, Dificultad: {dificultad}, Autor: {autor}, Fecha: {fecha}, Enlace: {enlace_descarga}")

except requests.exceptions.RequestException as e:
    # Manejo de errores relacionados con la solicitud HTTP
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    # Manejo de cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}") # Salidas:
# Nombre: Psycho, Dificultad: Fácil, Autor: Luisillo_o, Fecha: 10/08/2024, Enlace: https://mega.nz/file/MSkgWDKJ#UHmAFBkvOpAc9fPIDocrVDLYz0VY6BolhLz87f3tSNM
# Nombre: Dance-Samba, Dificultad: Medio, Autor: d1se0, Fecha: 26/08/2024, Enlace: https://mega.nz/file/JCtnnLAJ#yeVJuvp8zhHiM55IHvnFJZ62_cjR1vmH-miDBc30slY
# Nombre: Pequeñas-Mentirosas, Dificultad: Fácil, Autor: beafn28, Fecha: 26/09/2024, Enlace: https://mega.nz/file/PBVmhbZR#4FmEtW_KULolSuinPFLs4pX2ukPnq8TjUDTEQk2bvsE
# Nombre: Veneno, Dificultad: Medio, Autor: firstatack, Fecha: 30/06/2024, Enlace: https://mega.nz/file/kOFDBYJC#mzBiVsOorShPcTLjPfzmesxAiCHxGkKEDAGxAIJ0r0g
# Nombre: Grandma, Dificultad: Difícil, Autor: Pylon, Fecha: 13/08/2024, Enlace: https://mega.nz/file/4SM2XISI#0z1POGIBA7ycOSybOw4w8t_R5X0p208lD5n3LptYtyE
# Nombre: Apolos, Dificultad: Medio, Autor: Luisillo_o, Fecha: 06/09/2024, Enlace: https://mega.nz/file/bANg0LCa#8_gUBjBdGbcVXMYuqzr5fVyAF2OM3AsYWTsWspdm3K4
# Nombre: Report, Dificultad: Medio, Autor: TLuisillo_o, Fecha: 20/10/2024, Enlace: https://mega.nz/file/zJEQ2TqB#dcsILUO_bjeEx1d_G0GkBQsXNzYuvBDFuC3ar5clkV8
# Nombre: Swiss, Dificultad: Medio, Autor: darksblack, Fecha: 17/11/2024, Enlace: https://mega.nz/file/vdtjRZJR#Ao1QF3I7aMh0db5X2YjchpusbBa_LzpvA2JTUhO3EmQ
# Nombre: WhereIsMyWebShell, Dificultad: Fácil, Autor: El Pingüino de Mario, Fecha: 12/04/2024, Enlace: https://mega.nz/file/Nf8giRID#1SuYshwSEJQnX2AxVhF_q03koiXDe4SI-p3UQhzhE30


# Explicación de los cambios:
# Extracción del enlace de descarga:

# Dentro de cada <div>, hay un botón con la clase download que contiene el enlace de descarga en su atributo onclick.

# Usamos maquina.find('button', class_='download') para encontrar el botón de descarga.

# Si el botón existe y tiene el atributo onclick, extraemos el enlace de descarga usando split("'").

# Manejo de casos donde no hay enlace:

# Si no se encuentra el botón de descarga o no tiene un enlace válido, asignamos "Enlace no disponible".

# Impresión del enlace:

# El enlace de descarga se imprime junto con el nombre, dificultad, autor y fecha de la máquina.

import csv

with open('maquinas_1.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Dificultad', 'Autor', 'Fecha', 'Enlace'])  # Escribir encabezados
    for maquina in maquinas:
        onclick_text = maquina['onclick']
        valores = onclick_text.split("'")
        if len(valores) >= 12:
            nombre_maquina = valores[1]
            dificultad = valores[3]
            autor = valores[7]
            fecha = valores[11]
            boton_descarga = maquina.find('button', class_='download')
            enlace_descarga = boton_descarga['onclick'].split("'")[1] if boton_descarga and 'onclick' in boton_descarga.attrs else "Enlace no disponible"
            escritor.writerow([nombre_maquina, dificultad, autor, fecha, enlace_descarga])