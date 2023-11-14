from dash import Dash, html

app = Dash(__name__)

app.layout = html.H1("My dash application") # <h1>My dash app.</h1>

app.run(debug=True)