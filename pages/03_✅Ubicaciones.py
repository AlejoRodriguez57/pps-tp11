import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd
import plotly.express as px
from limpiezaDatos import areas

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

mapa = generar_mapa()

def agregar_marca(row):
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['nam'],
        icon=folium.Icon()
        ).add_to(mapa)

##

areaMasSur = areas.loc[areas["lat"].idxmin()]
areaMasNorte = areas.loc[areas["lat"].idxmax()]

fig = px.scatter(
    data_frame=areas,
    x="lat",
    y="lng",
    hover_name="nam",
    title="Distribución de las áreas protegidas"
)

##

st.title("Distribución general y ubicación de las áreas protegidas")
st.write("""
En esta seccion se observa dónde se ubican las áreas protegidas, su distribución
y un mapa interactivo que ubica todas las áreas protegidas en un mapa.
""")

# Hay áreas protegidas en todas las provincias. Misiones tiene 61. Mapa.

tab_distribucion, tab_lat, tab_mapa = st.tabs([
    "Distribución",
    "Latitud máxima y mínima",
    "Mapa"
])

with tab_distribucion:
    st.subheader("Si representamos todas las ubicaciones en un gráfico de dispersión, se forma la silueta de Argentina.")
    st.plotly_chart(fig)
    st.write("Esto significa que las áreas protegidas se distribuyen mayormente cerca de las fronteras exteriores (entre países). Por ello, forman la silueta.")

with tab_lat:
    with st.expander("El área más al sur es"):
        st.write(areaMasSur)
        st.image('images/marina_yanes.avif')
    with st.expander("El área más al norte es"):
        st.write(areaMasNorte)
        st.image('images/acambuco.jpeg')
with tab_mapa:
    st.subheader("Estas son todas las áreas protegidas de Argentina.")

    ac1,ac2 = st.columns([0.3, 0.7])

    with ac1:
        r_areas = ac1.checkbox("Reservas")
        if r_areas:
            a_rev = areas[areas['tap']=="Reserva"]
            a_rev.apply(agregar_marca, axis=1)

        r_parques = ac1.checkbox("Parques")
        if r_parques:
            a_par = areas[areas['tap']=="Parque"]
            a_par.apply(agregar_marca, axis=1)

        r_monu = ac1.checkbox("Monumentos nacionales")
        if r_monu:
            a_monu = areas[areas['tap']=="Monumento Nacional"]
            a_monu.apply(agregar_marca, axis=1)

        r_nodisp = ac1.checkbox("Información no disponible")
        if r_nodisp:
            a_nodisp = areas[areas['tap']=="Información no disponible"]
            a_nodisp.apply(agregar_marca, axis=1)

    with ac2:
        st_folium(mapa, key='areas')

    st.write("Como se puede ver en el mapa, no hay ninguna provincia que no tenga áreas protegidas.")
    st.write("La provincia con más áreas protegidas es Misiones, con un total de 61.")