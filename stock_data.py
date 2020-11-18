import os
import pandas as pd
from pandas_datareader import data, wb
import datetime

IEX_KEY = os.environ['IEXAPIKEY']

start = pd.to_datetime('2020-09-01')
end = pd.to_datetime('today')

palantir_df = data.DataReader('PLTR', 'yahoo', start , end)
print(palantir_df)
