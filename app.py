import dash
from dash import dash_table
from dash import html
from dash import dcc
from data import create_dataFrame
import numpy as np
import plotly.express as px



style_cell={'textAlign': 'center',
            'backgroundColor': '#f5f5f5',
            'fontWeight': 'bold',
            'header':False
           }


app = dash.Dash(__name__)

# df = pd.read_csv('data.csv')
df = create_dataFrame()

num_tables = int(np.ceil(df.shape[0] / 6))
dfs = np.array_split(df, num_tables)

# Create a list to store the table components
tables = []
for i, df in enumerate(dfs):
    tables.append(html.Div(
        dash_table.DataTable(
            id='table{}'.format(i),
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("rows"),
            style_table={'margin': '20px auto', 'border': 'none'},
            style_cell={
                'textAlign': 'center',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
            },
        ),
        style={'width': '25%', 'display': 'inline-block', 'margin': '20px', 'overflow': 'auto', 'height': '500px'}
    ))
    tables.append(html.Br())

app.layout = html.Div(
    tables,
    style={'overflow': 'auto', 'textAlign': 'center'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
