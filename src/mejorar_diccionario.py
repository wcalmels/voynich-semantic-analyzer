import pandas as pd
import json
import re
from collections import Counter

CSV_PATH = "voynich_texto_completo.csv"
DICT_PATH = "diccionario_voynich.json"

SALIDA_DESCONOCIDAS = "palabras_desconocidas_frecuentes.csv"
SALIDA_PROPUESTAS = "propuestas_diccionario.json"

# Cargar CSV
df = pd.read_csv(CSV_PATH)

# Cargar diccionario existente
try:
    with open(DICT_PATH, "r", encoding="utf-8") as f:
        diccionario = json.load(f)
except:
    diccionario = {}

contador = Counter()

# Contar palabras EVA
for texto in df["transcripcion_eva"].fillna(""):

    palabras = re.findall(r"[a-zA-Z]+", str(texto).lower())

    contador.update(palabras)

conocidas = set(k.lower() for k in diccionario.keys())

desconocidas = []

# Buscar palabras no conocidas
for palabra, frecuencia in contador.most_common():

    if palabra not in conocidas:

        desconocidas.append({
            "palabra_eva": palabra,
            "frecuencia": frecuencia,
            "propuesta_traduccion": ""
        })

# Exportar CSV
df_desconocidas = pd.DataFrame(desconocidas)

df_desconocidas.to_csv(
    SALIDA_DESCONOCIDAS,
    index=False,
    encoding="utf-8"
)

# Generar propuestas automáticas
propuestas = {}

for item in desconocidas[:50]:

    palabra = item["palabra_eva"]

    if palabra.startswith("qok"):
        propuesta = "raíz / agua medicinal"

    elif palabra.startswith("yk"):
        propuesta = "preparar / escaldar"

    elif palabra.startswith("sh"):
        propuesta = "calor / sol / dolor"

    elif palabra.startswith("ch"):
        propuesta = "cortar / compuesto"

    elif palabra.startswith("dai"):
        propuesta = "ciclo / repetición"

    elif palabra.startswith("ai"):
        propuesta = "luna / ciclo"

    elif palabra.startswith("ol") or palabra.startswith("ot"):
        propuesta = "interno / órgano"

    else:
        propuesta = "pendiente"

    propuestas[palabra] = propuesta

# Guardar JSON
with open(
    SALIDA_PROPUESTAS,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        propuestas,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Análisis completado.")
print(f"Archivo generado: {SALIDA_DESCONOCIDAS}")
print(f"Archivo generado: {SALIDA_PROPUESTAS}")

print("\nTop 20 palabras desconocidas:\n")

for item in desconocidas[:20]:

    print(
        f"{item['palabra_eva']} -> frecuencia {item['frecuencia']}"
    )