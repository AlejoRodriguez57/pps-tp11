import plotly.express as px
import pandas as pd
import streamlit as st

areas =  pd.read_csv('area_protegida.csv')

# datos #

tapFix = {
    0: "Información no disponible",
    1: "Parque",
    2: "Reserva",
    3: "Monumento Nacional"
}
areas["tap"] = areas["tap"].replace(tapFix)

japFix = {
    -1: "Información no disponible",
    0: "Información no disponible",
    2: "Nacional",
    3: "Provincial",
    4: "Municipal",
    5: "Privado"
}
areas["jap"] = areas["jap"].replace(japFix)
