"""
Traduce todas las transcripciones EVA del CSV usando el decodificador Riemann.
Genera un nuevo CSV con las columnas originales + traducción.
"""

import pandas as pd
from decodificador_voynich import traducir_linea

# Cargar el CSV con las transcripciones
df = pd.read_csv("voynich_texto_completo.csv", encoding='utf-8')

# Añadir columnas para las traducciones
df['traduccion_espanol'] = ""
df['traduccion_ingles'] = ""

# Recorrer cada fila y traducir si hay transcripción EVA
for idx, row in df.iterrows():
    eva = row['transcripcion_eva']
    if pd.notna(eva) and eva.strip():
        # Traducir al español (el contexto por defecto es herbolaria)
        try:
            trad_es = traducir_linea(eva, contexto="herbolaria")
            # Para inglés podemos usar el mismo diccionario o crear uno aparte
            trad_en = traducir_linea(eva, contexto="herbolaria")  # mejorable
        except Exception as e:
            trad_es = f"[Error: {e}]"
            trad_en = ""
        df.at[idx, 'traduccion_espanol'] = trad_es
        df.at[idx, 'traduccion_ingles'] = trad_en
    else:
        df.at[idx, 'traduccion_espanol'] = ""
        df.at[idx, 'traduccion_ingles'] = ""

# Guardar el resultado
df.to_csv("voynich_texto_traducido.csv", index=False, encoding='utf-8')
print("✅ Traducción completada. Archivo guardado: voynich_texto_traducido.csv")
print("\nVista previa de las primeras traducciones:")
print(df[['folio', 'transcripcion_eva', 'traduccion_espanol']].head(10))
