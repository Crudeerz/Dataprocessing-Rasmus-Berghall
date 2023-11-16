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

app = Dash(__name__ , external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(style={"display":"flex"}, children=[

    html.Div(id="left_div", style={"margin":"auto"}, children=[

        html.Div(id="div_!", children=[
            html.H1(id="H1_1", children="Dash application bootstrap", style={"text-align":"center"}),
            html.H3(id="H2_1", children="Gapminder data", style={"text-align":"center"}),
            dcc.Graph(id="my_graph", figure=px.strip(df.query("year==@y1"), x="lifeExp", template="plotly_dark", color="continent"), style={"width":"600px", }),
        ]),
        
        html.Div(id="div_2", children=[
            html.H1(id="H1_2", children="Dash application bootstrap 2", style={"text-align":"center"}),
            html.H3(id="H2_2", children="Gapminder data 2", style={"text-align":"center"}),
            dcc.Graph(id="my_graph2", figure=px.strip(df.query("year==@y2"), x="lifeExp", template="plotly_dark", color="continent", title=str(y2)), style={"width":"600px"})


        ])
    ]), 


    html.Div(id="right_div", style={"margin":"auto"}, children=[

        html.Div(id="div_3", children=[
            html.H1(id="H1_3", children="Dash application bootstrap 3", style={"text-align":"center"}),
            html.H3(id="H2_3", children="Gapminder data 3", style={"text-align":"center"}),
            dcc.Graph(id="my_graph3", figure=px.strip(df.query("year==@y3"), x="lifeExp", template="plotly_dark", color="continent"), style={"width":"600px"}) 
        ]),

        html.Div(id="div_4", children=[
            html.H1(id="H1_4", children="Dash application bootstrap 4", style={"text-align":"center"}),
            html.H3(id="H2_4", children="Gapminder data 4", style={"text-align":"center"}),
            dcc.Graph(id="my_graph4", figure=px.strip(df.query("year==@y4"), x="lifeExp", template="plotly_dark", color="continent"), style={"width":"600px"})
        ])

    ])
])


    

if __name__ == "__main__":
    app.run(debug=True)
# print(years)
