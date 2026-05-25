import pandas as pd

ARCHIVO = "corpus_medieval_turco.csv"
SALIDA = "corpus_medieval_turco_expandido.csv"

df = pd.read_csv(ARCHIVO)

nuevos_datos = [
    {
        "titulo": "Divrigi Darussifa Hydrotherapy Fragment",
        "fecha": 1228,
        "idioma": "Turco medieval / Persa médico",
        "region": "Anatolia Seljúcida",
        "tema": "hidroterapia médica",
        "texto_original": "Su ile beden arinir ve dard azalir",
        "transliteracion": "su ile beden arinir ve dard azalir",
        "traduccion": "Con agua el cuerpo se purifica y el dolor disminuye",
        "keywords": "agua cuerpo purificacion dolor hidroterapia medicina"
    },
    {
        "titulo": "Seljuk Women's Medicine Fragment",
        "fecha": 1230,
        "idioma": "Turco medieval",
        "region": "Anatolia",
        "tema": "medicina femenina",
        "texto_original": "Ay devri ve beden harareti ot ile dengelenir",
        "transliteracion": "ay devri ve beden harareti ot ile dengelenir",
        "traduccion": "El ciclo lunar y el calor corporal se equilibran con hierbas",
        "keywords": "luna ciclo cuerpo calor hierbas medicina femenina"
    },
    {
        "titulo": "Seljuk Herbal Preparation Fragment",
        "fecha": 1235,
        "idioma": "Turco medieval",
        "region": "Anatolia",
        "tema": "preparacion herbal",
        "texto_original": "Ot kaynatilir su ile karistirilir",
        "transliteracion": "ot kaynatilir su ile karistirilir",
        "traduccion": "La hierba se hierve y se mezcla con agua",
        "keywords": "hierba hervir agua mezcla preparacion medicina"
    },
    {
        "titulo": "Persian Gynecological Note",
        "fecha": 1245,
        "idioma": "Persa médico",
        "region": "Persia / Anatolia",
        "tema": "ginecologia medieval",
        "texto_original": "Dard va gardesh ba giyah va ab darmān shavad",
        "transliteracion": "dard va gardesh ba giyah va ab darman shavad",
        "traduccion": "El dolor y el ciclo son tratados con hierba y agua",
        "keywords": "dolor ciclo hierba agua tratamiento ginecologia"
    },
    {
        "titulo": "Astrological Medicine Lunar Fragment",
        "fecha": 1250,
        "idioma": "Árabe médico / Persa",
        "region": "Anatolia",
        "tema": "astrologia medica",
        "texto_original": "Al-qamar wa al-shams yuaththiran fi badan al-marid",
        "transliteracion": "al qamar wa al shams yuaththiran fi badan al marid",
        "traduccion": "La luna y el sol influyen en el cuerpo del paciente",
        "keywords": "luna sol cuerpo paciente astrologia medicina"
    },
    {
        "titulo": "Medieval Tincture Preparation",
        "fecha": 1260,
        "idioma": "Persa médico / Turco medieval",
        "region": "Anatolia",
        "tema": "farmacopea",
        "texto_original": "Rangin darman su va ot ile hazirlanir",
        "transliteracion": "rangin darman su va ot ile hazirlanir",
        "traduccion": "La tintura medicinal se prepara con agua y hierbas",
        "keywords": "tintura medicina agua hierbas preparacion"
    }
]

df_nuevo = pd.DataFrame(nuevos_datos)

df_expandido = pd.concat([df, df_nuevo], ignore_index=True)

df_expandido.to_csv(SALIDA, index=False, encoding="utf-8")

print("Corpus medieval expandido creado.")
print(f"Archivo generado: {SALIDA}")
print(f"Registros totales: {len(df_expandido)}")
print(df_expandido[["titulo", "fecha", "tema", "keywords"]])