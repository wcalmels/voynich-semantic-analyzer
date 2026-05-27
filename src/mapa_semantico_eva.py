import pandas as pd
import re
from collections import defaultdict, Counter

ARCHIVO = "voynich_texto_completo.csv"
SALIDA = "mapa_semantico_eva.csv"

df = pd.read_csv(ARCHIVO)

familias = {
    "qok": "líquidos / raíz / medicina",
    "yka": "preparación / hervido / escaldado",
    "sho": "sol / calor / dolor",
    "pch": "corte / raíz / mezcla",
    "dai": "ciclo / repetición / menstruación",
    "ata": "tintura / preparación",
    "cth": "número / medida / proporción",
    "qot": "perforar / abrir / canalizar",
    "fac": "hacer / ejecutar acción"
}

registros = []

for _, row in df.iterrows():
    folio = row.get("folio", "")
    uso = row.get("uso_medico", "")
    planta = row.get("planta", "")
    texto = str(row.get("transcripcion_eva", ""))

    palabras = re.findall(r"[a-zA-Z]+", texto.lower())

    for palabra in palabras:
        familia_detectada = "desconocida"
        significado = "pendiente"

        for prefijo, significado_familia in familias.items():
            if palabra.startswith(prefijo):
                familia_detectada = prefijo
                significado = significado_familia
                break

        registros.append({
            "folio": folio,
            "planta": planta,
            "uso_medico": uso,
            "palabra_eva": palabra,
            "familia": familia_detectada,
            "significado_probable": significado,
            "longitud": len(palabra)
        })

df_mapa = pd.DataFrame(registros)

df_mapa.to_csv(SALIDA, index=False, encoding="utf-8")

print("Mapa semántico EVA generado.")
print(f"Archivo creado: {SALIDA}")

print("\nResumen por familia:\n")

conteo = Counter(df_mapa["familia"])

for familia, frecuencia in conteo.most_common():
    print(f"{familia} -> {frecuencia}")