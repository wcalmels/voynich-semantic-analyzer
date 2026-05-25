import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

EVA_FILE = "mapa_semantico_eva_limpio.csv"
CORPUS_FILE = "corpus_medieval_turco_expandido.csv"
SALIDA = "embeddings_transformers_resultados.csv"

print("Cargando modelo semántico...")
modelo = SentenceTransformer('all-MiniLM-L6-v2')

df_eva = pd.read_csv(EVA_FILE)
df_corpus = pd.read_csv(CORPUS_FILE)

# -----------------------------
# DOCUMENTO EVA SEMÁNTICO
# -----------------------------

texto_eva = " ".join(
    df_eva["significado_probable"].fillna("").astype(str).tolist()
)

texto_eva += " "

texto_eva += " ".join(
    df_eva["palabra_eva"].fillna("").astype(str).tolist()
)

# -----------------------------
# EMBEDDING EVA
# -----------------------------

print("Generando embedding EVA...")
embedding_eva = modelo.encode([texto_eva])

# -----------------------------
# COMPARACIÓN
# -----------------------------

resultados = []

for _, row in df_corpus.iterrows():

    texto_corpus = " ".join([
        str(row.get("titulo", "")),
        str(row.get("tema", "")),
        str(row.get("texto_original", "")),
        str(row.get("transliteracion", "")),
        str(row.get("traduccion", "")),
        str(row.get("keywords", ""))
    ])

    embedding_corpus = modelo.encode([texto_corpus])

    similitud = cosine_similarity(
        embedding_eva,
        embedding_corpus
    )[0][0]

    resultados.append({
        "titulo": row.get("titulo", ""),
        "fecha": row.get("fecha", ""),
        "idioma": row.get("idioma", ""),
        "tema": row.get("tema", ""),
        "score_transformer": round(float(similitud), 4),
        "keywords": row.get("keywords", "")
    })

# -----------------------------
# RESULTADOS
# -----------------------------

df_resultados = pd.DataFrame(resultados)

df_resultados = df_resultados.sort_values(
    "score_transformer",
    ascending=False
)

df_resultados.to_csv(
    SALIDA,
    index=False,
    encoding="utf-8"
)

print("\nEmbeddings transformers completados.")
print(f"Archivo generado: {SALIDA}")

print("\nRanking semántico:\n")
print(df_resultados)