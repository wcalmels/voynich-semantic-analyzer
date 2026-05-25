import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EVA_FILE = "mapa_semantico_eva_limpio.csv"
CORPUS_FILE = "corpus_medieval_turco_expandido.csv"
SALIDA = "embeddings_comparacion_eva_medieval.csv"

df_eva = pd.read_csv(EVA_FILE)
df_corpus = pd.read_csv(CORPUS_FILE)

def limpiar(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñçşğâîû\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# Construir documento EVA semántico
texto_eva = " ".join(
    df_eva["significado_probable"].fillna("").astype(str).tolist()
)

texto_eva += " " + " ".join(
    df_eva["palabra_eva"].fillna("").astype(str).tolist()
)

texto_eva = limpiar(texto_eva)

registros = []

documentos = [texto_eva]
titulos = ["EVA_SEMANTICO"]

for _, row in df_corpus.iterrows():
    texto_corpus = " ".join([
        str(row.get("titulo", "")),
        str(row.get("tema", "")),
        str(row.get("texto_original", "")),
        str(row.get("transliteracion", "")),
        str(row.get("traduccion", "")),
        str(row.get("keywords", ""))
    ])

    documentos.append(limpiar(texto_corpus))
    titulos.append(row.get("titulo", ""))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documentos)

similitudes = cosine_similarity(X[0:1], X[1:]).flatten()

for i, score in enumerate(similitudes):
    row = df_corpus.iloc[i]

    registros.append({
        "titulo": row.get("titulo", ""),
        "fecha": row.get("fecha", ""),
        "idioma": row.get("idioma", ""),
        "region": row.get("region", ""),
        "tema": row.get("tema", ""),
        "score_embedding": round(float(score), 4),
        "keywords": row.get("keywords", "")
    })

df_resultado = pd.DataFrame(registros)
df_resultado = df_resultado.sort_values(
    "score_embedding",
    ascending=False
)

df_resultado.to_csv(SALIDA, index=False, encoding="utf-8")

print("Embeddings EVA vs corpus medieval generados.")
print(f"Archivo creado: {SALIDA}")
print("\nRanking de similitud:\n")
print(df_resultado)