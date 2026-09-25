import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

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

areas = pd.read_csv('area_protegida.csv')
st.title("Mapa")
mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['nam'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])

r_parque = ac1.checkbox("Areas de tipo parque")
if r_parque:
    a_par = areas[areas['tap']==1]
    a_par.apply(agregar_marca_aerop, axis=1)

r_reserva = ac1.checkbox("Areas de tipo reserva")
if r_reserva:
    a_rev = areas[areas['tap']==2]
    a_rev.apply(agregar_marca_aerop, axis=1)

r_monumento = ac1.checkbox("Areas de tipo monumento nacional")
if r_monumento:
    a_mon = areas[areas['tap']==3]
    a_mon.apply(agregar_marca_aerop, axis=1)

r_desconocido = ac1.checkbox("Areas de las que se desconoce su tipo")
if r_desconocido:
    a_des = areas[areas['tap']==0]
    a_des.apply(agregar_marca_aerop, axis=1)

with ac2:
    st_folium(mapa, key='areas')
