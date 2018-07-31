
import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
# Pops data off when reaches max len
from collections import deque

# Random data:
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=100
        ),
    ]
)

# NOTE: An output can depend on as many Inputs as you like, but can only control one Output.
# You can also chain inputs/outputs to get e.g. the values of one dropdown depending on the choice in another dropdown.
@app.callback(
    Output('live-graph', 'figure'),
    events=[Event('graph-update', 'interval')]
)

# Wait, why did we keep getting unexpected EOF until we typed more below this....?
# OOOH because it's a decorate -- it needs a function to decorate!

def update_graph_scatter():
    # Add new random data whenever this runs:
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    # Create the graph:
    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    # Send back the figure to our live-graph
    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)
