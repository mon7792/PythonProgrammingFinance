import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader.data as web


start = dt.datetime(2010,1,1)
end = dt.date.today()
end = dt.datetime.combine(end,dt.datetime.min.time())
# end = dt.datetime(2017,12,31)
df = web.DataReader('AAPL', 'yahoo', start, end)

print(df.head())


print(start)
print()
