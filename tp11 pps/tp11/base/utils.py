def pie(data, descripcion):
    return px.pie(data_frame = areas, values = data.values, names = data.index, title = {descripcion})

def line(xdata, ydata descripcion):
    return px.line(data_frame = areas, x = xdata, y = ydata, title = {descripcion})
