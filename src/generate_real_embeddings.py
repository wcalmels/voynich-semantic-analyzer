from sentence_transformers import SentenceTransformer
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

input_file = DATASETS_DIR / "embeddings_comparacion_eva_medieval.csv"
output_file = DATASETS_DIR / "real_embeddings.csv"

df = pd.read_csv(input_file)

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = (
    df["titulo"].astype(str) + " " +
    df["keywords"].astype(str)
).tolist()

embeddings = model.encode(texts)

embeddings_df = pd.DataFrame(embeddings)

final_df = pd.concat([df, embeddings_df], axis=1)

final_df.to_csv(output_file, index=False)

print("\nReal embeddings generated successfully.")
print(f"\nSaved to: {output_file}")
print(f"\nEmbedding dimensions: {embeddings.shape}")