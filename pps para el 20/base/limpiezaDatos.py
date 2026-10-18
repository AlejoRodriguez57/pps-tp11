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
    1: "Nacional",
    2: "Provincial",
    3: "Municipal",
    4: "Privado"
}
areas["jap"] = areas["jap"].replace(japFix)
