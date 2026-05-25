import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

EVA_FILE = "mapa_semantico_eva_limpio.csv"
SALIDA = "clusters_semanticos_automaticos.csv"

N_CLUSTERS = 4

print("Cargando datos EVA...")
df = pd.read_csv(EVA_FILE)

# Crear texto semántico por cada palabra EVA
documentos = []

for _, row in df.iterrows():
    texto = " ".join([
        str(row.get("palabra_eva", "")),
        str(row.get("familia", "")),
        str(row.get("significado_probable", "")),
        str(row.get("planta", "")),
        str(row.get("uso_medico", ""))
    ])

    documentos.append(texto)

print("Cargando modelo de embeddings...")
modelo = SentenceTransformer("all-MiniLM-L6-v2")

print("Generando embeddings...")
embeddings = modelo.encode(documentos)

print("Ejecutando clustering semántico...")
kmeans = KMeans(
    n_clusters=N_CLUSTERS,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(embeddings)

df["cluster_semantico"] = clusters

# Calcular palabra más representativa por cluster
resumen = []

for cluster_id in sorted(df["cluster_semantico"].unique()):
    sub = df[df["cluster_semantico"] == cluster_id]

    palabras = ", ".join(sub["palabra_eva"].astype(str).unique())
    familias = ", ".join(sub["familia"].astype(str).unique())
    significados = ", ".join(sub["significado_probable"].astype(str).unique())

    resumen.append({
        "cluster": cluster_id,
        "cantidad": len(sub),
        "palabras_eva": palabras,
        "familias": familias,
        "significados_probables": significados
    })

df_resumen = pd.DataFrame(resumen)

df.to_csv(SALIDA, index=False, encoding="utf-8")
df_resumen.to_csv("resumen_clusters_semanticos.csv", index=False, encoding="utf-8")

print("Clustering semántico automático completado.")
print(f"Archivo creado: {SALIDA}")
print("Archivo creado: resumen_clusters_semanticos.csv")
print("\nResumen:\n")
print(df_resumen)