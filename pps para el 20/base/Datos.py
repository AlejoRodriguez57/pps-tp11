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
    fuentes utilizadas para la imagen de Acambuco: https://www.google.com/imgres?q=Reserva%20Provincial%20de%20Flora%20y%20Fauna%20Acambuco&imgurl=https%3A%2F%2Fsib.gob.ar%2Farchivos%2Fthumbs%2F472x_f_acambuco.jpg&imgrefurl=https%3A%2F%2Fsib.gob.ar%2Farea%2FSALTA*AC*ACAMBUCO&docid=2jESFnOHz8d1ZM&tbnid=WB7yh6iPPKY_sM&vet=12ahUKEwiJ7pDprtCXAxXvBLkGHZ1hCBsQnPAOegUIlwEQAA..i&w=472&h=303&hcb=2&ved=2ahUKEwiJ7pDprtCXAxXvBLkGHZ1hCBsQnPAOegUIlwEQAA
    fuentes utilizadas para la imagen de Marina Yanes: https://www.ambito.com/informacion-general/cambio-climatico/cual-es-la-importancia-las-dos-nuevas-areas-marinas-protegidas-n5005111
    fuentes utilizadas para la imagen de Parque Pereyra: https://www.google.com/imgres?q=parque%20pereyra&imgurl=https%3A%2F%2Fwww.canal26.com%2Fresizer%2Fv2%2FVECA64QSXREFRDELOTMSUPPR5E.png%3Fauth%3Dc452f9915874b993cd22145d1501a4e92dcf0f1aa776b3dd90625e7863491833%26height%3D675%26width%3D1200%26quality%3D70%26smart%3Dtrue&imgrefurl=https%3A%2F%2Fwww.canal26.com%2Fturismo%2F2026%2F06%2F03%2Fparque-pereyra-iraola-la-historia-secreta-del-pulmon-verde-bonaerense-al-que-se-puede-llegar-en-tren-colectivo-o-auto%2F&docid=pS7D6a0Gru5kLM&tbnid=E5CsI8hiBbhzaM&vet=12ahUKEwiMgqiQrtCXAxWZO7kGHQcCM_wQnPAOegUIxwEQAA..i&w=1200&h=675&hcb=2&ved=2ahUKEwiMgqiQrtCXAxWZO7kGHQcCM_wQnPAOegUIxwEQAA
""")

# ORIGINAL
