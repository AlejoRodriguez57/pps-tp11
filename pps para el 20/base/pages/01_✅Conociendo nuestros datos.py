import pandas as pd
import streamlit as st
from utils import pie_graf
from limpiezaDatos import areas

st.title("Sobre los datos")

##

with st.expander("Cuantas areas protegidas hay en Argentina"):
    filas, columnas = areas.shape
    st.write(f'Hay { filas} Areeas protegidas en Argentina')

with st.expander("¿Qué datos tenemos de cada área protegida y qué significa cada uno?"):
    st.write("De cada área protegida tenemos estos datos:")

    st.markdown("""
    - **lat**: Latitud del área protegida sobre un mapa.
    - **lng**: Longitud del área protegida sobre un mapa.
    - **gid**: Es un identificador único.
    - **entidad**: Indica de forma simplificada (Sí/No) si un área protegida cuenta con un estatus, reconocimiento o designación oficial de conservación otorgado por una institución o tratado específico.
    - **objeto**: Hace referencia al objeto geográfico o tipo de entidad.
    - **fna**: Es la combinación de gna y nam. Aclara nombre y categoría legal.
    - **gna**: Es la categoría conceptual o legal a la que pertenece.
    - **nam**: Es el nombre propio o específico del lugar, sin incluir la categoría legal o conceptual.
    - **tap**: Indica qué tipo de área protegida es: parque, reserva o monumento nacional.
    - **jap**: Hace referencia al nivel del Estado que tiene el control legal, la administración y la propiedad.
    - **caa**: Hace referencia a la clasificación de la Autoridad Responsable. A diferencia de jap, solo diferencia entre privado y estatal, mientras que jap especifica si es municipal, provincial o nacional.
    - **fdc**: Es la fuente de datos de captura. Se utiliza principalmente para registrar la ley, decreto o resolución que creó el área y el organismo oficial que aportó los límites territoriales.
    - **sag**: Hace referencia al organismo oficial que aportó los límites territoriales.
    - **area**: Se refiere al tamaño del área protegida. No indica la medida, pero probablemente sean hectáreas (ha).
    """)

    
with st.expander("¿Que tipos de areas protegidas hay y en que proporciones?"):
    pieTap = pie_graf(areas["tap"].value_counts(), "proporcion de tipos de areas protegidas")
    st.plotly_chart(pieTap)

with st.expander("¿Que juridcciones de areas protegidas hay y en que proporciones?"):
    pieJap = pie_graf(areas["jap"].value_counts(), "proporcion de juridicciones de las areas protegidas")
    st.plotly_chart(pieJap)

st.dataframe(areas)