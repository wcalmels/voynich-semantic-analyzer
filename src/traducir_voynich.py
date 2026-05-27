import pandas as pd

# Cargar CSV generado previamente
df = pd.read_csv("voynich_texto_completo.csv")

salida = []

salida.append("TRADUCCIÓN EXPERIMENTAL DEL MANUSCRITO VOYNICH")
salida.append("=" * 60)
salida.append("Modelo: interpretación médica contextual basada en folio, planta, uso médico y coherencia.")
salida.append("Nota: esta no es una traducción lingüística definitiva, sino una reconstrucción experimental.")
salida.append("=" * 60)
salida.append("")

for _, row in df.iterrows():
    folio = row["folio"]
    planta = row["planta"]
    uso = row["uso_medico"]
    eva = row["transcripcion_eva"]
    coherencia = row["coherencia"]

    salida.append(f"FOLIO {folio}")
    salida.append("-" * 40)
    salida.append(f"Planta / elemento probable: {planta}")
    salida.append(f"Uso médico contextual: {uso}")
    
    if isinstance(eva, str) and eva.strip():
        salida.append(f"Transcripción EVA disponible: {eva}")
    else:
        salida.append("Transcripción EVA disponible: no registrada")

    salida.append(f"Nivel de coherencia estimado: {coherencia}")

    traduccion = (
        f"Este folio parece corresponder a una receta o instrucción médica asociada a "
        f"{planta}, orientada a {uso.lower()}. "
        f"Su función probable dentro del manuscrito sería terapéutica, ritual-médica "
        f"o farmacológica, según la sección contextual del corpus."
    )

    salida.append("Traducción experimental:")
    salida.append(traduccion)
    salida.append("")

# Guardar traducción en TXT
with open("traduccion_voynich_experimental.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(salida))

print("Traducción experimental generada correctamente.")
print("Archivo creado: traduccion_voynich_experimental.txt")