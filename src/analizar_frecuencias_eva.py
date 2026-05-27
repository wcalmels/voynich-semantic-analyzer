import re
from collections import Counter
import pandas as pd

ARCHIVO_EVA = "voynich_eva_corpus.evt"

with open(ARCHIVO_EVA, "r", encoding="utf-8", errors="ignore") as f:
    contenido = f.read()

# Extraer palabras EVA
palabras = re.findall(r"\b[a-z]+\b", contenido.lower())

# Contar frecuencias
contador = Counter(palabras)

# Crear dataframe
df = pd.DataFrame(
    contador.most_common(200),
    columns=["palabra_eva", "frecuencia"]
)

# Guardar CSV
df.to_csv(
    "frecuencias_eva.csv",
    index=False,
    encoding="utf-8"
)

print("Análisis completado.")
print("Archivo generado: frecuencias_eva.csv")

print("\nTop 20 palabras EVA:\n")

for palabra, freq in contador.most_common(20):
    print(f"{palabra} -> {freq}")