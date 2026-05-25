import pandas as pd
from collections import Counter

ENTRADA = "mapa_semantico_eva_limpio.csv"
SALIDA = "informe_semantico_voynich.txt"

df = pd.read_csv(ENTRADA)

lineas = []

lineas.append("INFORME SEMÁNTICO EXPERIMENTAL - MANUSCRITO VOYNICH")
lineas.append("=" * 70)
lineas.append("Modelo: análisis EVA por familias léxicas, folios, plantas y uso médico.")
lineas.append("Nota: informe experimental, no traducción definitiva.")
lineas.append("=" * 70)
lineas.append("")

conteo = Counter(df["familia"])

lineas.append("1. RESUMEN GENERAL DE FAMILIAS EVA")
lineas.append("-" * 70)

for familia, frecuencia in conteo.most_common():
    significado = df[df["familia"] == familia]["significado_probable"].iloc[0]
    lineas.append(f"Familia EVA: {familia}")
    lineas.append(f"Frecuencia: {frecuencia}")
    lineas.append(f"Significado probable: {significado}")
    lineas.append("")

lineas.append("")
lineas.append("2. ANÁLISIS POR FAMILIA")
lineas.append("-" * 70)

for familia in conteo.keys():
    sub = df[df["familia"] == familia]

    significado = sub["significado_probable"].iloc[0]
    palabras = sorted(sub["palabra_eva"].unique())
    folios = sorted(sub["folio"].astype(str).unique())
    plantas = sorted(sub["planta"].astype(str).unique())
    usos = sorted(sub["uso_medico"].astype(str).unique())

    lineas.append(f"FAMILIA: {familia}")
    lineas.append(f"Significado probable: {significado}")
    lineas.append(f"Palabras EVA asociadas: {', '.join(palabras)}")
    lineas.append(f"Folios asociados: {', '.join(folios)}")
    lineas.append(f"Plantas asociadas: {', '.join(plantas)}")
    lineas.append("Usos médicos asociados:")

    for uso in usos[:10]:
        lineas.append(f" - {uso}")

    lineas.append("")

lineas.append("")
lineas.append("3. INTERPRETACIÓN CONTEXTUAL")
lineas.append("-" * 70)
lineas.append(
    "El mapa semántico muestra una concentración de familias EVA relacionadas "
    "con preparación medicinal, agua/raíz, calor/sol/dolor, ciclos corporales "
    "y tinturas. Esta distribución es compatible con una lectura médica-formularia "
    "del corpus experimental."
)
lineas.append("")
lineas.append(
    "Las familias yka, qok, pch, dai, ata y sho podrían funcionar como raíces "
    "o marcadores semánticos recurrentes dentro de un sistema de instrucciones "
    "botánicas, farmacológicas o terapéuticas."
)
lineas.append("")
lineas.append(
    "Este resultado no constituye prueba definitiva de traducción, pero sí entrega "
    "una base estructurada para comparar el texto EVA con corpus médicos medievales, "
    "turco antiguo, persa médico, hidroterapia y astrología médica."
)

with open(SALIDA, "w", encoding="utf-8") as f:
    f.write("\n".join(lineas))

print("Informe semántico generado correctamente.")
print(f"Archivo creado: {SALIDA}")