def cabecera():
    """Muestra la cabecera de la aplicación."""
    borde = "="
    lateral = "|"
    titulo = f"""{borde * 89}
{lateral}                                                              {lateral}
{lateral}   ____                                _                      {lateral}
{lateral}  / ___|  __ _  _ __ ___    ___  _ __ | |_  __ _   __ _  ___  {lateral}
{lateral} | |  _  / _` || '_ ` _ \\  / _ \\| '__|| __|/ _` | / _` |/ __| {lateral}
{lateral} | |_| || (_| || | | | | ||  __/| |   | |_| (_| || (_| |\\__ \\ {lateral}
{lateral}  \\____| \\__,_||_| |_| |_| \\___||_|    \\__|\\__,_| \\__, ||___/ {lateral}
{lateral}                                                  |___/       {lateral}
{lateral}                                                              {lateral}
{borde * 89}"""
    print(titulo)
 
 
def crear_tag_basico(nombre):
    """
    Crea un gamertag básico usando las primeras 4 letras.
 
    Parámetro:
    nombre (str): Nombre del usuario
 
    Retorna:
    str: Gamertag básico
    """
    return nombre[:4]
 
 
def crear_tag_invertido(nombre):
    """
    Crea un gamertag invirtiendo el nombre completo.
 
    Parámetro:
    nombre (str): Nombre del usuario
 
    Retorna:
    str: Gamertag invertido
    """
    return nombre[::-1]
 
 
def crear_tag_intercalado(nombre, apellido):
    """
    Crea un gamertag combinando nombre y apellido.
 
    Parámetros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
 
    Retorna:
    str: Gamertag intercalado
    """
    primera_letra_nombre = nombre[0]
    primera_letra_apellido = apellido[0]
    resto_nombre = nombre[1:]
    resto_apellido = apellido[1:]
 
    tag = (
        primera_letra_nombre
        + primera_letra_apellido
        + resto_nombre
        + resto_apellido
    )
 
    return tag
 
 
def crear_tag_elite(nombre):
    """
    Crea un gamertag "elite" usando el inicio y el final del nombre.
 
    Ejemplo:
    "Pablo" → "Palo"
 
    Parámetro:
    nombre (str): Nombre del usuario
 
    Retorna:
    str: Gamertag elite
    """
    return nombre[:2] + nombre[-2:]
 
 
def crear_tag_numerico(nombre, numero_favorito):
    """
    Crea un gamertag usando las primeras 5 letras del nombre
    y el número favorito.
 
    Parámetros:
    nombre (str): Nombre del usuario
    numero_favorito (int): Número favorito del usuario
 
    Retorna:
    str: Gamertag numérico
    """
    return nombre[:5] + str(numero_favorito)
 
 
def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
 
    Parámetro:
    nombre (str): Nombre que se va a analizar
 
    Retorna:
    None
    """
    longitud_nombre = len(nombre)
 
    print("\n📊 ESTADÍSTICAS DE TU NOMBRE:")
    print(f"NOMBRE COMPLETO: {nombre}")
    print(f"LONGITUD DEL NOMBRE: {longitud_nombre}")
    print(f"PRIMERA LETRA: {nombre[0]}")
    print(f"ÚLTIMA LETRA: {nombre[-1]}")
 
 
def generar_todas_las_opciones(nombre, apellido, numero_favorito):
    """
    Genera y muestra todas las opciones de gamertag.
 
    Parámetros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero_favorito (int): Número favorito del usuario
 
    Retorna:
    None
    """
    tag_basico = crear_tag_basico(nombre)
    tag_invertido = crear_tag_invertido(nombre)
    tag_intercalado = crear_tag_intercalado(nombre, apellido)
    tag_elite = crear_tag_elite(nombre)
    tag_numerico = crear_tag_numerico(nombre, numero_favorito)
 
    print("\n========================================")
    print("🎯 TUS OPCIONES DE GAMERTAG:")
    print("========================================")
 
    print(f"1. TAG BÁSICO: {tag_basico}")
    print(f"2. TAG INVERTIDO: {tag_invertido}")
    print(f"3. TAG INTERCALADO: {tag_intercalado}")
    print(f"4. TAG ELITE: {tag_elite}")
    print(f"5. TAG NUMÉRICO: {tag_numerico}")
 
 
# ===========================================
# APLICACIÓN PRINCIPAL
# ===========================================
 
cabecera()
 
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
 
while True:
    entrada_numero = input("Introduce tu número favorito: ")
    if entrada_numero.isdigit():
        numero_favorito = int(entrada_numero)
        break
    print("Por favor, introduce un número entero válido.")
 
mostrar_estadisticas(nombre)
 
generar_todas_las_opciones(
    nombre,
    apellido,
    numero_favorito)

print("\n ¡Gracias por usar la aplicación de gamertags!🎮")