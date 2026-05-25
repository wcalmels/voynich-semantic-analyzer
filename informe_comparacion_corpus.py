import pandas as pd

ENTRADA = "comparacion_eva_corpus_medieval.csv"
SALIDA = "informe_comparacion_eva_corpus_medieval.txt"

df = pd.read_csv(ENTRADA)

lineas = []

lineas.append("INFORME DE COMPARACIÓN EVA VS CORPUS MÉDICO MEDIEVAL")
lineas.append("=" * 70)
lineas.append("Marco: comparación experimental entre familias EVA y corpus medieval contextual.")
lineas.append("Nota: no constituye prueba definitiva de traducción; es evidencia exploratoria.")
lineas.append("=" * 70)
lineas.append("")

lineas.append("1. RANKING DE SIMILITUD CONTEXTUAL")
lineas.append("-" * 70)

for _, row in df.iterrows():
    lineas.append(f"Título: {row['titulo']}")
    lineas.append(f"Fecha: {row['fecha']}")
    lineas.append(f"Idioma: {row['idioma']}")
    lineas.append(f"Región: {row['region']}")
    lineas.append(f"Tema: {row['tema']}")
    lineas.append(f"Score de coincidencia: {row['score_coincidencia']}")
    lineas.append(f"Coincidencias: {row['coincidencias_semanticas']}")
    lineas.append(f"Keywords: {row['keywords']}")
    lineas.append("")

lineas.append("2. INTERPRETACIÓN")
lineas.append("-" * 70)
lineas.append(
    "Los mayores puntajes aparecen en fragmentos asociados a medicina femenina, "
    "dolor, calor, preparación herbal, ginecología y astrología médica. "
    "Esto es compatible con una hipótesis contextual médico-botánica, aunque "
    "todavía requiere ampliación del corpus y validación estadística formal."
)
lineas.append("")
lineas.append(
    "La aparición recurrente de términos como ciclo, calor, dolor, medicina, "
    "hierbas, agua, sol y luna sugiere que las familias EVA experimentales "
    "podrían estar capturando dominios semánticos próximos a un corpus médico "
    "medieval anatolio/persa."
)
lineas.append("")
lineas.append(
    "El resultado más prometedor no debe interpretarse como traducción directa, "
    "sino como alineamiento semántico contextual entre estructuras EVA y un "
    "marco médico medieval restringido."
)

with open(SALIDA, "w", encoding="utf-8") as f:
    f.write("\n".join(lineas))

print("Informe de comparación generado correctamente.")
print(f"Archivo creado: {SALIDA}")