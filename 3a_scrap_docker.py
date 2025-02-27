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
        # - autor: Sexto valor en la lista (índice 5)
        # - fecha: Octavo valor en la lista (índice 7)
        nombre_maquina = valores[1]
        dificultad = valores[3]
        autor = valores[5]
        fecha = valores[7]
        
        # Imprimimos la información de la máquina
        print(f"Nombre: {nombre_maquina}, Dificultad: {dificultad}, Autor: {autor}, Fecha: {fecha}")

except requests.exceptions.RequestException as e:
    # Manejo de errores relacionados con la solicitud HTTP
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    # Manejo de cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}") # Salidas:
# Nombre: Psycho, Dificultad: Fácil, Autor: #8bc34a, Fecha: Luisillo_o
# Nombre: Dance-Samba, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: Pequeñas-Mentirosas, Dificultad: Fácil, Autor: #8bc34a, Fecha: beafn28
# Nombre: Veneno, Dificultad: Medio, Autor: #e0a553, Fecha: firstatack
# Nombre: Grandma, Dificultad: Difícil, Autor: #d83c31, Fecha: Pylon
# Nombre: Apolos, Dificultad: Medio, Autor: #e0a553, Fecha: Luisillo_o
# Nombre: Report, Dificultad: Medio, Autor: #e0a553, Fecha: TLuisillo_o
# Nombre: Swiss, Dificultad: Medio, Autor: #e0a553, Fecha: darksblack
# Nombre: WhereIsMyWebShell, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Inclusion, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Collections, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Trust, Dificultad: Muy Fácil, Autor: #43959b, Fecha: El Pingüino de Mario
# Nombre: Crackoff, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Predictable (Muy Difícil), Dificultad: Difícil, Autor: #d83c31, Fecha: C4rta
# Nombre: BreakMySSH, Dificultad: Muy Fácil, Autor: #43959b, Fecha: El Pingüino de Mario
# Nombre: NodeClimb, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Library, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: ConsoleLog, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: HackZones, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: PingPong, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: FirstHacking, Dificultad: Muy Fácil, Autor: #43959b, Fecha: El Pingüino de Mario
# Nombre: Reverse, Dificultad: Medio, Autor: #e0a553, Fecha: maciiii___
# Nombre: MyBB, Dificultad: Medio, Autor: #e0a553, Fecha: Pylon
# Nombre: Hidden, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: 404-not-found, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: 0xc0ffee, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: DebugMe, Dificultad: Difícil, Autor: #d83c31, Fecha: Lenam
# Nombre: Stranger, Dificultad: Medio, Autor: #e0a553, Fecha: kaikoperez
# Nombre: Stack, Dificultad: Medio, Autor: #e0a553, Fecha: 4bytes
# Nombre: Vendetta, Dificultad: Fácil, Autor: #8bc34a, Fecha: misk0z
# Nombre: BuscaLove, Dificultad: Fácil, Autor: #8bc34a, Fecha: Prendelo
# Nombre: UserSearch, Dificultad: Medio, Autor: #e0a553, Fecha: kvzlx
# Nombre: Vulnerame, Dificultad: Difícil, Autor: #d83c31, Fecha: firstatack
# Nombre: chmod-4755, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: Lfi.elf, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Candy, Dificultad: Fácil, Autor: #8bc34a, Fecha: Luisillo_o
# Nombre: Verdejo, Dificultad: Fácil, Autor: #8bc34a, Fecha: The Hackers Labs
# Nombre: HedgeHog, Dificultad: Muy Fácil, Autor: #43959b, Fecha: AnkbNikas
# Nombre: BorazuwarahCTF, Dificultad: Muy Fácil, Autor: #43959b, Fecha: BorazuwarahCTF
# Nombre: Sender, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Insecure, Dificultad: Difícil, Autor: #d83c31, Fecha: 4bytes
# Nombre: Upload, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Domain, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: DevTools, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Move, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Database, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Vacaciones, Dificultad: Muy Fácil, Autor: #43959b, Fecha: Romabri
# Nombre: Dark, Dificultad: Medio, Autor: #e0a553, Fecha: makak77
# Nombre: Rubiks, Dificultad: Medio, Autor: #e0a553, Fecha: Luisillo_o
# Nombre: Forgotten_Portal, Dificultad: Medio, Autor: #e0a553, Fecha: Cyberland
# Nombre: Force, Dificultad: Difícil, Autor: #d83c31, Fecha: kvzlx
# Nombre: SecretJenkins, Dificultad: Facil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: HiddenCat, Dificultad: Facil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Fileception, Dificultad: Medio, Autor: #e0a553, Fecha: danielPRZ
# Nombre: HackMeDaddy, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Backend, Dificultad: Fácil, Autor: #8bc34a, Fecha: 4bytes
# Nombre: Vulnvault, Dificultad: Fácil, Autor: #8bc34a, Fecha: d1se0
# Nombre: Allien, Dificultad: Fácil, Autor: #8bc34a, Fecha: Luisillo_o
# Nombre: HereBash, Dificultad: Medio, Autor: #e0a553, Fecha: firstatack
# Nombre: Subversion (Beta), Dificultad: Difícil, Autor: #d83c31, Fecha: Lenam
# Nombre: Reflection, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: BadPlugin, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Raas, Dificultad: Difícil, Autor: #d83c31, Fecha: darksblack
# Nombre: Extraviado, Dificultad: Fácil, Autor: #8bc34a, Fecha: Hack_Viper
# Nombre: cineHack, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: Seeker, Dificultad: Medio, Autor: #e0a553, Fecha: maciiii___
# Nombre: Tproot, Dificultad: Muy Fácil, Autor: #43959b, Fecha: d1se0
# Nombre: Internship, Dificultad: Fácil, Autor: #8bc34a, Fecha: s1egfr1ed
# Nombre: Canario, Dificultad: Difícil, Autor: #d83c31, Fecha: 4bytes
# Nombre: ApiBase, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Memesploit, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: WalkingCMS, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Mirame, Dificultad: Fácil, Autor: #8bc34a, Fecha: maciiii___
# Nombre: Rutas, Dificultad: Medio, Autor: #e0a553, Fecha: firstatack
# Nombre: NorC, Dificultad: Difícil, Autor: #d83c31, Fecha: kvzlx
# Nombre: ChatMe, Dificultad: Medio, Autor: #e0a553, Fecha: Pylon & Zunderrub
# Nombre: ShowTime, Dificultad: Fácil, Autor: #8bc34a, Fecha: maciiii___
# Nombre: Pinguinazo, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Balulero, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Inj3ct0rs, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: ChocolateLovers, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Sites, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Redirection, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: r00tless, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: -Pn, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: BruteShock, Dificultad: Medio, Autor: #e0a553, Fecha: maciiii___ & darksblack
# Nombre: Escolares, Dificultad: Fácil, Autor: #8bc34a, Fecha: Luisillo_o
# Nombre: AnonymousPingu, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: File, Dificultad: Fácil, Autor: #8bc34a, Fecha: Scuffito y Jul3n-dot
# Nombre: HackPenguin, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: FindYourStyle, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Buffered, Dificultad: Difícil, Autor: #d83c31, Fecha: rxffsec
# Nombre: Whoiam, Dificultad: Fácil, Autor: #8bc34a, Fecha: Pylon
# Nombre: JenkHack, Dificultad: Fácil, Autor: #8bc34a, Fecha: d1se0
# Nombre: Amor, Dificultad: Fácil, Autor: #8bc34a, Fecha: Romabri
# Nombre: Darkweb, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Asucar, Dificultad: Medio, Autor: #e0a553, Fecha: The Hackers Labs
# Nombre: Road to Olympus, Dificultad: Difícil, Autor: #d83c31, Fecha: PatxaSec
# Nombre: AguaDeMayo, Dificultad: Facil, Autor: #8bc34a, Fecha: The Hackers Labs
# Nombre: Master, Dificultad: Medio, Autor: #e0a553, Fecha: Pylon & El Pingüino de Mario
# Nombre: SkullNet, Dificultad: Difícil, Autor: #d83c31, Fecha: Slayer0x & W4tson
# Nombre: Pressenter, Dificultad: Fácil, Autor: #8bc34a, Fecha: d1se0
# Nombre: Los 40 Ladrones, Dificultad: Fácil, Autor: #8bc34a, Fecha: firstatack
# Nombre: Picadilly, Dificultad: Fácil, Autor: #8bc34a, Fecha: kaikoperez
# Nombre: Devil, Dificultad: Medio, Autor: #e0a553, Fecha: kaikoperez
# Nombre: Winterfell, Dificultad: Fácil, Autor: #8bc34a, Fecha: Zunderrub
# Nombre: Mapache2, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: StrongJenkins, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: HackTheHeaven, Dificultad: Difícil, Autor: #d83c31, Fecha: AlbertoMD3
# Nombre: Pntopntobarra, Dificultad: Fácil, Autor: #8bc34a, Fecha: maciiii___
# Nombre: PyRed, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Flow, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: LittlePivoting, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: DockHackLab, Dificultad: Medio, Autor: #e0a553, Fecha: firstatack
# Nombre: Paradise, Dificultad: Fácil, Autor: #8bc34a, Fecha: kaikoperez
# Nombre: SummerVibes, Dificultad: Difícil, Autor: #d83c31, Fecha: El Pingüino de Mario
# Nombre: Bashpariencias, Dificultad: Medio, Autor: #e0a553, Fecha: firstatack
# Nombre: BigPivoting, Dificultad: Difícil, Autor: #d83c31, Fecha: El Pingüino de Mario
# Nombre: Corruptress, Dificultad: Difícil, Autor: #d83c31, Fecha: maciiii___
# Nombre: Fooding, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: Stellarjwt, Dificultad: Fácil, Autor: #8bc34a, Fecha: Alv-fh
# Nombre: Queuemedic, Dificultad: Difícil, Autor: #d83c31, Fecha: b0ysie7e
# Nombre: ChocolateFire, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario
# Nombre: DoubleTrouble, Dificultad: Difícil, Autor: #d83c31, Fecha: maciiii___ & darksblack
# Nombre: Eclipse, Dificultad: Medio, Autor: #e0a553, Fecha: Xerosec
# Nombre: DockerLabs, Dificultad: Fácil, Autor: #8bc34a, Fecha: El Pingüino de Mario
# Nombre: Wallet, Dificultad: Medio, Autor: #e0a553, Fecha: Pylon & El Pingüino de Mario
# Nombre: Cachopo, Dificultad: Medio, Autor: #e0a553, Fecha: PatxaSec
# Nombre: Obsession, Dificultad: Muy Fácil, Autor: #43959b, Fecha: Juan
# Nombre: DoubleFlow, Dificultad: Difícil, Autor: #d83c31, Fecha: 4bytes
# Nombre: Elevator, Dificultad: Fácil, Autor: #8bc34a, Fecha: beafn28
# Nombre: Cracker, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: Spain, Dificultad: Difícil, Autor: #d83c31, Fecha: darksblack
# Nombre: Express, Dificultad: Medio, Autor: #e0a553, Fecha: d1se0
# Nombre: Patriaquerida, Dificultad: Fácil, Autor: #8bc34a, Fecha: JuanR
# Nombre: Insanity, Dificultad: Difícil, Autor: #d83c31, Fecha: maciiii___
# Nombre: Lifeordead, Dificultad: Difícil, Autor: #d83c31, Fecha: d1se0
# Nombre: Unrecover, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario#
# Nombre: Walking Dead, Dificultad: Fácil, Autor: #8bc34a, Fecha: JuanR
# Nombre: ApiRoot, Dificultad: Medio, Autor: #e0a553, Fecha: El Pingüino de Mario



