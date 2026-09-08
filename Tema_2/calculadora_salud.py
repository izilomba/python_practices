"""

Este programa representa una calculadora de salud que permite a los usuarios ingresar información personal y recibir recomendaciones de salud basadas en sus datos. La calculadora puede incluir funciones para calcular el índice de masa corporal (IMC), la tasa metabólica basal (TMB), y otros indicadores de salud relevantes. Además, puede proporcionar consejos sobre nutrición, ejercicio y hábitos saludables según los resultados obtenidos.

"""

#======================================================================================================================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
#======================================================================================================================================

def calcular_imc(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Fórmula: IMC = peso / (altura^2)

    Parámetros:
    peso_kg (float): Peso en kilogramos
    altura_m (float): Altura en metros

    Retorna:
    float: El IMC calculado
    """
    imc = peso_kg / (altura_m ** 2)
    return imc

def es_peso_saludable(imc):
    """
    Determina si el IMC está en rango saludable (18.5 - 24.9).

    Parámetro:
    imc (float): Índice de Masa Corporal

    Retorna:
    bool: True sí está en rango saludable, False sí no
    """
    # Operadores de comparación y lógicos
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    """Descripción: Determina si una persona tiene sobrepeso según su IMC.

Criterio médico: Se considera sobrepeso cuando el IMC es mayor o igual a 25.

Parámetro:

imc (float): El Índice de Masa Corporal calculado

Debe retornar:

True si hay sobrepeso (IMC ≥ 25)

False si no hay sobrepeso (IMC < 25)"""

    return imc >= 25

def tiene_bajo_peso(imc):

    """Descripción: Determina si una persona tiene bajo peso según su IMC.

Criterio médico: Se considera bajo peso cuando el IMC es menor a 18.5.

Parámetro:

imc (float): El Índice de Masa Corporal calculado

Debe retornar:

True si hay bajo peso (IMC < 18.5)

False si no hay bajo peso (IMC ≥ 18.5)"""

    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):

    """Calcula las calorías diarias recomendadas usando la fórmula de Harris-Benedict.

Fórmulas médicas:

Para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad)

Para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad)

Parámetros:

peso_kg (float): Peso en kilogramos

altura_cm (float): Altura en centímetros

edad (int): Edad en años

es_hombre (bool): True si es hombre, False si es mujer

Debe retornar:

(float): Las calorías diarias calculadas según el sexo"""

    # Operadores aritmeticos y booleanos

    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)

    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)

    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer

def calcular_agua_diaria(peso_kg):
    """Debe retornar:

(float): Litros de agua recomendados

Pasos a seguir:

Calcula cuántos mililitros de agua se necesitan: peso_kg * 35

Convierte los mililitros a litros dividiendo entre 1000

Retorna el resultado"""

    ml_agua = peso_kg * 35
    litros_agua = ml_agua / 1000

    return litros_agua



def calcular_ritmo_cardiaco_maximo(edad):
    """Descripción: Calcula el ritmo cardíaco máximo recomendado durante ejercicio.

Fórmula médica: 220 - edad

Parámetro:

edad (int): Edad en años

Debe retornar:

(int): Pulsaciones por minuto máximas recomendadas"""

    return 220 - edad

def generar_reporte_completo(nombre, peso, altura, edad, es_hombre):
    """"
    Genera un reporte completo de salud y fitness

    """

    print("="*60)
    print(f"📊 REPORTE DE FITNESS Y SALUD - {nombre}")
    print("="*60)

    # Cálculos
    imc = calcular_imc(peso, altura)
    calorias = calcular_calorias_diarias(peso, altura, edad, es_hombre)
    agua = calcular_agua_diaria(peso)
    fc_max = calcular_ritmo_cardiaco_maximo(edad)

    # Información Básica
    print("\n👤 Datos Personales:")
    print(f"   Peso: {peso} kg")
    print(f"   Altura: {altura} m")
    print(f"   Edad: {edad}")
    print(f"   ¿Hombre?: {es_hombre}")

    # IMC y evaluación
    print(f"\n💪 Índice de masa corporal (IMC):")
    print(f"     Tu IMC: {round(imc, 2)}")
    print(f"     ¿Es peso saludable? {es_peso_saludable(imc)}")
    print(f"     ¿Es bajo peso? {tiene_bajo_peso(imc)}")
    print(f"     ¿Sobrepeso? {tiene_sobrepeso(imc)}")

    # Calorias
    print(f"\n🍽️  Nutrición:")
    print(f"    Calorías diarias recomendadas: {round(calorias, 0)} kcal")
    print(f"    Agua diaria recomendada: {round(agua, 2)} litros")

    # Cardio
    print(f"\n❤️  Zona Cardíaca:")
    print(f"    Frecuencia cardíaca máxima: {fc_max} bpm")
    print(f"    Zona cardio óptima: {round(fc_max*0.6, 0)} - {round(fc_max*0.8, 0)} bpm")

    print("\n" + "="*60)

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

cabecera = """
╔════════════════════════════════════════════════════════════╗
║     💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪          ║
║                                                            ║
║        ¡Descubre tus métricas de salud óptimas!            ║
╚════════════════════════════════════════════════════════════╝
"""
print(cabecera)

# Solicitar datos al usuario
nombre = input("\n👤 ¿Cuál es tu nombre? ")
peso = float(input("⚖️  ¿Cuánto pesas? (kg): "))
altura = float(input("📏 ¿Cuánto mides? (metros, ej: 1.75): "))
edad = int(input("🎂 ¿Cuántos años tienes? "))
sexo = input("⚤  ¿Eres hombre o mujer? (H/M): ")

# Convertir sexo a booleano
es_hombre = sexo == "H" or sexo == "h" or sexo == "hombre"

# Generar reporte
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n✨ ¡Cuida tu salud! ✨\n")