import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

df = pd.read_csv(DATASETS_DIR / "real_embeddings.csv")

embedding_cols = [col for col in df.columns if str(col).isdigit()]
matrix = df[embedding_cols].values

similarity_matrix = cosine_similarity(matrix)
upper_triangle = similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)]

print("\n=== Real Semantic Embedding Metrics ===\n")
print(f"Embedding dimensions : {matrix.shape}")
print(f"Mean Similarity      : {upper_triangle.mean():.4f}")
print(f"Std Deviation        : {upper_triangle.std():.4f}")
print(f"Max Similarity       : {upper_triangle.max():.4f}")
print(f"Min Similarity       : {upper_triangle.min():.4f}")

pairs = []

for i in range(len(similarity_matrix)):
    for j in range(i + 1, len(similarity_matrix)):
        pairs.append((i, j, similarity_matrix[i][j]))

pairs = sorted(pairs, key=lambda x: x[2], reverse=True)

print("\nTop Semantic Similarity Pairs:\n")

for i, j, score in pairs[:10]:
    print(f"{i} <-> {j} | {score:.4f} | {df.iloc[i]['titulo']} <-> {df.iloc[j]['titulo']}")
