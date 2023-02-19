import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

# load sample data into a pandas dataframe
data = pd.read_csv("sample_data.csv")

# create the dash app and set the bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# create the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.FormGroup([
                dbc.Label("Enter Age"),
                dbc.Input(type="number", id="age-input", placeholder="Enter Age")
            ]),
            html.Br(),
            dbc.Button("Submit", id="submit-button", color="primary", block=True),
            html.Br()
        ], md=4),
        dbc.Col([
            html.Div(id="table-container")
        ], md=8)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id="graph-container")
        ], md=12)
    ])
])

# create the callback that will update the table and the graph based on the age input
@app.callback(
    [dash.dependencies.Output("table-container", "children"), dash.dependencies.Output("graph-container", "children")],
    [dash.dependencies.Input("submit-button", "n_clicks")],
    [dash.dependencies.State("age-input", "value")]
)
def update_table_and_graph(n_clicks, age):
    if age is not None:
        age = int(age) + 1
        filtered_data = data[data["age"] == age]
        table = dbc.Table.from_dataframe(filtered_data, striped=True, bordered=True, hover=True)
        graph = dcc.Graph(figure=px.histogram(filtered_data, x="age"))
        return [table, graph]
    else:
        return ["", ""]

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
