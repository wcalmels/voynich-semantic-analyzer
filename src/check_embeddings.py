import pandas as pd

df = pd.read_csv("datasets/embeddings_comparacion_eva_medieval.csv")

print("\nCOLUMNS:\n")
print(df.columns)

print("\nDTYPES:\n")
print(df.dtypes)

print("\nHEAD:\n")
print(df.head())
