import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd
import plotly.express as px

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['nam'],
        icon=folium.Icon()
        ).add_to(mapa)

areas = pd.read_csv('area_protegida.csv')

areaMasSur = areas.loc[areas["lat"].idxmin()]
areaMasNorte = areas.loc[areas["lat"].idxmax()]

fig = px.pie(data_frame = p5_v1, values = p5_v1.values, names = p5_v1.index, title = "proporcion de juridcciones de las areas protegidas")

##

st.title("Distribucion general y ubicacion de las areas protegidas")

# hay areas protegidas en todas las provincias, misiones 61, mapa

st.subheader("Estan son todas las areas protegidas de la argentina")

mapa = generar_mapa()

st.write("Como se puede ver en el mapa, no hay provincia que no tenga areas protegidas")
st.write("La provincia con mas areas protegidas es Misiones con 61 areas protegidas en total")

#

ac1,ac2 = st.tabs(["Distribución", "Latud maxima y minima"])

tab_distribucion = ac1.Distribucion("Distribucion")
if tab_distribucion:
    st.subheader("Si trazamos todas las ubicaciones en un grafico de dispersion da la sirueta de argentina")
    st.plotly_chart(fig)
    st.write("Esto significa que mayormente las provincias se distribuyen en la frontera externas (entre paises). Por ello forman la silueta")

tab_lat = ac1.checkbox("Latud maxima y minima")
if tab_lat:  
    with st.expander("el area mas al sur es"):
        st.write(areaMasSur)
    with st.expander("el area mas al norte es"):
        st.write(areaMasNorte)
