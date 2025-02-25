import requests
from bs4 import BeautifulSoup

# URL de MercadoLibre con los notebooks listados
URL = "https://listado.mercadolibre.com.ar/notebooks#D[A:notebooks]"

# Headers para simular un navegador real y evitar bloqueos
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Hacer la solicitud HTTP a la página de MercadoLibre
response = requests.get(URL, headers=HEADERS)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar el primer producto en la lista
    primer_producto = soup.select_one("ol > li h3 a")

    if primer_producto:
        # Extraer el nombre del producto
        nombre = primer_producto.text.strip()

        # Extraer el enlace y limpiar la URL
        enlace = primer_producto["href"]
        enlace_limpio = enlace.split("?")[0]  # Elimina parámetros de seguimiento

        # Mostrar el resultado
        print(f"Nombre: {nombre}")
        print(f"Enlace: {enlace_limpio}")
    else:
        print("No se encontró el primer producto.")
else:
    print(f"Error al acceder a la página. Código: {response.status_code}")
# Salida:
# Nombre: Notebook 15.6'' Intel Celeron N4020 256gb Ssd 8gb Ram Linux
# Enlace: https://click1.mercadolibre.com.ar/mclics/clicks/external/MLA/count
                                                                              