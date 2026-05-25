import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(
    page_title="Voynich Semantic Analyzer",
    layout="wide"
)

st.title("🔓 Voynich Semantic Analyzer")
st.caption("Panel experimental EVA · glifos · familias semánticas · traducción contextual")

# -----------------------------
# CARGA DE ARCHIVOS
# -----------------------------

df_trad = None
df_sem = None

if os.path.exists("voynich_texto_traducido.csv"):
    df_trad = pd.read_csv("voynich_texto_traducido.csv")

if os.path.exists("mapa_semantico_eva_limpio.csv"):
    df_sem = pd.read_csv("mapa_semantico_eva_limpio.csv")

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("🔎 Filtros")

busqueda = st.sidebar.text_input("Buscar palabra EVA, folio, planta o uso médico")

familia_sel = "Todas"

if df_sem is not None and "familia" in df_sem.columns:
    familias = ["Todas"] + sorted(df_sem["familia"].dropna().unique().tolist())
    familia_sel = st.sidebar.selectbox("Filtrar por familia EVA", familias)

# -----------------------------
# IMAGEN PRINCIPAL
# -----------------------------

st.header("📜 Folio Voynich")

if os.path.exists("voynich_folio.jpg"):
    img = Image.open("voynich_folio.jpg")
    st.image(img, caption="Folio analizado", use_container_width=True)
else:
    st.warning("No se encontró voynich_folio.jpg")
# -----------------------------
# BUSCADOR EVA AVANZADO
# -----------------------------

st.header("🔎 Buscador EVA avanzado")

if df_sem is not None:

    termino = st.text_input(
        "Buscar en folio, planta, uso médico, palabra EVA, familia o significado"
    )

    if termino:
        t = termino.lower()

        resultados_busqueda = df_sem[
            df_sem.astype(str).apply(
                lambda row: row.str.lower().str.contains(t).any(),
                axis=1
            )
        ]

        st.write(f"Resultados encontrados: {len(resultados_busqueda)}")

        st.dataframe(
            resultados_busqueda,
            use_container_width=True
        )

        if not resultados_busqueda.empty:
            csv_busqueda = resultados_busqueda.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Descargar resultados de búsqueda",
                csv_busqueda,
                "resultados_busqueda_eva.csv",
                "text/csv"
            )

    else:
        st.info("Escribe una palabra EVA, folio, planta, familia o uso médico para buscar.")

else:
    st.warning("No se encontró mapa_semantico_eva_limpio.csv")
# -----------------------------
# MAPA SEMÁNTICO
# -----------------------------

st.header("🧠 Mapa semántico EVA")

if df_sem is not None:

    df_filtrado = df_sem.copy()

    if familia_sel != "Todas":
        df_filtrado = df_filtrado[df_filtrado["familia"] == familia_sel]

    if busqueda:
        b = busqueda.lower()
        df_filtrado = df_filtrado[
            df_filtrado.astype(str).apply(
                lambda row: row.str.lower().str.contains(b).any(),
                axis=1
            )
        ]

    st.dataframe(df_filtrado, use_container_width=True)

    st.subheader("Frecuencia por familia")
    st.bar_chart(df_filtrado["familia"].value_counts())

    csv_sem = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Descargar mapa semántico filtrado",
        csv_sem,
        "mapa_semantico_filtrado.csv",
        "text/csv"
    )

else:
    st.warning("No se encontró mapa_semantico_eva_limpio.csv")

# -----------------------------
# TRADUCCIÓN EXPERIMENTAL
# -----------------------------

st.header("📊 Traducción experimental")

if df_trad is not None:

    df_trad_filtrado = df_trad.copy()

    if busqueda:
        b = busqueda.lower()
        df_trad_filtrado = df_trad_filtrado[
            df_trad_filtrado.astype(str).apply(
                lambda row: row.str.lower().str.contains(b).any(),
                axis=1
            )
        ]

    st.dataframe(df_trad_filtrado, use_container_width=True)

    csv_trad = df_trad_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Descargar traducción filtrada",
        csv_trad,
        "voynich_traduccion_filtrada.csv",
        "text/csv"
    )

else:
    st.warning("No se encontró voynich_texto_traducido.csv")

# -----------------------------
# INFORME
# -----------------------------

st.header("📘 Informe semántico")

if os.path.exists("informe_semantico_voynich.txt"):

    with open("informe_semantico_voynich.txt", "r", encoding="utf-8") as f:
        informe = f.read()

    st.text_area("Informe generado", informe, height=450)

    st.download_button(
        "⬇️ Descargar informe",
        informe,
        "informe_semantico_voynich.txt",
        "text/plain"
    )

else:
    st.warning("No se encontró informe_semantico_voynich.txt")

# -----------------------------
# GLIFOS
# -----------------------------

st.header("🔠 Glifos extraídos")

if os.path.exists("glifos_extraidos"):

    archivos = sorted(os.listdir("glifos_extraidos"))

    cantidad = st.slider("Cantidad de glifos a mostrar", 5, min(100, len(archivos)), 30)

    columnas = st.columns(6)

    for i, archivo in enumerate(archivos[:cantidad]):
        ruta = os.path.join("glifos_extraidos", archivo)

        try:
            img = Image.open(ruta)
            columnas[i % 6].image(img, caption=archivo, use_container_width=True)
        except:
            pass

else:
    st.warning("No existe carpeta glifos_extraidos")
# -----------------------------
# MAPA DE EMBEDDINGS 2D
# -----------------------------

st.header("🧭 Mapa semántico 2D EVA vs Corpus Medieval")

if os.path.exists("mapa_embeddings_2d.png"):
    img_embed = Image.open("mapa_embeddings_2d.png")
    st.image(
        img_embed,
        caption="Mapa PCA 2D de embeddings semánticos",
        use_container_width=True
    )
else:
    st.warning("No se encontró mapa_embeddings_2d.png")

if os.path.exists("mapa_embeddings_2d.csv"):
    df_embed = pd.read_csv("mapa_embeddings_2d.csv")
    st.dataframe(df_embed, use_container_width=True)
else:
    st.warning("No se encontró mapa_embeddings_2d.csv")
    # -----------------------------
# CLUSTERS SEMÁNTICOS AUTOMÁTICOS
# -----------------------------

st.header("🧬 Clusters semánticos automáticos")

if os.path.exists("resumen_clusters_semanticos.csv"):

    df_clusters_resumen = pd.read_csv("resumen_clusters_semanticos.csv")

    st.subheader("Resumen de clusters")
    st.dataframe(df_clusters_resumen, use_container_width=True)

else:
    st.warning("No se encontró resumen_clusters_semanticos.csv")


if os.path.exists("clusters_semanticos_automaticos.csv"):

    df_clusters = pd.read_csv("clusters_semanticos_automaticos.csv")

    st.subheader("Detalle de glifos/EVA por cluster")
    st.dataframe(df_clusters, use_container_width=True)

    st.bar_chart(df_clusters["cluster_semantico"].value_counts())

else:
    st.warning("No se encontró clusters_semanticos_automaticos.csv")
st.success("Sistema Voynich cargado correctamente.")