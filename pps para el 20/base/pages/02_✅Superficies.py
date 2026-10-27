import streamlit as st
import pandas as pd
from utils import bar_graf, scatter_and_meanLine
from limpiezaDatos import areas

mediaSuperficieAreas = areas["area"].mean()

AreasSantaCruz = areas[
    (areas["lat"] <= -46)
    & (areas["lat"] >= -52)]

mediaSuperficieSAreasSantaCruz = AreasSantaCruz["area"].mean()

CincoAreasMasGrandes = areas.sort_values(by="area", ascending=False).head(5)
CincoAreasMasChicas = areas.sort_values(by="area", ascending=True).head(5)

##

st.title("Sobre el tamaño de las áreas protegidas")
st.write("""
En esta sección se observa tamaño de las áreas protegidas, el promedio,
los tamaños mínimos y máximos, y cuál es el gráfico más conveniente
para ver cuál es el tamaño de área más común.

No se indica la unidad de medida, pero probablemente sean hectáreas (ha).")
""")

tab_maximosYMinimos, tab_promedios = st.tabs([
    "Máximos y mínimos",
    "Promedios",
])

with tab_maximosYMinimos:
    st.subheader("Las 5 áreas protegidas más grandes son")
    st.write(CincoAreasMasGrandes)

    st.subheader("Las 5 áreas protegidas más pequeñas son")
    st.write(CincoAreasMasChicas)

with tab_promedios:
    st.subheader(f"El promedio del tamaño de las áreas protegidas es de: {mediaSuperficieAreas}")

    st.subheader("Aproximadamente 4 de cada 5 áreas protegidas están por debajo de ese promedio")

    st.write(f"Por ejemplo, en Santa Cruz, el promedio de la superficie de las áreas protegidas es de: {mediaSuperficieSAreasSantaCruz}")

    with st.expander("Explicación de por qué el promedio del tamaño de las áreas protegidas de Santa Cruz es tan bajo"):
        st.write("Esto se debe a que el promedio es muy sensible a los valores extremos, que pueden elevarlo o reducirlo considerablemente, incluso cuando corresponden a unos pocos datos. En este caso, hay unas pocas áreas protegidas con una superficie muy grande, lo que hace que el promedio se eleve por encima de la superficie de la mayoría de las áreas protegidas. Aproximadamente 4 de cada 5 áreas protegidas están por debajo del promedio.")
        st.write("Esto no significa que el promedio no sirva; su utilidad depende de para qué se use. Si queremos conocer los valores más frecuentes, una buena opción es utilizar un gráfico de frecuencias, que muestra cuántas veces aparece cada valor.")

        with st.expander("Ejemplo de un gráfico de frecuencias"):
            barFrec = bar_graf(areas["area"].value_counts().index, areas["area"].value_counts().values, "Gráfico de frecuencias")
            st.plotly_chart(barFrec)

            st.write("Por el tipo de datos que estamos representando, el gráfico puede resultar un poco extraño a primera vista, pero eso no significa que sea incorrecto. En el eje Y se muestra la frecuencia, es decir, cuántas áreas protegidas tienen exactamente la misma superficie. En el eje X se representan las superficies. Según los datos, la gran mayoría de las áreas protegidas tienen una superficie de entre 0 y 4 millones.")