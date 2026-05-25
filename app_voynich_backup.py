import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(
    page_title="Voynich Semantic Analyzer",
    layout="wide"
)

st.title("🔓 Voynich Semantic Analyzer")
st.subheader("Sistema experimental de análisis EVA y semántica contextual")

# Imagen principal
st.header("📜 Folio analizado")

if os.path.exists("voynich_folio.jpg"):
    imagen = Image.open("voynich_folio.jpg")
    st.image(imagen, caption="Voynich Folio", use_container_width=True)
else:
    st.warning("No se encontró voynich_folio.jpg")

# CSV traducido
st.header("📊 Traducción experimental")

if os.path.exists("voynich_texto_traducido.csv"):

    df_trad = pd.read_csv("voynich_texto_traducido.csv")

    st.dataframe(df_trad, use_container_width=True)

else:
    st.warning("No se encontró voynich_texto_traducido.csv")

# Mapa semántico
st.header("🧠 Mapa semántico EVA")

if os.path.exists("mapa_semantico_eva_limpio.csv"):

    df_sem = pd.read_csv("mapa_semantico_eva_limpio.csv")

    st.dataframe(df_sem, use_container_width=True)

    st.subheader("Frecuencia por familia")

    frecuencia = df_sem["familia"].value_counts()

    st.bar_chart(frecuencia)

else:
    st.warning("No se encontró mapa_semantico_eva_limpio.csv")

# Informe semántico
st.header("📘 Informe interpretativo")

if os.path.exists("informe_semantico_voynich.txt"):

    with open(
        "informe_semantico_voynich.txt",
        "r",
        encoding="utf-8"
    ) as f:

        informe = f.read()

    st.text_area(
        "Informe",
        informe,
        height=500
    )

else:
    st.warning("No se encontró informe_semantico_voynich.txt")

# Glifos
st.header("🔠 Glifos extraídos")

if os.path.exists("glifos_extraidos"):

    archivos = os.listdir("glifos_extraidos")

    columnas = st.columns(5)

    for i, archivo in enumerate(archivos[:50]):

        ruta = os.path.join("glifos_extraidos", archivo)

        try:
            img = Image.open(ruta)

            columnas[i % 5].image(
                img,
                caption=archivo,
                use_container_width=True
            )

        except:
            pass

else:
    st.warning("No existe carpeta glifos_extraidos")

st.success("Sistema Voynich cargado correctamente.")