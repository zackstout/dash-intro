
import dash
# Dash uses React in the background to handle these:
from dash.dependencies import Input, Output

import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# app.layout = html.Div('what up')

app.layout = html.Div(children=[
    html.H2(children='what up'),
    dcc.Input(id='input', value='submit...', type='text'),
    html.Div(id='output')
    # dcc.Graph(
    #     id = 'example',
    #     figure = {
    #         'data': [
    #             {'x': [1, 2, 3, 4, 5], 'y': [1, 11, 2, 6, 4], 'type': 'line', 'name': 'yo'},
    #             {'x': [1, 2, 3, 4, 5], 'y': [2, 0, 3, -4, 8], 'type': 'bar', 'name': 'hiya'}
    #         ],
    #         'layout': {
    #             'title': 'Dashin'
    #         }
    #     }
    # )
])



@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)


def update_value(input_data):
    return 'Input: "{}"'.format(input_data)







if __name__ == '__main__':
    app.run_server(debug=True)






# dashin!
