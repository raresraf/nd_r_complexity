
import plotly.graph_objects as go
import numpy as np

# Data points
coords = [
    (2500, 2500, 0.04890100), (2500, 5000, 0.09279700), (2500, 7500, 0.13996300),
    (2500, 10000, 0.20393600), (2500, 12500, 0.22157700), (2500, 15000, 0.25861200),
    (2500, 17500, 0.32057400), (2500, 20000, 0.32818100), (5000, 2500, 0.09725500),
    (5000, 5000, 0.18812000), (5000, 7500, 0.27919700), (5000, 10000, 0.40614000),
    (5000, 12500, 0.47966600), (5000, 15000, 0.57703700), (5000, 17500, 0.63734800),
    (5000, 20000, 0.75036900), (7500, 2500, 0.14226200), (7500, 5000, 0.28197700),
    (7500, 7500, 0.41949000), (7500, 10000, 0.57677600), (7500, 12500, 0.71452600),
    (7500, 15000, 0.82336700), (7500, 17500, 0.98810200), (7500, 20000, 1.11671100),
    (10000, 2500, 0.18909500), (10000, 5000, 0.37511500), (10000, 7500, 0.56139800),
    (10000, 10000, 0.78178300), (10000, 12500, 0.96800900), (10000, 15000, 1.11957800),
    (10000, 17500, 1.34153300), (10000, 20000, 1.54005700), (12500, 2500, 0.23255600),
    (12500, 5000, 0.46671700), (12500, 7500, 0.70155100), (12500, 10000, 0.97202700),
    (12500, 12500, 1.22789500), (12500, 15000, 1.45225000), (12500, 17500, 1.72889900),
    (12500, 20000, 1.93507000), (15000, 2500, 0.27716500), (15000, 5000, 0.57047300),
    (15000, 7500, 0.84754100), (15000, 10000, 1.17217500), (15000, 12500, 1.45725400),
    (15000, 15000, 1.72738700), (15000, 17500, 2.01050600), (15000, 20000, 2.26070200),
    (17500, 2500, 0.32282200), (17500, 5000, 0.66139500), (17500, 7500, 0.97547700),
    (17500, 10000, 1.33687600), (17500, 12500, 1.69452900), (17500, 15000, 1.98614600),
    (17500, 17500, 2.31899900), (17500, 20000, 2.63955600), (20000, 2500, 0.37004700),
    (20000, 5000, 0.74787000), (20000, 7500, 1.11706200), (20000, 10000, 1.50660100),
    (20000, 12500, 1.89765200), (20000, 15000, 2.25583100), (20000, 17500, 2.74388800),
    (20000, 20000, 3.03968600)
]

n_vals = [c[0] for c in coords]
w_vals = [c[1] for c in coords]
time_vals = [c[2] for c in coords]

# Create the 3D scatter plot for the measured data
scatter_plot = go.Scatter3d(
    x=n_vals,
    y=w_vals,
    z=time_vals,
    mode='markers',
    marker=dict(
        size=5,
        color='blue',
    ),
    name='Measured Data'
)

# Create the fitted surface
n_range = np.linspace(min(n_vals), max(n_vals), 10)
w_range = np.linspace(min(w_vals), max(w_vals), 10)
n_surface, w_surface = np.meshgrid(n_range, w_range)
time_surface = 7.628e-09 * n_surface * w_surface

surface_plot = go.Surface(
    x=n_surface,
    y=w_surface,
    z=time_surface,
    colorscale='Reds',
    opacity=0.7,
    name='Fitted Surface'
)

# Create the figure and add the plots
fig = go.Figure(data=[scatter_plot, surface_plot])

# Update the layout
fig.update_layout(
    title='0/1 Knapsack Algorithm Performance',
    scene=dict(
        xaxis_title='n (Number of Items)',
        yaxis_title='W (Capacity)',
        zaxis_title='Time (seconds)'
    ),
    legend_title_text='Legend',
    width=1000,
    height=800
)

# Save the plot to an HTML file
fig.write_html("docs/knapsack_visualization.html")

print("Interactive 3D visualization created at docs/knapsack_visualization.html")
