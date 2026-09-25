import pandas as pd
import streamlit as st

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
filas, columnas = areas.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = areas.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
nombres_ubic = areas['tap'].unique()
cant_ubic = len(areas['tap'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna tap?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna tap?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas ?"):
   
    st.write(areas.columns)

        