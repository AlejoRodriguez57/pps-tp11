import plotly.express as px

def pie_graf(data, descripcion):
    return px.pie(values=data.values, names=data.index, title=descripcion)


def bar_graf(xdata, ydata, descripcion):
    return px.bar(x=xdata, y=ydata, title=descripcion)

def scatter_and_meanLine(xdata, ydata, mean, descripcion):
    fig = px.scatter(x=xdata, y=ydata, title=descripcion)
    fig.add_hline(
        y=mean,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Promedio: {mean:.2f}",
        annotation_position="bottom right"
    )

    return fig