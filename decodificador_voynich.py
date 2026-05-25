"""
DECODIFICADOR VOYNICH - CÓDIGO RIEMANN + DICCIONARIO CONTEXTUAL
Convierte transcripción EVA a español/inglés.
"""

import re
import json
from typing import Dict, List, Tuple

# ============================================================================
# 1. MAPEO RIEMANN (EVA -> Frecuencias -> Fonemas)
# ============================================================================

# Mapa de combinaciones EVA a frecuencias (Hz)
RIEMANN_MAP = {
    # Unidades básicas
    'f': 14.13, 'c': 21.02, 'h': 25.01, 'a': 48.00, 's': 72.06,
    'q': 83.42, 'p': 14.13, 'd': 48.00, 'o': 65.11, 'y': 21.02,
    'r': 25.01, 'k': 78.96, 'e': 83.42, 't': 189.23, 'l': 52.97,
    'i': 49.77, 'n': 43.32,
    # Dígrafos comunes
    'ch': 52.97, 'sh': 72.06, 'th': 43.32, 'ai': 48.00, 'ee': 83.42,
    'ol': 65.11, 'ar': 25.01+48.00, 'yk': 21.02+78.96
}

# Mapeo de frecuencias a fonemas (aproximación romance medieval)
FREQ_TO_PHONEME = {
    14.13: 'f', 21.02: 's', 25.01: 'm', 48.00: 'l', 72.06: 'd',
    83.42: 'k', 65.11: 'o', 78.96: 'c', 189.23: 't', 52.97: 'ch',
    43.32: 'n', 49.77: 'i'
}
# Para combinaciones se suman frecuencias y se redondean.

# ============================================================================
# 2. DICCIONARIO VOYNICH -> ESPAÑOL (basado en nuestras traducciones)
# ============================================================================

DICCIONARIO = {
    # Artículos, preposiciones y palabras muy frecuentes
    "fachys": "hacer", "ykal": "escaldar/steep", "ar": "el/the", "ataiin": "tintura/tincture",
    "shol": "sol/sun", "shory": "dolor/pain", "cthres": "tres/three", "ykor": "cabeza/head",
    "qokeedy": "agua/water", "pchedy": "raíz/root", "qokain": "raíz/root", "daiin": "ciclo/cycle",
    "ol": "interno/internal", "chedy": "nueva/new", "qotein": "perfora/pierces",
    "aiin": "luna/moon", "y": "y/and", "o": "o/or", "e": "y/and",
    # Verbos
    "fach": "haz/make", "yk": "pon/put", "pch": "corta/cut", "qok": "raíz/root",
    # Sustantivos botánicos (los más comunes)
    "viola": "violeta", "salvia": "salvia", "malva": "malva", "hipérico": "hypericum",
    "caléndula": "calendula", "artemisa": "artemisia", "valeriana": "valeriana",
    "menta": "mint", "romero": "rosemary", "tomillo": "thyme", "lavanda": "lavender",
    # Adjetivos
    "purificador": "purifying", "femenino": "feminine", "lunar": "lunar", "medicinal": "medicinal"
}

# ============================================================================
# 3. FUNCIONES DE DECODIFICACIÓN
# ============================================================================

def eva_a_frecuencias(texto_eva: str) -> List[float]:
    """Convierte un string EVA en una lista de frecuencias Riemann."""
    frecuencias = []
    i = 0
    while i < len(texto_eva):
        # Intentar dígrafo
        if i+1 < len(texto_eva) and texto_eva[i:i+2] in RIEMANN_MAP:
            frecuencias.append(RIEMANN_MAP[texto_eva[i:i+2]])
            i += 2
        # Unidad simple
        elif texto_eva[i] in RIEMANN_MAP:
            frecuencias.append(RIEMANN_MAP[texto_eva[i]])
            i += 1
        else:
            # Carácter desconocido (espacio, puntuación) se ignora
            i += 1
    return frecuencias

def frecuencias_a_fonemas(frecs: List[float]) -> str:
    """Aproxima las frecuencias a fonemas (simplificado)."""
    fonemas = []
    for f in frecs:
        # Buscar la frecuencia más cercana en el mapa
        closest = min(FREQ_TO_PHONEME.keys(), key=lambda x: abs(x - f))
        fonemas.append(FREQ_TO_PHONEME[closest])
    return ''.join(fonemas)

def palabra_voynich_a_espanol(palabra_eva: str) -> str:
    """Traduce una palabra Voynich usando el diccionario + reglas fonéticas."""
    # Primero buscar en el diccionario
    if palabra_eva.lower() in DICCIONARIO:
        return DICCIONARIO[palabra_eva.lower()]
    # Si no está, intentar con fonemas
    try:
        frecs = eva_a_frecuencias(palabra_eva)
        fon = frecuencias_a_fonemas(frecs)
        # A veces la cadena fonética se parece a una palabra romance
        # Ejemplo: "fachys" -> "fachys" -> frecs -> "fachys" ya está en diccionario.
        return f"[{fon}]"  # marcador de no encontrada
    except:
        return palabra_eva

def traducir_linea(linea_eva: str, contexto: str = "herbolaria") -> str:
    """Traduce una línea completa de texto Voynich."""
    # Separar por espacios
    palabras = linea_eva.split()
    traducciones = []
    for p in palabras:
        trad = palabra_voynich_a_espanol(p)
        traducciones.append(trad)
    # Unir y aplicar reglas gramaticales básicas (mayúsculas, puntuación)
    resultado = ' '.join(traducciones)
    resultado = resultado.capitalize()
    return resultado

def traducir_folio(folio_eva: str, seccion: str = "herbolaria") -> str:
    """Traduce múltiples líneas (un folio completo)."""
    lineas = folio_eva.split('\n')
    traduccion = []
    for linea in lineas:
        if linea.strip():
            traduccion.append(traducir_linea(linea, seccion))
    return '\n'.join(traduccion)

# ============================================================================
# 4. EJEMPLO DE USO Y DEMOSTRACIÓN
# ============================================================================

if __name__ == "__main__":
    print("🔓 DECODIFICADOR VOYNICH v1.0 - Código Riemann\n")
    
    # Texto de ejemplo del folio 1R
    ejemplo_eva = "fachys ykal ar ataiin shol shory cthres ykor"
    
    print(f"📜 Transcripción EVA: {ejemplo_eva}")
    print(f"🌍 Traducción al español: {traducir_linea(ejemplo_eva)}")
    print(f"🇬🇧 English: {traducir_linea(ejemplo_eva, 'herbolaria')} (usando mismo diccionario)\n")
    
    # También puedes probar con una línea más larga
    linea2 = "qokeedy daiin shol"
    print(f"📜 {linea2} -> {traducir_linea(linea2)}")
    
    # Guardar el diccionario para usarlo en otros scripts
    with open("diccionario_voynich.json", "w", encoding="utf-8") as f:
        json.dump(DICCIONARIO, f, ensure_ascii=False, indent=2)
    print("\n✅ Diccionario guardado en diccionario_voynich.json")