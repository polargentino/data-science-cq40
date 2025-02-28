"""
Aprendiendo a obtener archivo robots.txt para hacer scraping ético.
¡Claro! Vamos a empezar con el web scraping y cómo obtener el archivo robots.txt de un sitio web.
El archivo robots.txt es un documento que los sitios web utilizan para comunicarse con los rastreadores web (web crawlers), indicándoles qué partes del sitio pueden o no pueden visitar.
Aquí tienes un código en Python para obtener el contenido del archivo robots.txt de un sitio web:
"""
import requests # Esta línea importa la biblioteca requests, que es una librería HTTP para Python. Permite enviar solicitudes HTTP/HTTPS a servidores web y manejar las respuestas.



def get_robots_txt(url):
    """
    Obtiene el contenido del archivo robots.txt de un sitio web.
    
    Args:
        url (str): La URL base del sitio web (ej. 'https://www.ejemplo.com')
        
    Returns:
        str: El contenido del archivo robots.txt
    """
# Aquí se define una función llamada get_robots_txt que toma un parámetro: la URL del sitio web.
# El texto entre comillas triples es un docstring (documentación de la función) que explica qué hace la función, qué parámetros acepta y qué devuelve.

    
    # Asegurarse de que la URL no termine con '/'
    if url.endswith('/'):
        url = url[:-1]
# Este bloque verifica si la URL termina con una barra diagonal (/).
# Si termina con /, se elimina usando un slice url[:-1] que toma todos los caracteres excepto el último.
# Esto es importante para construir correctamente la URL del archivo robots.txt.        
    
    # Construir la URL completa para el archivo robots.txt
    robots_url = f"{url}/robots.txt"
# Esta línea construye la URL completa para el archivo robots.txt.
# Utiliza un f-string para concatenar la URL base con "/robots.txt".
# Por ejemplo, si url es "https://www.infobae.com", entonces robots_url será "https://www.infobae.com/robots.txt".    
    
    try:
        # Realizar la solicitud HTTP
        response = requests.get(robots_url)
# Aquí comienza un bloque try-except para manejar posibles errores.
# requests.get(robots_url) envía una solicitud HTTP GET a la URL del robots.txt.
# El resultado se guarda en la variable response, que es un objeto que contiene la respuesta del servidor.        
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.text
        else:
            return f"Error al obtener robots.txt: Código de estado {response.status_code}"
# Este bloque verifica el código de estado HTTP de la respuesta.
# El código 200 significa "OK" (éxito).
# Si es 200, devuelve el contenido textual del archivo robots.txt mediante response.text.
# Si no es 200, devuelve un mensaje de error que incluye el código de estado recibido.       
    
    except Exception as e:
        return f"Error: {str(e)}"
# Este es el bloque except que captura cualquier excepción que pueda ocurrir durante la solicitud HTTP.
# Podría ser un error de conexión, un problema de DNS, etc.
# Devuelve un mensaje con el error capturado.    

# Ejemplo de uso
if __name__ == "__main__":
# Esta condición comprueba si el script se está ejecutando directamente (no siendo importado como módulo).
# Es una práctica común en Python para código que debe ejecutarse solo cuando el script se ejecuta directamente.   
    # URL de Infobae
    website_url = "https://www.infobae.com"
    
    robots_content = get_robots_txt(website_url)
    print(robots_content)
# Define la URL base del sitio web de Infobae.
# Llama a la función get_robots_txt pasando esa URL.
# Imprime el contenido del archivo robots.txt en la consola.

# Este código es relativamente sencillo pero efectivo para obtener el archivo robots.txt de cualquier sitio web. La estructura try-except es importante porque maneja posibles errores que pueden ocurrir durante la solicitud HTTP, como problemas de conexión o respuestas de error del servidor.
# ¿Hay alguna parte específica que te gustaría que explique con más detalle?

# Salidas:
# User-agent: *

# Sitemap: https://www.infobae.com/arc/outboundfeeds/sitemap2/
# Sitemap: https://www.infobae.com/arc/outboundfeeds/news-sitemap2/
# Sitemap: https://www.infobae.com/arc/outboundfeeds/sitemap2/category/america/
# Sitemap: https://www.infobae.com/arc/outboundfeeds/news-sitemap2/category/america/
# Sitemap: https://www.infobae.com/arc/outboundfeeds/sitemap2/category/teleshow/
# Sitemap: https://www.infobae.com/arc/outboundfeeds/news-sitemap2/category/teleshow/

# Sitemap: https://www.infobae.com/arc/outboundfeeds/sitemap-index-static/

# Fuente: Claude3.7 Sonnet
# ¡Excelente! El código funcionó correctamente y has obtenido el archivo robots.txt de Infobae.com. Esto es lo que puedes observar en el resultado:

# 1. `User-agent: *` - Esto indica que las reglas aplican a todos los bots/crawlers.

# 2. Hay varios sitemaps listados, que son archivos XML que contienen información sobre las páginas del sitio, su relevancia y frecuencia de actualización:
#    - Sitemaps generales: `sitemap2/`
#    - Sitemaps de noticias: `news-sitemap2/`
#    - Sitemaps por categorías como "america" y "teleshow"
#    - Un sitemap estático: `sitemap-index-static/`

# Curiosamente, no veo prohibiciones o restricciones explícitas (`Disallow`) en este robots.txt, lo que podría indicar que el sitio permite el crawling de la mayoría de sus páginas.

# ¿Te gustaría continuar con el siguiente paso en el aprendizaje de web scraping? Podríamos:
# - Extraer información de una página específica de Infobae
# - Trabajar con los sitemaps que encontramos
# - Analizar la estructura HTML de las páginas

# ¿Qué te interesaría explorar ahora?