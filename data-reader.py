
import seaborn as sns
import dash
# Dash uses React in the background to handle these:
from dash.dependencies import Input, Output

import dash_core_components as dcc
import dash_html_components as html

# Grabbing dataset from seaborn -- couldn't access the one from the tutorial:
df = sns.load_dataset('iris')

print(df.head())

app = dash.Dash()

app.layout = html.Div(children=[
    html.H2(children='what up'),
    html.Div(children='''
        Aspect to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])


# Called whenever input changes ("reactive programming": on change, update values of all components that depend on its value):
# If you want to pass values but not fire, you can use *State*.
# Key names are optional:
@app.callback(
# We can update any keyword-argument of any component here, e.g. options of a dropdown.
    Output(component_id='output-graph', component_property='children'), # Output is the 'children' property of component that has id='output-graph'
    [Input(component_id='input', component_property='value')] # Input is the 'value' property of component that has id='input'
)
#
# NOTE: Never mutate global vars within these callbacks! Nice way to avoid this is via Pandas filters.
def update_value(input_data):
    aspect = 'sepal_length'
    if (input_data):
        aspect = input_data # As soon as user completes typing in e.g. 'petal_length', the graph will update:

    return dcc.Graph(
            id = 'iris',
            figure = {
                'data': [
                    {'x': df.index, 'y': df[aspect], 'type': 'line', 'name': 'irises'},
                ],
                'layout': {
                    'title': 'Dashin'
                }
            }
        )


if __name__ == '__main__':
    app.run_server(debug=True)
