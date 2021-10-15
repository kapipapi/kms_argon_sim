import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


def plot_positions(r: np.array):
    marker_data = go.Scatter3d(
        x=r[:, 0],
        y=r[:, 1],
        z=r[:, 2],
        marker=go.scatter3d.Marker(size=5),
        opacity=1,
        mode='markers'
    )
    fig = go.Figure(data=marker_data)
    fig.show()


def plot_momentum(p: np.array):
    _, axs = plt.subplots(1, 3)
    for (ii, title), ax in zip(enumerate('x y z'.split()), axs):
        ax.hist(p[:, ii], bins=30)
        ax.set_title(f'p_{title}')
    plt.show()
