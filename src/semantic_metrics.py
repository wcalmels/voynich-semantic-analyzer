import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

file_path = DATASETS_DIR / "embeddings_comparacion_eva_medieval.csv"

df = pd.read_csv(file_path)

print("\nDataset Preview:\n")
print(df.head())

numeric_df = df.select_dtypes(include=np.number)

if numeric_df.shape[1] < 2:
    print("Not enough numeric columns for cosine similarity.")
    exit()

matrix = numeric_df.values

similarity_matrix = cosine_similarity(matrix)

mean_similarity = similarity_matrix.mean()
max_similarity = similarity_matrix.max()
min_similarity = similarity_matrix.min()

print("\n=== Semantic Similarity Metrics ===\n")
print(f"Mean Similarity: {mean_similarity:.4f}")
print(f"Max Similarity : {max_similarity:.4f}")
print(f"Min Similarity : {min_similarity:.4f}")

upper_triangle = similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)]

print(f"Std Deviation  : {upper_triangle.std():.4f}")

top_pairs = []

for i in range(len(similarity_matrix)):
    for j in range(i + 1, len(similarity_matrix)):
        top_pairs.append((i, j, similarity_matrix[i][j]))

top_pairs = sorted(top_pairs, key=lambda x: x[2], reverse=True)

print("\nTop Semantic Similarity Pairs:\n")

for pair in top_pairs[:10]:
    print(pair)