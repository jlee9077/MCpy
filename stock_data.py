import os
import pandas as pd
from pandas_datareader import data, wb
import datetime
import plotly.graph_objects as go

IEX_KEY = os.environ['IEXAPIKEY']

start = pd.to_datetime('2020-09-01')
end = pd.to_datetime('today')

ticker = raw_input("Please Enter Ticker Symbol: ").upper()
print('You entered ticker : ', ticker)

stock_data = data.DataReader(ticker, 'yahoo', start , end)

fig = go.Figure()

fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close']))

#customize x and y axis labels
fig.update_xaxes(
    title = 'Date',
    rangeslider_visible=True
)

fig.update_yaxes(
    title = 'Stock Price'
)

#add chart title
fig.update_layout(title = ticker)

fig.show()
