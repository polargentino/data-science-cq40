import google.generativeai as genai

# Configura la API Key
API_KEY = 'AIzaSyBj243ZkRZ-P3svcjupgXWWL-S1iitrRK8'  # Reemplaza con tu clave real
genai.configure(api_key=API_KEY)

# Selecciona un modelo actualizado (por ejemplo, Gemini 1.5 Flash)
modelo = genai.GenerativeModel('gemini-1.5-flash')  # Cambia 'gemini-pro' por esto

# Define una función para que el agente responda
def agente_responde(pregunta):
    respuesta = modelo.generate_content(pregunta)
    return respuesta.text

# Prueba el agente
if __name__ == "__main__":
    while True:
        entrada = input("Hazme una pregunta (o escribe 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
        try:
            resultado = agente_responde(entrada)
            print("Agente: ", resultado)
        except Exception as e:
            print(f"Error: {e}")