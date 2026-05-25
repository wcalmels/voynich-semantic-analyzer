import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

EVA_FILE = "mapa_semantico_eva_limpio.csv"
CORPUS_FILE = "corpus_medieval_turco_expandido.csv"
SALIDA_CSV = "mapa_embeddings_2d.csv"
SALIDA_IMG = "mapa_embeddings_2d.png"

print("Cargando modelo...")
modelo = SentenceTransformer("all-MiniLM-L6-v2")

df_eva = pd.read_csv(EVA_FILE)
df_corpus = pd.read_csv(CORPUS_FILE)

# Documento EVA
texto_eva = " ".join(df_eva["significado_probable"].fillna("").astype(str).tolist())
texto_eva += " " + " ".join(df_eva["palabra_eva"].fillna("").astype(str).tolist())

documentos = [texto_eva]
labels = ["EVA_SEMANTICO"]
tipos = ["EVA"]

# Documentos corpus medieval
for _, row in df_corpus.iterrows():
    texto = " ".join([
        str(row.get("titulo", "")),
        str(row.get("tema", "")),
        str(row.get("texto_original", "")),
        str(row.get("transliteracion", "")),
        str(row.get("traduccion", "")),
        str(row.get("keywords", ""))
    ])

    documentos.append(texto)
    labels.append(str(row.get("titulo", "")))
    tipos.append("CORPUS_MEDIEVAL")

print("Generando embeddings...")
embeddings = modelo.encode(documentos)

print("Reduciendo a 2D con PCA...")
pca = PCA(n_components=2)
coords = pca.fit_transform(embeddings)

df_out = pd.DataFrame({
    "label": labels,
    "tipo": tipos,
    "x": coords[:, 0],
    "y": coords[:, 1]
})

df_out.to_csv(SALIDA_CSV, index=False, encoding="utf-8")

# Visualización
plt.figure(figsize=(12, 8))

for i, row in df_out.iterrows():
    if row["tipo"] == "EVA":
        plt.scatter(row["x"], row["y"], marker="*", s=300)
    else:
        plt.scatter(row["x"], row["y"], s=100)

    plt.text(
        row["x"] + 0.01,
        row["y"] + 0.01,
        row["label"],
        fontsize=8
    )

plt.title("Mapa semántico 2D - EVA vs Corpus Médico Medieval")
plt.xlabel("Componente PCA 1")
plt.ylabel("Componente PCA 2")
plt.grid(True)
plt.tight_layout()

plt.savefig(SALIDA_IMG, dpi=300)

print("Visualización generada.")
print(f"CSV creado: {SALIDA_CSV}")
print(f"Imagen creada: {SALIDA_IMG}")

plt.show()