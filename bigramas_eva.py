import re
from collections import Counter
import pandas as pd

ARCHIVO_EVA = "voynich_eva_corpus.evt"

with open(
    ARCHIVO_EVA,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    contenido = f.read().lower()

# Extraer palabras EVA
palabras = re.findall(r"\b[a-z]+\b", contenido)

# Crear bigramas
bigramas = []

for i in range(len(palabras)-1):

    bigrama = palabras[i] + " " + palabras[i+1]

    bigramas.append(bigrama)

# Contar frecuencia
contador = Counter(bigramas)

# Crear dataframe
df = pd.DataFrame(
    contador.most_common(200),
    columns=["bigrama", "frecuencia"]
)

# Guardar CSV
df.to_csv(
    "bigramas_eva.csv",
    index=False,
    encoding="utf-8"
)

print("Análisis de bigramas completado.")
print("Archivo generado: bigramas_eva.csv")

print("\nTop 20 bigramas EVA:\n")

for bigrama, freq in contador.most_common(20):

    print(f"{bigrama} -> {freq}")