import streamlit as st

st.header("Respondé las siguientes preguntas:")

st.subheader("¿Qué es un área protegida?")

p1 = st.radio(
    "Seleccioná una respuesta:",
    [
        "Un área protegida en Argentina es un lugar de la naturaleza que se cuida de forma especial para proteger la fauna y la flora",
        "Es un espacio geográfico delimitado y regulado con el fin de preservar a largo plazo, ya sea un ecosistema o un patrimonio cultural",
        "Es un territorio resguardado por ley para salvar especies en peligro",
    ],
    horizontal=False,
    index=None
)

if p1 == "Es un espacio geográfico delimitado y regulado con el fin de preservar a largo plazo, ya sea un ecosistema o un patrimonio cultural":
    st.write("Correcto")
elif p1 == None:
    pass
else:
    st.write("Incorrecto")


st.subheader("¿El promedio es una medida?")

p2 = st.radio(
    "Seleccioná una respuesta:",
    [
        "En absoluto, es muy imprecisa para todos los casos",
        "Es correcta y siempre sirve",
        "Es precisa cuando no hay valores que se separen demasiado de la mayoría",
    ],
    horizontal=False,
    index=None
)

if p2 == "Es precisa cuando no hay valores que se separen demasiado de la mayoría":
    st.write("Correcto")
elif p2 == None:
    pass
else:
    st.write("Incorrecto")



st.subheader("¿Hay una distribución clara en cuanto a dónde se ubican las áreas protegidas?")

p3 = st.radio(
    "Seleccioná una respuesta:",
    [
        "Sí, están todas en las fronteras con otros países y el mar; por ello, forman la silueta de Argentina con precisión",
        "Están por todos lados, pero hay una tendencia clara hacia las fronteras externas, el mar y las fronteras internas (entre provincias)",
        "No la hay; están esparcidas aleatoriamente en Argentina",
    ],
    horizontal=False,
    index=None
)

if p3 == "Están por todos lados, pero hay una tendencia clara hacia las fronteras externas, el mar y las fronteras internas (entre provincias)":
    st.write("Correcto")
elif p3 == None:
    pass
else:
    st.write("Incorrecto")
