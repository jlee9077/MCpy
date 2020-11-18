import os
import pandas as pd
from pandas_datareader import data, wb
import datetime
import plotly.graph_objects as go

IEX_KEY = os.environ['IEXAPIKEY']

start = pd.to_datetime('2020-09-01')
end = pd.to_datetime('today')

palantir_df = data.DataReader('PLTR', 'yahoo', start , end)
# print(palantir_df)

fig = go.Figure()

fig.add_trace(go.Scatter(x=palantir_df.index, y=palantir_df['Close']))

#customize x and y axis labels
fig.update_xaxes(
    title = 'Date',
    rangeslider_visible=True
)

fig.update_yaxes(
    title = 'Stock Price'
)

#add chart title
fig.update_layout(title = 'PALANTIR')

fig.show()
