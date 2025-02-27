import requests
from bs4 import BeautifulSoup
import charset_normalizer  # Para detectar codificación automáticamente

url = "https://dockerlabs.es"

try:
    # Realizar la solicitud
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()  # Lanza una excepción si hay error HTTP

    # Detectar codificación automáticamente
    codificacion = charset_normalizer.detect(respuesta.content)['encoding']
    if codificacion:
        respuesta.encoding = codificacion
    else:
        respuesta.encoding = 'utf-8'  # Fallback a UTF-8

    # Parsear el HTML
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Encontrar las máquinas
    maquinas = soup.find_all('div', onclick=True)

    if not maquinas:
        print("No se encontraron máquinas en la página.")
    else:
        print("Máquinas encontradas:")
        for i, maquina in enumerate(maquinas, 1):
            try:
                onclick_text = maquina['onclick']
                partes = onclick_text.split("'")
                nombre = partes[1]
                dificultad = partes[3]
                autor = partes[7]
                print(f"{i}. {nombre} --> {dificultad} --> {autor}")
            except (IndexError, KeyError):
                print(f"{i}. Error al procesar una máquina: {onclick_text}")

except requests.RequestException as e:
    print(f"Error al conectar con la página: {e}")
except Exception as e:
    print(f"Error inesperado: {e}") # Salidas: Por Grok3 AI

#  Máquinas encontradas:
# 1. Psycho --> Fácil --> Luisillo_o
# 2. Dance-Samba --> Medio --> d1se0
# 3. Pequeñas-Mentirosas --> Fácil --> beafn28
# 4. Veneno --> Medio --> firstatack
# 5. Grandma --> Difícil --> Pylon
# 6. Apolos --> Medio --> Luisillo_o
# 7. Report --> Medio --> TLuisillo_o
 

# Cambios y mejoras
# Manejo de excepciones:
# Se agrega try/except para capturar errores de red (como timeouts) o problemas al parsear el HTML.
# Si falla el procesamiento de una máquina específica, no detiene el programa, solo muestra un mensaje.
# Codificación automática:
# Usa charset_normalizer (requiere instalación con pip install charset_normalizer) para detectar la codificación del sitio automáticamente, evitando problemas con caracteres como "ñ" o "á".
# Si no se detecta, usa UTF-8 como fallback.
# Timeout:
# Se añade timeout=10 en la solicitud para evitar que el programa se cuelgue si el sitio no responde.
# Uso de enumerate:
# Reemplaza conteo_maquinas con enumerate para numerar las máquinas en la salida de forma más elegante.
# Validación de datos:
# Comprueba si se encontraron máquinas antes de intentar procesarlas.
# Maneja errores en caso de que el atributo onclick no esté presente o tenga un formato inesperado.
# Salida mejorada:
# Numeración de las máquinas para facilitar la lectura.
# Instalación adicional
# Para que el código mejorado funcione, necesitas instalar charset_normalizer: