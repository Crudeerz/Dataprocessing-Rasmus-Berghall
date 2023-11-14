from dash import Dash, html, dcc, callback, Output, Input
import plotly_express as px
import pandas as pd

df = px.data.gapminder()

counter = 0


app = Dash(__name__)


my_H1 = html.H1(style={"fontFamily":"helvetica"},children="My dash application")
my_H2 = html.H2(id="my-h2", children="More info...")
my_dropdown = dcc.Dropdown(id="my-dropdown", options=df["year"].unique(), value=2007, style={"width":"200px"})
my_graph = dcc.Graph(id="my-graph", figure=px.strip(df.query("year == 2007"), x="lifeExp", color="continent"))
my_button = html.Button("Click here!")

app.layout = html.Div(style={"backgroundColor": "white"},children=[my_H1, my_H2, my_dropdown, my_graph, my_button]) # <h1>My dash app.</h1>


@callback(
        Output(my_H2, component_property="children"),
        Output(my_graph, component_property="figure"),
        Input(my_dropdown, component_property="value")
)
def select_year(year):
    return f"{year}", px.strip(df.query("year == @year"), x="lifeExp", color="continent")


@callback(
    Output(my_H1, "children"),
    Input(my_button, "n_clicks")
)
def button_clicked(n):
    global counter
    counter += 1
    return f"Button clicked {counter} times"

app.run(debug=True, port=3000)
