import pandas as pd

ENTRADA = "mapa_semantico_eva.csv"
SALIDA = "mapa_semantico_eva_limpio.csv"

df = pd.read_csv(ENTRADA)

# Eliminar filas sin palabra EVA válida
df = df.dropna(subset=["palabra_eva"])

# Convertir a texto
df["palabra_eva"] = df["palabra_eva"].astype(str).str.strip().str.lower()

# Filtrar palabras vacías, demasiado cortas o ruido
df_limpio = df[
    (df["palabra_eva"] != "") &
    (df["palabra_eva"].str.len() >= 3) &
    (df["familia"] != "desconocida")
]

# Guardar limpio
df_limpio.to_csv(SALIDA, index=False, encoding="utf-8")

print("Mapa semántico limpio generado.")
print(f"Archivo creado: {SALIDA}")
print(f"Registros originales: {len(df)}")
print(f"Registros limpios: {len(df_limpio)}")

print("\nResumen limpio por familia:\n")
print(df_limpio["familia"].value_counts())