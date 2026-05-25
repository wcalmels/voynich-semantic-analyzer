import pandas as pd

datos = [

    {
        "titulo": "Divrigi Darussifa Notes",
        "fecha": 1228,
        "idioma": "Turco medieval / Persa médico",
        "region": "Anatolia Seljúcida",
        "tema": "hidroterapia",
        "texto_original": "Su sesi ile beden dengelenir",
        "transliteracion": "su sesi ile beden dengelenir",
        "traduccion": "El cuerpo se equilibra con el sonido del agua",
        "keywords": "agua hidroterapia equilibrio cuerpo"
    },

    {
        "titulo": "Seljuk Herbal Fragment",
        "fecha": 1235,
        "idioma": "Turco medieval",
        "region": "Anatolia",
        "tema": "botánica médica",
        "texto_original": "Ot kaynatilir ve hasta icirilir",
        "transliteracion": "ot kaynatilir ve hasta icirilir",
        "traduccion": "La hierba es hervida y dada al paciente",
        "keywords": "hierba hervir medicina paciente"
    },

    {
        "titulo": "Persian Medical Treatise",
        "fecha": 1240,
        "idioma": "Persa médico",
        "region": "Persia / Anatolia",
        "tema": "medicina femenina",
        "texto_original": "Dard va garmayi ba giyahan darmān shavad",
        "transliteracion": "dard va garmayi ba giyahan darman shavad",
        "traduccion": "El dolor y el calor son tratados con hierbas",
        "keywords": "dolor calor hierbas medicina"
    },

    {
        "titulo": "Astrological Healing Notes",
        "fecha": 1250,
        "idioma": "Árabe médico",
        "region": "Anatolia",
        "tema": "astrología médica",
        "texto_original": "Al-shams yuaththir ala al-badan",
        "transliteracion": "al shams yuaththir ala al badan",
        "traduccion": "El sol influye sobre el cuerpo",
        "keywords": "sol cuerpo astrologia medicina"
    }

]

df = pd.DataFrame(datos)

df.to_csv(
    "corpus_medieval_turco.csv",
    index=False,
    encoding="utf-8"
)

print("Corpus medieval creado correctamente.")
print("Archivo generado: corpus_medieval_turco.csv")

print("\nVista previa:\n")
print(df.head())