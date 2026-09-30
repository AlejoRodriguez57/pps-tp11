import streamlit as st
import pandas as pd
import line from "../utils.py"

areas = pd.read_csv('area_protegida.csv')

mediaSuperficieAreas = areas.mean()

AreasSantaCruz = areas[
    (areas["lat"] <= -46)
    & (areas["lat"] >= -52)]

mediaSuperficieSAreasSantaCruz = AreasSantaCruz["area"].mean()

CincoAreasMasGrandes = areas.sort_values(by="area", ascending=False).head(5)

##

st.title("Sobre las el tamaño de las areas protegidas")

# 5 areas mas grandes

with st.expander("Las 5 areas protegidsa mas grandes son protegidas son"):
    st.write(CincoAreasMasGrandes)

# media

st.subheader("El promedio de todas las areas protegidas son:")

with st.expander("promedio de las areas protegidas"):
    st.write(mediaSuperficieAreas)

# media de santa cruz

st.subheader("La mayoria de las areas protegidas estan por debajo del promedio")

with st.expander("areas de santa cruz"):
    st.write(mediaSuperficieSAreasSantaCruz)

    with st.expander("explicacion de por que esta tan por debajo del promedio el tamaño de las areas protegidas de santa cruz"):

        st.write("  Esto se debe a que el promedio reacciona mucho a los valores extremos, elevenadolo o reduciendolo por unas pocos datos. En este caso hay unas pocas areas protegidas con un area muy grande haciendo que el promedio se eleve, descartando la mayoria de las areas protegidas; aproximadamente 4 de cada 5 areas protegidas estan por debajo del promedio")
        st.write(" Esto no significa que el promedio no sirva, depende para que se use. En el caso de que solo quieras ver los datos mas comunes la mejor manera es hacer un Moda, que es un grafico que muestra los valores mas comunes.")
        
        with st.expander("ejemplo de grafico moda"):
            line(areas["areas"].value_counts().name, areas["areas"].value_counts().index, "grafico moda")