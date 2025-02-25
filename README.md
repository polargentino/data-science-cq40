# Proyecto de Configuración para Ciencia de Datos

Este proyecto verifica la instalación y funcionamiento de diversas librerías utilizadas en Web Scraping y Análisis de Datos en Python.

## 📌 Requisitos
- Python 3.7+
- Entorno virtual recomendado (`venv` o `virtualenv`)
- Conexión a Internet para probar las solicitudes web

## 📦 Instalación
Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## 🛠️ Librerías Incluidas

### 🔍 Web Scraping
- **requests**: Para realizar solicitudes HTTP.
- **beautifulsoup4**: Para analizar HTML y extraer datos.
- **scrapy**: Un framework para web scraping.
- **selenium**: Para automatizar navegadores web.
- **playwright**: Otra alternativa a Selenium para automatización web.

### 📊 Análisis de Datos.
- **pandas**: Manipulación de datos en estructuras tipo DataFrame.
- **numpy**: Cálculo numérico eficiente.
- **matplotlib**: Visualización de datos con gráficos.
- **scikit-learn**: Algoritmos de aprendizaje automático.

## 🚀 Uso
Para ejecutar el script y verificar la instalación de las librerías:

```bash
python script.py
```

Si todo está correctamente instalado, el script mostrará la versión de cada librería y realizará pequeñas pruebas con ellas.

## 📝 Notas
- Si alguna librería falta, puedes instalarla con:

  ```bash
  pip install nombre_libreria
  ```

- Si tienes problemas con `playwright`, ejecuta:

  ```bash
  playwright install
  ```

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

Por Pol Monsalvo 25/02/2025
