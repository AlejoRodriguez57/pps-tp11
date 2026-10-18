import streamlit as st

st.subheader("¿Qué es un área protegida?")

p1 = st.radio(
    "Seleccioná una respuesta:",
    [
        "Una área protegida en Argentina es un lugar de la naturaleza que se cuida de forma especial para proteger fauna y flora",
        "Es un espacio geográfico delimitado y regulado con el fin de preservar a largo plazo ya sea un ecosistema o patrimonio cultural",
        "Es un territorio resguardado por ley para salvar especies en peligro",
    ],
    horizontal=False,
    index=None
)

if p1 == "Es un espacio geográfico delimitado y regulado con el fin de preservar a largo plazo ya sea un ecosistema o patrimonio cultural":
    st.write("Correcto")
else:
    st.write("Incorrecto")


st.subheader("¿El promedio es una medida?")

p2 = st.radio(
    "Seleccioná una respuesta:",
    [
        "En absoluto, es muy imprecisa para todos los casos",
        "Es correcta y siempre sirve",
        "Es preciso cuando no hay valores que no se separen demasiado de la mayoría",
    ],
    horizontal=False,
    index=None
)

if p2 == "Es preciso cuando no hay valores que no se separen demasiado de la mayoría":
    st.write("Correcto")
else:
    st.write("Incorrecto")


st.subheader("¿Hay una distribución clara en cuanto a dónde se ubican las áreas protegidas?")

p3 = st.radio(
    "Seleccioná una respuesta:",
    [
        "Sí, están todas en las fronteras con otros países y el mar, por ello forman la silueta de Argentina con precisión",
        "Están por todos lados pero hay una tendencia clara a las fronteras externas, mar y fronteras internas (entre provincias)",
        "No la hay, están esparcidas aleatoriamente en Argentina",
    ],
    horizontal=False,
    index=None
)

if p3 == "Están por todos lados pero hay una tendencia clara a las fronteras externas, mar y fronteras internas (entre provincias)":
    st.write("Correcto")
else:
    st.write("Incorrecto")