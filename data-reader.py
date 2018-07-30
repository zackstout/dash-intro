
import seaborn as sns
import dash
# Dash uses React in the background to handle these:
from dash.dependencies import Input, Output

import dash_core_components as dcc
import dash_html_components as html

df = sns.load_dataset('iris')

print(df.head())

app = dash.Dash()

app.layout = html.Div(children=[
    html.H2(children='what up'),
    # html.Div(id='output')
    html.Div(children='''
        Aspect to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
#
#
def update_value(input_data):
    # return 'Input: "{}"'.format(input_data)
    aspect = 'sepal_length'
    if (input_data):
        aspect = input_data

    return dcc.Graph(
            id = 'iris',
            figure = {
                'data': [
                    {'x': df.index, 'y': df[aspect], 'type': 'line', 'name': 'irises'},
                    # {'x': [1, 2, 3, 4, 5], 'y': [2, 0, 3, -4, 8], 'type': 'bar', 'name': 'hiya'}
                ],
                'layout': {
                    'title': 'Dashin'
                }
            }
        )





if __name__ == '__main__':
    app.run_server(debug=True)
