import streamlit as st
import pandas as pd

import streamlit as st
import plotly.express as px

areas = pd.read_csv('area_protegida.csv')

fig = px.scatter(data_frame = areas, x = areas["lat"], y = areas["lng"], title = "¿Hay relacion entre latitud y longitud?")
st.plotly_chart(fig)