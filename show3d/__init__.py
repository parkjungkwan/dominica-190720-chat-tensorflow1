import plotly
import plotly.graph_objs as go
import numpy as np

df = 'data/mt_bruno_elevation.csv'
Z = np.loadtxt(df, delimiter=',', skiprows=1, usecols=range(1, 25))
data = [go.Surface(z=Z)]
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename='../templates/mt-3d-surface.html')