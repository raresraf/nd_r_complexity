
import plotly.graph_objects as go
import numpy as np

# Data points for BFS
coords = [
    (1000000, 1000000, 0.23427400), (1000000, 2000000, 0.40370200), (1000000, 3000000, 0.55278100),
    (1000000, 4000000, 0.74719900), (1000000, 5000000, 0.96643100), (2000000, 2000000, 0.00639500),
    (2000000, 4000000, 0.80506300), (2000000, 6000000, 1.21548900), (2000000, 8000000, 1.60598000),
    (2000000, 10000000, 2.08949700), (3000000, 3000000, 0.73830300), (3000000, 6000000, 1.33893400),
    (3000000, 9000000, 1.82142800), (3000000, 12000000, 2.48483900), (3000000, 15000000, 3.31258000),
    (4000000, 4000000, 1.02087000), (4000000, 8000000, 1.71033900), (4000000, 12000000, 2.52250600),
    (4000000, 16000000, 3.41296500), (4000000, 20000000, 4.43548200), (5000000, 5000000, 0.00974300),
    (5000000, 10000000, 2.19720700), (5000000, 15000000, 3.34508000), (5000000, 20000000, 4.33967000),
    (5000000, 25000000, 5.63834700)
]

v_vals = [c[0] for c in coords]
e_vals = [c[1] for c in coords]
time_vals = [c[2] for c in coords]

# Create the 3D scatter plot for the measured data
scatter_plot = go.Scatter3d(
    x=v_vals,
    y=e_vals,
    z=time_vals,
    mode='markers',
    marker=dict(
        size=5,
        color='green',
    ),
    name='Measured BFS Data'
)

# Create the fitted surface
v_range = np.linspace(min(v_vals), max(v_vals), 10)
e_range = np.linspace(min(e_vals), max(e_vals), 10)
v_surface, e_surface = np.meshgrid(v_range, e_range)
time_surface = 1.668154878787879e-07 * (v_surface + e_surface)

surface_plot = go.Surface(
    x=v_surface,
    y=e_surface,
    z=time_surface,
    colorscale='Oranges',
    opacity=0.7,
    name='Fitted Surface'
)

# Create the figure and add the plots
fig = go.Figure(data=[scatter_plot, surface_plot])

# Update the layout
fig.update_layout(
    title='Breadth-First Search (BFS) Algorithm Performance',
    scene=dict(
        xaxis_title='V (Number of Vertices)',
        yaxis_title='E (Number of Edges)',
        zaxis_title='Time (seconds)'
    ),
    legend_title_text='Legend',
    width=1000,
    height=800
)

# Save the plot to an HTML file
fig.write_html("docs/bfs_visualization.html")

print("Interactive 3D visualization for BFS created at docs/bfs_visualization.html")
