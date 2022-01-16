import copy
## import von numpy fuer arrays und wesentliches mathematische Funktionen
import numpy as np
## import von plotly fuer die Graphen
import plotly
import plotly.graph_objs._figure
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class plot(go.Figure):
    result = None

    def __init__(self, *args):
        go.Figure.__init__(self, *args)

    def plot_contour(self, xmin, xmax, ymin, ymax, function):
        x_axis = np.linspace(xmin, xmax, 100)
        y_axis = np.linspace(ymin, ymax, 100)
        [x, y] = np.meshgrid(x_axis, y_axis)
        z = function([x, y])
        self.add_trace(go.Contour(x=x_axis, y=y_axis, z=z, contours_coloring='lines'))
        self.update_layout(template='plotly_white', width=500, height=500)

    def add_gradients(self, gradf):
        for X in range(-4, 1):
            for Y in range(-2, 3):
                self.add_annotation(
                    ax=X,  # arrows' head
                    ay=Y,  # arrows' head
                    x=X + gradf([X, Y])[0],  # arrows' tail
                    y=Y + gradf([X, Y])[1],  # arrows' tail
                    xref='x',
                    yref='y',
                    axref='x',
                    ayref='y',
                    text='',  # if you want only the arrow
                    showarrow=True,
                    arrowhead=2,
                    # arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='red')

    def add_gradient_descent(self, x0, function, grad, gamma=1, Iterationen=10, color=None, Nebenbedingung=None):
        x = np.zeros(shape=(Iterationen + 1, 2))
        x[0, :] = np.array(x0)
        for i in range(Iterationen):
            x[i + 1] = -gamma * grad(x[i, :]) + x[i, :]
        f_x = np.round(function(x[-1]), 3)
        if not color is None:
            self.add_scatter(
                x=x[:, 0],
                y=x[:, 1],
                mode='lines+markers',
                showlegend=False,
                line_color=color)
        else:
            self.add_scatter(
                x=x[:, 0],
                y=x[:, 1],
                mode='lines+markers',
                showlegend=False,
                line_color=color)
        self.result = x[-1]
        if Nebenbedingung is None:
            self.update_layout(title="x0=" + str(np.round(x0, 3)) + ", gamma =" +
                                     str(np.round(gamma, 3)) + ",<br> Iterationen=" + str(Iterationen) +
                                     ", f(x)=" + str(np.round(f_x, 3)) + ", x=" + str(np.round(self.result, 3)))
        else:
            self.update_layout(title="x0=" + str(np.round(x0, 3)) + ", gamma =" +
                                     str(np.round(gamma, 3)) + ",<br> Iterationen=" + str(Iterationen) +
                                     ", f(x)=" + str(np.round(f_x, 3)) + ", h(x) = "
                                     + str(np.round(Nebenbedingung(self.result), 3))
                                     + ",<br> x=" + str(np.round(self.result, 3)))

    def add_h(self):
        def h_(x):
            return x ** 3 + 9 * x ** 2 + 27 * x + 27
        xmin = self.data[0]['x'].min()
        xmax = self.data[0]['x'].max()
        ymin = self.data[0]['y'].min()
        ymax = self.data[0]['y'].max()
        x = [x for x in np.linspace(xmin, xmax, 1000) if ymin <= h_(x) <= ymax]
        x = np.array(x)
        y = h_(x)
        self.add_trace(go.Scatter(x=x, y=y, showlegend=False, marker={'color': '#FF6692'}))

    def plot_surface(self, xmin, xmax, ymin, ymax, function, opacity=1, showscale=True, colorscale=None):
        x_axis = np.linspace(xmin, xmax, 100)
        y_axis = np.linspace(ymin, ymax, 100)
        [x, y] = np.meshgrid(x_axis, y_axis)
        z = function([x, y])
        if colorscale is None:
            self.add_surface(x=x, y=y, z=z, opacity=opacity, showscale=showscale)
        else:
            self.add_surface(x=x, y=y, z=z, opacity=opacity, showscale=showscale, colorscale=colorscale)
        self.update_layout(template='plotly_white', width=500, height=500)
        
    def contour_zoom(self, xmin, xmax, ymin, ymax, function):
        self.data[0]['x'] =  x_axis = np.linspace(xmin, xmax, 100)
        self.data[0]['y'] =  y_axis = np.linspace(ymin, ymax, 100)
        [x, y] = np.meshgrid(x_axis, y_axis)
        self.data[0]['z'] = function([x, y])
        self.update_layout(xaxis_range=[xmin, xmax])
        self.update_layout(yaxis_range=[ymin, ymax])
