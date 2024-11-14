import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, callback
import dash_mantine_components as dmc

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the app
app.layout = html.Div(children = [
    html.H1("Dummy Toggle Switch App", style={'margin-left': '10px'}),
    html.H5("Below is a Dash Mantine Components toggle switch", style={'margin-left': '10px', 'color': 'grey'}),
    html.Div([
        dmc.Switch(id="switch-example", style={'margin-left': '10px'}, checked=True, onLabel = 'SHOW TEXT', offLabel = 'HIDE TEXT', size = 'md'),
        dmc.Text(id="switch-text", style={'margin-left': '10px', 'color': 'red'}),
    ]),
])

@callback(
    Output("switch-text", "children"),
    Input("switch-example", "checked"))

def settings(checked):
    return f'Showing text now' if checked else ''

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
