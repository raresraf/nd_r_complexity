
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Create a 2x2 subplot grid
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}],
           [{'type': 'surface'}, {'type': 'surface'}]],
    subplot_titles=("k=1", "k=2", "k=3", "k=4")
)

# Define the domain for n and d
n_range = np.linspace(1, 1000, 10)
d_range = np.linspace(1, 10, 10)
n_surface, d_surface = np.meshgrid(n_range, d_range)

# k values for each subplot
k_values = [1, 2, 3, 4]

# Positions for the subplots
positions = [(1, 1), (1, 2), (2, 1), (2, 2)]

for i, k in enumerate(k_values):
    row, col = positions[i]

    # Function 1: z = 8 * n * d * k
    z1 = 8 * n_surface * d_surface * k

    # Function 2: z = 10 * n * d + 20 * n * k
    z2 = 10 * n_surface * d_surface + 20 * n_surface * k

    # Add surfaces to the subplot
    fig.add_trace(
        go.Surface(x=n_surface, y=d_surface, z=z1, colorscale='Blues', showscale=False, name=f'8ndk (k={k})'),
        row=row, col=col
    )
    fig.add_trace(
        go.Surface(x=n_surface, y=d_surface, z=z2, colorscale='Reds', showscale=False, name=f'10nd + 20nk (k={k})'),
        row=row, col=col
    )

# Update the layout for the entire figure
fig.update_layout(
    title_text='Comparison of z = 8ndk and z = 10nd + 20nk',
    height=800,
    width=1000,
    scene1=dict(xaxis_title='n', yaxis_title='d', zaxis_title='Result'),
    scene2=dict(xaxis_title='n', yaxis_title='d', zaxis_title='Result'),
    scene3=dict(xaxis_title='n', yaxis_title='d', zaxis_title='Result'),
    scene4=dict(xaxis_title='n', yaxis_title='d', zaxis_title='Result')
)

# Save the plot to an HTML file
fig.write_html("docs/grid_visualization.html")

print("Interactive 2x2 grid visualization created at docs/grid_visualization.html")
