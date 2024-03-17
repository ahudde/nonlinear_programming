# import of numpy for arrays and basic mathematical functions
import numpy as np
# import of plotly for the graphs
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class plot(go.Figure):
    result = None

    def __init__(self, *args):
        go.Figure.__init__(self, *args)

    def plot_contour(self, xmin, xmax, ymin, ymax, function):
        x_axis = np.linspace(xmin, xmax, 100)
        y_axis = np.linspace(ymin, ymax, 100)
        [x1, x2] = np.meshgrid(x_axis, y_axis)
        z = function([x1, x2])
        self.add_trace(go.Contour(x=x_axis, y=y_axis, z=z, contours_coloring='lines', showscale=False))
        self.update_layout(template='plotly_white', width=500, height=500)
        self.update_layout(scene = dict(
                    xaxis_title='x1',
                    yaxis_title='x2',
                    zaxis_title='f(x)'))
        self.for_each_trace(
            lambda t: t.update(hovertemplate="x1 %{x}<br>x2 %{y}<br>f(x) %{z}<extra></extra>"))

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
                    arrowwidth=2,
                    arrowcolor='red')

    def add_gradient_descent(self, x0, function, grad, gamma=1, iterations=10, color=None, constraint=None):
        x = np.zeros(shape=(iterations + 1, 2))
        f_x = np.zeros(iterations + 1)
        x[0, :] = np.array(x0)
        f_x[0] = np.round(function(x[0, :]), 3)
        for i in range(iterations):
            x[i + 1] = -gamma * grad(x[i, :]) + x[i, :]
            f_x[i + 1] = np.round(function(x[i + 1, :]), 3)
        self.add_scatter(
            x=x[:, 0],
            y=x[:, 1],
            mode='lines+markers',
            showlegend=False,
            line_color=color)
        self.result = x[-1]
        if constraint is None:
            self.update_layout(title="x0=" + str(np.round(x0, 3)) + ", gamma =" +
                                     str(np.round(gamma, 3)) + ",<br> iterations=" + str(iterations) +
                                     ", f(x)=" + str(np.round(f_x[-1], 3)) + ", x=" + str(np.round(self.result, 3)))
        else:
            self.update_layout(title="x0=" + str(np.round(x0, 3)) + ", gamma =" +
                                     str(np.round(gamma, 3)) + ",<br> iterations=" + str(iterations) +
                                     ", f(x)=" + str(np.round(f_x[-1], 3)) + ", h(x) = "
                                     + str(np.round(constraint(self.result), 3))
                                     + ",<br> x=" + str(np.round(self.result, 3)))
        self.for_each_trace(
            lambda t: t.update(hovertemplate="x1 %{x}<br>x2 %{y}<extra></extra>"))

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
        self.update_layout(scene = dict(
                    xaxis_title='x1',
                    yaxis_title='x2',
                    zaxis_title='y'))
        self.for_each_trace(
            lambda t: t.update(hovertemplate="x1 %{x}<br>x2 %{y}<br>f(x) %{z}<extra></extra>"))

    def contour_zoom(self, xmin, xmax, ymin, ymax, function):
        self.data[0]['x'] = x_axis = np.linspace(xmin, xmax, 100)
        self.data[0]['y'] = y_axis = np.linspace(ymin, ymax, 100)
        [x, y] = np.meshgrid(x_axis, y_axis)
        self.data[0]['z'] = function([x, y])
        self.update_layout(xaxis_range=[xmin, xmax])
        self.update_layout(yaxis_range=[ymin, ymax])

    def add_gradient_descent_surface(self, x0, function, grad, gamma=1, iterations=10, color=None, constraint=None):
        x = np.zeros(shape=(iterations + 1, 2))
        f_x = np.zeros(iterations + 1)
        x[0, :] = np.array(x0)
        f_x[0] = np.round(function(x[0, :]), 3)
        for i in range(iterations):
            x[i + 1] = -gamma * grad(x[i, :]) + x[i, :]
            f_x[i + 1] = np.round(function(x[i + 1, :]), 3)
        self.add_scatter3d(
            x=x[:, 0],
            y=x[:, 1],
            z=f_x,
            #mode='lines+markers',
            showlegend=False,
            line_color=color)
        self.result = x[-1]
        self.for_each_trace(
            lambda t: t.update(hovertemplate="x1 %{x}<br>x2 %{y}<br>f(x) %{f_x}<extra></extra>"))

def show_plot(contour_plot, surface_plot):
    fig = make_subplots(rows=1,
                        cols=2,
                        specs = [[{"type": "contour"}, {"type": "surface"}]],
                        shared_yaxes = True)

    fig.layout.update(contour_plot.layout)
    fig.update_layout(template='plotly_white', width=1000, height=500)

    for i in range(len(surface_plot.data)):
        fig.add_trace(
            surface_plot.data[i],
            row=1, col=2
        )

    for i in range(len(contour_plot.data)):
        fig.add_trace(
            contour_plot.data[i],
            row=1, col=1
        )

    fig.show()