import pandas as pd
import streamlit as st
import plotly.express as px
import pie from "../utils.py"

areas =  pd.read_csv('area_protegida.csv')
st.title("Sobre el dataset")
st.write("Explicación de las columnas y qué representan")
filas, columnas = areas.shape

##

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = areas.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
with st.expander("¿Que tipos de areas protegidas hay y en que proporciones?"):
    pieTap = pie(areas["tap"].value_counts(), "prorcion de tipos de areas protegidas")
    st.plotly_chart(pieTap)

with st.expander("¿Que juridcciones de areas protegidas hay y en que proporciones?"):
    pieTap = pie(areas["jap"].value_counts(), "prorcion de juridicciones de las areas protegidas")
    st.plotly_chart(pieTap)