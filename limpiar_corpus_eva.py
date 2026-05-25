import re
import json

ARCHIVO_EVA = "voynich_eva_corpus.evt"

lineas_eva = []

with open(ARCHIVO_EVA, "r", encoding="utf-8", errors="ignore") as f:
    for linea in f:
        linea = linea.strip()

        # Buscar líneas con formato de folio Voynich: <f1r>, <f1v>, <f116v>, etc.
        if not linea.startswith("<f"):
            continue

        # Separar encabezado del texto
        if ">" not in linea:
            continue

        encabezado, texto = linea.split(">", 1)

        # Limpiar texto EVA
        texto = texto.lower()

        # Eliminar comentarios entre llaves o corchetes
        texto = re.sub(r"\{.*?\}", " ", texto)
        texto = re.sub(r"\[.*?\]", " ", texto)

        # Conservar solo letras, espacios, puntos y guiones EVA básicos
        texto = re.sub(r"[^a-z\s\.\-]", " ", texto)

        # Cambiar puntos y guiones por espacios
        texto = texto.replace(".", " ")
        texto = texto.replace("-", " ")

        # Normalizar espacios
        texto = re.sub(r"\s+", " ", texto).strip()

        # Filtrar líneas demasiado cortas
        if len(texto) < 5:
            continue

        lineas_eva.append({
            "folio": encabezado.replace("<", "").strip(),
            "eva": texto
        })

with open("corpus_eva_limpio.json", "w", encoding="utf-8") as f:
    json.dump(lineas_eva, f, indent=2, ensure_ascii=False)

print("Corpus EVA limpio generado.")
print(f"Líneas extraídas: {len(lineas_eva)}")

print("\nPrimeras 10 líneas:\n")

for item in lineas_eva[:10]:
    print(item["folio"], "->", item["eva"])