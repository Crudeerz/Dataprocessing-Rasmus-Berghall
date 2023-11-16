import plotly.express as px
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import random

# print("Hello")
df = px.data.gapminder()
years = list(df["year"].unique())
y1 = random.choice(years)
y2 = random.choice(years)
y3 = random.choice(years)
y4 = random.choice(years)
# html.Div(id="div_!", children=[
#     html.H1(id="H1_1", children="Dash application bootstrap", style={"text-align":"center"}),
#     html.H3(id="H2_1", children="Gapminder data", style={"text-align":"center"}),
#     dcc.Graph(id="my_graph", figure=px.strip(df.query("year==@y1"), x="lifeExp", template="plotly_dark", color="continent"), style={"width":"600px", }),

app = Dash(__name__ , external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])


app.layout = dbc.Container(children=[
    
])

    

if __name__ == "__main__":
    app.run(debug=True)
# print(years)
