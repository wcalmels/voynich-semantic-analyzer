import pandas as pd
import re
from collections import Counter

ARCHIVO = "voynich_texto_completo.csv"

df = pd.read_csv(ARCHIVO)

palabras = []

for texto in df["transcripcion_eva"].fillna(""):

    tokens = re.findall(r"[a-zA-Z]+", str(texto).lower())

    palabras.extend(tokens)

# Longitudes
longitudes = [len(p) for p in palabras]

# Prefijos
prefijos = Counter()

# Sufijos
sufijos = Counter()

for palabra in palabras:

    if len(palabra) >= 3:

        prefijos[palabra[:3]] += 1
        sufijos[palabra[-3:]] += 1

print("\nTOP PREFIJOS:\n")

for p, f in prefijos.most_common(20):
    print(p, "->", f)

print("\nTOP SUFIJOS:\n")

for s, f in sufijos.most_common(20):
    print(s, "->", f)

print("\nESTADÍSTICAS:\n")

print("Total palabras:", len(palabras))
print("Longitud promedio:", round(sum(longitudes)/len(longitudes), 2))
print("Longitud máxima:", max(longitudes))
print("Longitud mínima:", min(longitudes))