# Explicación paso a paso:
# Importación de librerías:

# requests: Para hacer solicitudes HTTP y obtener el contenido de la página web.

# BeautifulSoup: Para parsear el contenido HTML y extraer información específica.

# URL del sitio web:

# Definimos la URL del sitio web que queremos scrapear (https://dockerlabs.es).

# Solicitud HTTP:

# Usamos requests.get(url) para hacer una solicitud GET a la URL.

# respuesta.raise_for_status() verifica si la solicitud fue exitosa (código de estado 200). Si no, lanza una excepción.

# respuesta.encoding = 'utf-8' asegura que el contenido se interprete correctamente como UTF-8, evitando problemas con caracteres especiales.

# Parseo del HTML:

# Usamos BeautifulSoup(respuesta.text, 'html.parser') para parsear el contenido HTML de la respuesta.

# Búsqueda de elementos:

# Usamos soup.find_all('div', onclick=True) para encontrar todos los elementos <div> que tengan un atributo onclick.

# Iteración sobre las máquinas:

# Para cada máquina (<div> con onclick), extraemos el valor del atributo onclick.

# Extracción de valores:

# El valor del atributo onclick es una cadena de texto que contiene varios valores separados por comillas simples (').

# Usamos split("'") para dividir la cadena en una lista de valores.

# Los valores útiles están en las posiciones impares de la lista:

# nombre_maquina: Segundo valor (índice 1).

# dificultad: Cuarto valor (índice 3).

# autor: Sexto valor (índice 5).

# fecha: Octavo valor (índice 7).

# Impresión de la información:

# Usamos print() para mostrar la información de cada máquina en un formato legible.

# Manejo de errores:

# Capturamos excepciones relacionadas con la solicitud HTTP (requests.exceptions.RequestException) y cualquier otro error inesperado (Exception).