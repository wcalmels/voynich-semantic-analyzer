import pandas as pd
import re
from collections import Counter

EVA_FILE = "mapa_semantico_eva_limpio.csv"
CORPUS_FILE = "corpus_medieval_turco_expandido.csv"
SALIDA = "comparacion_eva_corpus_medieval.csv"

df_eva = pd.read_csv(EVA_FILE)
df_corpus = pd.read_csv(CORPUS_FILE)

def tokenizar(texto):
    texto = str(texto).lower()
    return re.findall(r"[a-záéíóúüñçşğâîû]+", texto)

# Tokens EVA
tokens_eva = []
for palabra in df_eva["palabra_eva"].dropna():
    tokens_eva.extend(tokenizar(palabra))

# Familias semánticas EVA
familias_eva = df_eva["significado_probable"].dropna().tolist()
tokens_semanticos_eva = []

for item in familias_eva:
    tokens_semanticos_eva.extend(tokenizar(item))

# Tokens corpus medieval
registros = []

for _, row in df_corpus.iterrows():
    texto_total = " ".join([
        str(row.get("titulo", "")),
        str(row.get("tema", "")),
        str(row.get("texto_original", "")),
        str(row.get("transliteracion", "")),
        str(row.get("traduccion", "")),
        str(row.get("keywords", ""))
    ])

    tokens_corpus = tokenizar(texto_total)

    contador_corpus = Counter(tokens_corpus)
    contador_eva_sem = Counter(tokens_semanticos_eva)

    coincidencias = set(tokens_corpus) & set(tokens_semanticos_eva)

    score = len(coincidencias)

    registros.append({
        "titulo": row.get("titulo", ""),
        "fecha": row.get("fecha", ""),
        "idioma": row.get("idioma", ""),
        "region": row.get("region", ""),
        "tema": row.get("tema", ""),
        "coincidencias_semanticas": ", ".join(sorted(coincidencias)),
        "score_coincidencia": score,
        "keywords": row.get("keywords", "")
    })

df_resultado = pd.DataFrame(registros)

df_resultado = df_resultado.sort_values(
    "score_coincidencia",
    ascending=False
)

df_resultado.to_csv(SALIDA, index=False, encoding="utf-8")

print("Comparación EVA vs corpus medieval completada.")
print(f"Archivo generado: {SALIDA}")
print("\nResultados:\n")
print(df_resultado)