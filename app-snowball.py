# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import xarray as xr
import numpy as np

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
DS = xr.open_dataset("data/ape_5000_55_0S_atm_2d_ml.ym.zm.nc",decode_times=False)
data_sit=DS.sit.squeeze()
data_hs=DS.hs_icecl.squeeze() + data_sit

sit = data_sit.values.flatten()
hs = data_hs.values.flatten()
time=np.repeat(np.arange(0,len(data_sit.time),1),len(data_sit.lat))
lat=np.tile(data_sit.lat.values,len(data_sit.time))


df = pd.DataFrame({
    "sit": sit,
    "hs": hs,
    "time": time,
    "lat": lat
})


fig = px.line(df, x="lat", y=["sit", "hs"], title='Sea-ice thickness', animation_frame="time", range_y=(0,80))

app.layout = html.Div(children=[
    html.H1(children='Snowball Test'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
