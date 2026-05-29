import random
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


INPUT_FILE = "datasets/embeddings_comparacion_eva_medieval.csv"
OUTPUT_FILE = "datasets/randomized_100_runs_results.csv"

N_RUNS = 100

print("Loading dataset...")
df = pd.read_csv(INPUT_FILE)

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

original_texts = (
    df["titulo"].astype(str)
    + " "
    + df["keywords"].astype(str)
).tolist()

print("Generating original embeddings...")
original_embeddings = model.encode(original_texts)

original_similarity = cosine_similarity(original_embeddings)

original_upper = original_similarity[
    np.triu_indices_from(original_similarity, k=1)
]

original_mean = float(original_upper.mean())

print(f"\nOriginal Mean Similarity: {original_mean:.6f}")

results = []

print("\nRunning randomized baselines...\n")

for run in range(N_RUNS):

    randomized_keywords = []

    for keywords in df["keywords"].astype(str):

        tokens = keywords.split()

        random.shuffle(tokens)

        randomized_keywords.append(
            " ".join(tokens)
        )

    randomized_texts = (
        df["titulo"].astype(str)
        + " "
        + pd.Series(randomized_keywords)
    ).tolist()

    randomized_embeddings = model.encode(randomized_texts)

    randomized_similarity = cosine_similarity(
        randomized_embeddings
    )

    randomized_upper = randomized_similarity[
        np.triu_indices_from(
            randomized_similarity,
            k=1
        )
    ]

    mean_similarity = float(
        randomized_upper.mean()
    )

    results.append(mean_similarity)

    if (run + 1) % 10 == 0:
        print(
            f"Completed {run + 1}/{N_RUNS}"
        )

results = np.array(results)

summary = pd.DataFrame({
    "metric": [
        "original_mean",
        "randomized_mean",
        "randomized_std",
        "randomized_min",
        "randomized_max"
    ],
    "value": [
        original_mean,
        results.mean(),
        results.std(),
        results.min(),
        results.max()
    ]
})

summary.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n=== RESULTS ===\n")

print(summary)

print("\nDifference:")
print(
    original_mean - results.mean()
)

print(
    f"\nSaved to: {OUTPUT_FILE}"
)