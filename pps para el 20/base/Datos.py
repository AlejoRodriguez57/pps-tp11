import streamlit as st
st.image('images/banner.png')

st.title("Áreas protegidas de Argentina")

st.write("""
En esta página web se van a conocer datos sobre las áreas protegidas
de Argentina, su distribución geográfica, tamaño, tipo y jurisdicción.
""")

with st.header("¿Qué es un área protegida?"):

    st.write("""
    Es un espacio geográfico claramente delimitado y legalmente regulado
    con el fin de preservar a largo plazo el patrimonio cultural o un ecosistema.

    Por ejemplo, cerca de La Plata, un área protegida es el Parque Pereyra.
    """)

st.header("Secciones principales de la página web")

st.subheader("1. Conociendo nuestros datos")

st.write("""
Se puede ver qué datos tiene el dataset y cuántas áreas protegidas hay.
""")

st.subheader("2. Superficies")

st.write("""
Trata sobre el tamaño de las áreas protegidas, el promedio,
los tamaños mínimos y máximos, y cuál es el gráfico más conveniente
para ver cuál es el tamaño de área más común.
""")

st.subheader("3. Ubicaciones")

st.write("""
Trata sobre dónde se ubican las áreas protegidas, su distribución
y un mapa interactivo que ubica todas las áreas protegidas en un mapa.
""")

st.subheader("⚠️ Hoy 16/10/2026 Los datos utilizados pueden estar desactualizados y no necesariamente representan la situación actual.")

st.write("fuentes utilizadas: Instituto grafico nacional https://www.ign.gob.ar/NuestrasActividades/InformacionGeoespacial/CapasSIG")

# ORIGINAL