import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
VIS_DIR = BASE_DIR / "visualizations"

VIS_DIR.mkdir(exist_ok=True)

def plot_frequency_distribution():
    file_path = DATASETS_DIR / "frecuencias_eva.csv"

    if not file_path.exists():
        print(f"Missing file: {file_path}")
        return

    df = pd.read_csv(file_path)

    print(df.head())

    x_col = df.columns[0]
    y_col = df.columns[1]

    top = df.sort_values(y_col, ascending=False).head(20)

    plt.figure(figsize=(12, 6))
    plt.bar(top[x_col].astype(str), top[y_col])
    plt.title("Top 20 EVA Token Frequency Distribution")
    plt.xlabel("EVA Token")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(VIS_DIR / "eva_frequency_distribution.png", dpi=300)
    plt.close()

def plot_embedding_projection():
    file_path = DATASETS_DIR / "mapa_embeddings_2d.csv"

    if not file_path.exists():
        print(f"Missing file: {file_path}")
        return

    df = pd.read_csv(file_path)

    print(df.head())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) < 2:
        print("Not enough numeric columns for embedding projection.")
        return

    x_col, y_col = numeric_cols[0], numeric_cols[1]

    plt.figure(figsize=(9, 7))
    plt.scatter(df[x_col], df[y_col], s=35, alpha=0.75)
    plt.title("Semantic Embedding Projection")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.savefig(VIS_DIR / "semantic_embedding_projection.png", dpi=300)
    plt.close()

def plot_cluster_summary():
    file_path = DATASETS_DIR / "resumen_clusters_semanticos.csv"

    if not file_path.exists():
        print(f"Missing file: {file_path}")
        return

    df = pd.read_csv(file_path)

    print(df.head())

    x_col = df.columns[0]
    y_col = df.columns[1]

    plt.figure(figsize=(10, 6))
    plt.bar(df[x_col].astype(str), df[y_col])
    plt.title("Semantic Cluster Summary")
    plt.xlabel("Cluster")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(VIS_DIR / "semantic_cluster_summary.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_frequency_distribution()
    plot_embedding_projection()
    plot_cluster_summary()
    print("Research figures generated successfully.")