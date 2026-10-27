import streamlit as st
st.image('images/banner.png')

st.title("Áreas protegidas de Argentina")

st.write("""
En esta página web se van a conocer datos sobre las áreas protegidas
de Argentina, su distribución geográfica, tamaño, tipo y jurisdicción.
""")

with st.expander("¿Qué es un área protegida?"):

    st.write("""
    Es un espacio geográfico claramente delimitado y legalmente regulado
    con el fin de preservar a largo plazo el patrimonio cultural o un ecosistema.

    Por ejemplo, cerca de La Plata, un área protegida es el Parque Pereyra.
    """)

    st.image('images/parque_pereyra.jpeg')

st.header("Secciones principales de la página web")

st.subheader("1. Conociendo nuestros datos")

st.write("""
En esta sección se muestran todos los datos sobre las áreas protegidas, cuantas hay, proporciones de juridiscciones y tipos
""")

st.subheader("2. Superficies")

st.write("""
En esta sección se observa tamaño de las áreas protegidas, el promedio,
los tamaños mínimos y máximos, y cuál es el gráfico más conveniente
para ver cuál es el tamaño de área más común.
""")

st.subheader("3. Ubicaciones")

st.write("""
En esta seccion se observa dónde se ubican las áreas protegidas, su distribución
y un mapa interactivo que ubica todas las áreas protegidas en un mapa.
""")

st.subheader("⚠️ Hoy 16/10/2026 Los datos utilizados pueden estar desactualizados y no necesariamente representan la situación actual.")

st.write("fuentes utilizadas para el dataset: Instituto grafico nacional https://www.ign.gob.ar/NuestrasActividades/InformacionGeoespacial/CapasSIG")
st.markdown("""
    fuentes utilizadas para la imagen de Acambuco: https://sib.gob.ar/areas-protegidas/resprov-de-flora-y-fauna-acambuco-salta
    fuentes utilizadas para la imagen de Marina Yanes: https://www.ambito.com/informacion-general/cambio-climatico/cual-es-la-importancia-las-dos-nuevas-areas-marinas-protegidas-n5005111
    fuentes utilizadas para la imagen de Parque Pereyra: https://www.canal26.com/resizer/v2/VECA64QSXREFRDELOTMSUPPR5E.png?auth=c452f9915874b993cd22145d1501a4e92dcf0f1aa776b3dd90625e7863491833&height=675&width=1200&quality=70&smart=true
""")

# ORIGINAL
