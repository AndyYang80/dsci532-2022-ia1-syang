from vega_datasets import data
from dash import Dash, dcc, html, Input, Output
import altair as alt

def plot_alt(xmax):
    driving = data("driving")
    chart = alt.Chart(driving[driving["miles"] < xmax]).mark_point().encode(
        alt.X("miles", title = "miles driven per capita"),
        alt.Y("gas", title = "gas price per gallon (USD)"))
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
        html.Div("Interactive Driving Data", style={'fontSize': 44}),
        html.Iframe(
            id='scatter',
            srcDoc=plot_alt(xmax = 0),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=3000, max=11000)])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xmax):
    return plot_alt(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)