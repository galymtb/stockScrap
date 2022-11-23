import time
import pandas as pd

year = 365 * 86400
month = 30 * 86400
day = 86400

stock = 'SPY'
endDate = int(time.time())
startDate = int(endDate - year)
interval = "1d" # 1wk 1mo

query_url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={startDate}&period2={endDate}&interval={interval}&events=history&includeAdjustedClose=true"

newFileName = stock + ".xlsx"

df = pd.read_csv(query_url)
df.to_excel(newFileName)
print('DataFrame is written to Excel File successfully.')