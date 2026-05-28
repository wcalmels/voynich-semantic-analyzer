import random
from pathlib import Path

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

INPUT_FILE = DATASETS_DIR / "embeddings_comparacion_eva_medieval.csv"
OUTPUT_FILE = DATASETS_DIR / "randomized_eva_baseline_results.csv"

RANDOM_SEED = 47
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


def summarize_similarity(matrix):
    upper = matrix[np.triu_indices_from(matrix, k=1)]
    return {
        "mean_similarity": float(upper.mean()),
        "std_similarity": float(upper.std()),
        "max_similarity": float(upper.max()),
        "min_similarity": float(upper.min()),
    }


def main():
    df = pd.read_csv(INPUT_FILE)

    required_columns = ["titulo", "keywords"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    original_texts = (
        df["titulo"].astype(str) + " " + df["keywords"].astype(str)
    ).tolist()

    randomized_keywords = []

    for keywords in df["keywords"].astype(str):
        tokens = keywords.split()
        random.shuffle(tokens)
        randomized_keywords.append(" ".join(tokens))

    randomized_texts = (
        df["titulo"].astype(str) + " " + pd.Series(randomized_keywords)
    ).tolist()

    original_embeddings = model.encode(original_texts)
    randomized_embeddings = model.encode(randomized_texts)

    original_similarity = cosine_similarity(original_embeddings)
    randomized_similarity = cosine_similarity(randomized_embeddings)

    original_summary = summarize_similarity(original_similarity)
    randomized_summary = summarize_similarity(randomized_similarity)

    results = []

    for metric in original_summary:
        original_value = original_summary[metric]
        randomized_value = randomized_summary[metric]

        results.append({
            "metric": metric,
            "original": original_value,
            "randomized_baseline": randomized_value,
            "difference": original_value - randomized_value
        })

    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_FILE, index=False)

    print("\n=== Randomized EVA Baseline Analysis ===\n")
    print(results_df.to_string(index=False))
    print(f"\nSaved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()