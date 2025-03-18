import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configura la API Key desde el archivo .env
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("No se encontró la API_KEY en el archivo .env")
genai.configure(api_key=API_KEY)

# Selecciona el modelo Gemini 1.5 Flash
modelo = genai.GenerativeModel('gemini-1.5-flash')

# Lista global para almacenar el historial
historial = []


def guardar_respuesta_en_archivo(texto):
    """Guarda la respuesta del agente en un archivo de texto con marca de tiempo.

    Args:
        texto (str): La respuesta generada por el agente.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"respuestas_agente_{timestamp}.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"Respuesta guardada en 'respuestas_agente_{timestamp}.txt'")


def agente_responde(pregunta, estilo="neutral"):
    """Genera una respuesta del agente basada en la pregunta y un estilo personalizado.

    Args:
        pregunta (str): La entrada del usuario.
        estilo (str, optional): El tono o estilo de la respuesta. Opciones: 'neutral', 'poetico', 'historico'. 
                                Por defecto es 'neutral'.

    Returns:
        str: La respuesta generada por el modelo.
    """
    historial.append({"rol": "usuario", "texto": pregunta})

    # Personalizar el prompt según el estilo y añadir contexto histórico explícito
    if estilo == "poetico":
        prompt = f"Escribe una respuesta poética a: {pregunta}"
    elif estilo == "historico":
        prompt = f"Responde como un historiador del siglo XVI sobre esta pregunta histórica: {pregunta}"
    else:
        prompt = f"Responde como un experto en historia si es una pregunta histórica, o de forma general si no lo es: {pregunta}"

    respuesta = modelo.generate_content(prompt)
    texto_respuesta = respuesta.text
    historial.append({"rol": "agente", "texto": texto_respuesta})

    return texto_respuesta


def interpretar_entrada_vaga(entrada):
    """Interpreta entradas vagas y decide qué hacer de forma autónoma.

    Args:
        entrada (str): La entrada del usuario.

    Returns:
        tuple: (pregunta refinada, estilo) para procesar la respuesta.
    """
    entrada_lower = entrada.lower()
    if "suleiman" in entrada_lower or "sultán" in entrada_lower:
        opciones = [
            ("Escribe un poema corto sobre el Sultán Suleimán", "poetico"),
            ("Explica la vida del Sultán Suleimán", "historico"),
            ("¿Qué logró Suleimán el Magnífico?", "neutral")
        ]
        if historial and "poema" in historial[-1]["texto"].lower():
            return opciones[1]  # Cambia a histórico si ya dio un poema
        return opciones[0]  # Por defecto, poema
    return (entrada, "neutral")


def interactuar_bidireccional(entrada):
    """Solicita clarificación al usuario si la entrada es ambigua.

    Args:
        entrada (str): La entrada del usuario.

    Returns:
        str: La entrada refinada tras la interacción.
    """
    if len(entrada.split()) <= 2 and "?" not in entrada:  # Si es corta y no es pregunta clara
        print("¿Podrías darme más detalles? Por ejemplo:")
        print("1. Quiero un poema.")
        print("2. Quiero una explicación histórica.")
        opcion = input("Elige una opción (1, 2) o escribe más: ")
        if opcion == "1":
            return f"Escribe un poema sobre {entrada}"
        elif opcion == "2":
            return f"Explica la historia de {entrada}"
        return opcion
    return entrada


if __name__ == "__main__":
    print("¡Bienvenido al Agente Autónomo Mejorado!")
    while True:
        entrada = input("Hazme una pregunta (o escribe 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break

        try:
            # Mejorar entrada vaga con interacción bidireccional
            entrada_refinada = interactuar_bidireccional(entrada)

            # Interpretar autónomamente la entrada
            pregunta, estilo = interpretar_entrada_vaga(entrada_refinada)

            # Generar respuesta con memoria y estilo personalizado
            resultado = agente_responde(pregunta, estilo=estilo)

            # Mostrar el historial reciente (pregunta anterior, no la actual)
            if len(historial) > 2:  # Asegurarse de que haya una pregunta anterior
                print("Contexto anterior:", historial[-3]["texto"][:50] + "...")
            print("Agente:", resultado)

            # Guardar la respuesta en un archivo
            guardar_respuesta_en_archivo(resultado)

        except Exception as e:
            print(f"Error: {e}")

# SAalidas:
# # ¡Bienvenido al Agente Autónomo Mejorado!
# Hazme una pregunta (o escribe 'salir' para terminar): quien es Jesús de nazaret?
# Agente: Jesús de Nazaret es una figura central en el cristianismo, cuya existencia histórica es un tema debatido entre académicos, aunque la mayoría de los historiadores concuerdan en que existió una persona histórica en la que se basa la figura bíblica.  No hay evidencia extrabíblica directa y contemporánea que describa a Jesús con el mismo detalle que los evangelios, pero  hay referencias indirectas de historiadores romanos como Tácito y Josefo que, aunque breves y con posibles interpretaciones divergentes, apuntan hacia la existencia de un Jesús que tuvo seguidores y fue crucificado en Judea bajo el gobierno romano.

# La dificultad para establecer una biografía definitiva de Jesús se debe a la naturaleza de las fuentes. Los evangelios, los textos canónicos del cristianismo, son escritos que, si bien contienen información histórica, también son textos teológicos con una agenda narrativa y teológica específica,  que busca transmitir un mensaje de fe más que una biografía objetiva al estilo moderno.  Por lo tanto, separar la figura histórica de Jesús de la figura teológica y mítica que se ha construido a su alrededor es un reto hermenéutico complejo.

# En resumen, mientras la existencia de una persona histórica llamada Jesús es probable según la evidencia disponible, la reconstrucción de su vida, sus enseñanzas y su impacto se basa en una compleja interpretación de fuentes con sesgos ideológicos y religiosos inherentes. La figura que conocemos es, por tanto, una construcción histórica y teológica que ha evolucionado a través de siglos de interpretación y tradición.

# Respuesta guardada en 'respuestas_agente_2025-03-18_18-34-21.txt'
# Hazme una pregunta (o escribe 'salir' para terminar): cuales fueron sus enseñanzas?
# Contexto anterior: Jesús de Nazaret es una figura central en el crist...
# Agente: La pregunta "¿Cuáles fueron sus enseñanzas?" requiere contexto.  Para responder adecuadamente, necesito saber **a quién** se refiere "sus".  ¿De qué persona o grupo se está hablando?  

# Por ejemplo:

# * **Si se refiere a Jesús:** Sus enseñanzas, según los Evangelios, se centran en el amor, la compasión, el perdón, la humildad, la justicia social y el reino de Dios.  Se basan en parábolas, sermones (como el Sermón del Monte), y acciones.  La interpretación de estas enseñanzas ha variado ampliamente a lo largo de la historia, dando lugar a diferentes denominaciones cristianas.

# * **Si se refiere a Sócrates:** Sus enseñanzas, conocidas principalmente a través de los escritos de Platón y Jenofonte, se centraban en la búsqueda del conocimiento a través del diálogo y la introspección.  El método socrático, que implicaba cuestionar las suposiciones y definir términos, buscaba llegar a la verdad mediante el razonamiento.  Enseñaba la importancia de la virtud y la autoconciencia.

# * **Si se refiere a Confucio:** Sus enseñanzas, recogidas en los Analectos, se centran en la ética, la moralidad, la familia, la sociedad y el gobierno.  Énfasis en la importancia de la jerarquía social, el respeto filial, la rectitud, la benevolencia y el ritual.  Su filosofía ha tenido una profunda influencia en la cultura china.

# * **Si se refiere a un líder político moderno:** Sus enseñanzas dependerán de su ideología y acciones.  Podrían abarcar desde políticas económicas específicas hasta visiones sobre la justicia social o la política exterior.  Sería necesario especificar de qué líder se habla para una respuesta precisa.

# En resumen, la pregunta es demasiado amplia para una respuesta concisa sin más información.  Proporcione el nombre de la persona o grupo, y podré dar una respuesta históricamente precisa e informada.

# Respuesta guardada en 'respuestas_agente_2025-03-18_18-35-15.txt'
# Hazme una pregunta (o escribe 'salir' para terminar): cuales fueron las parabolas de jesús de nazaret?
# Contexto anterior: La pregunta "¿Cuáles fueron sus enseñanzas?" requi...
# Agente: No existe una lista exhaustiva y canónicamente aceptada de las parábolas de Jesús de Nazaret.  Los evangelios canónicos (Mateo, Marcos, Lucas y Juan) contienen diferentes colecciones de relatos que son considerados parábolas, y la clasificación misma depende de la interpretación teológica y literaria.  No hay un acuerdo unánime sobre qué relatos califican exactamente como parábolas y cuáles son otros tipos de enseñanza, como alegorías o simplemente narraciones.

# Los evangelios presentan varias parábolas que son relativamente comunes en diferentes versiones, pero con variaciones en el detalle.  Entre las más conocidas y recurrentes,  podemos mencionar:

# * **La parábola del sembrador:** Ilustra la recepción diversa del mensaje de Dios.
# * **La parábola del buen samaritano:**  Enfoca en el amor al prójimo, independientemente de la pertenencia religiosa o social.
# * **La parábola del hijo pródigo:**  Trata sobre el perdón y la misericordia divina.
# * **La parábola de la oveja perdida:**  También enfatiza el amor y la búsqueda de lo perdido por parte de Dios.
# * **La parábola de los talentos:**  Habla sobre la responsabilidad y el uso de los dones recibidos.
# * **La parábola del trigo y la cizaña:**  Se refiere a la coexistencia del bien y del mal en el mundo.
# * **La parábola del fariseo y el publicano:**  Resalta la humildad y la justicia ante Dios.


# Es crucial entender que la identificación de una narrativa como parábola es una interpretación posterior. Los evangelios mismos no clasifican sistemáticamente sus relatos de esta manera.  Además, la transmisión oral de estas historias antes de su redacción escrita probablemente llevó a variaciones y a la posible pérdida de otras parábolas.  Por lo tanto, cualquier listado de "las parábolas" de Jesús es necesariamente incompleto y sujeto a debate académico.

# Respuesta guardada en 'respuestas_agente_2025-03-18_18-36-22.txt'
# Hazme una pregunta (o escribe 'salir' para terminar):            