import plotly.express as px


def pie_graf(data, descripcion):
    return px.pie(values=data.values, names=data.index, title=descripcion)


def bar_graf(xdata, ydata, descripcion):
    return px.bar(x=xdata, y=ydata, title=descripcion)
