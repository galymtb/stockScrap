import datetime as dt
from pandas_datareader import data as pdr

def getData(stock, start, end):
    """Function for getting/scrapping data about stock. Technically, it doesn't scrap data from the web. Pandas DR has access to Yahoo Finance
       stock = Stock Ticker Name
       start = starting time point
       end = ending time point (usually today)
    """
    stockData = pdr.get_data_yahoo(stock, start=start, end=end)
    return stockData

def exportFromDF(stockData, fileName):
    """Exporting data with pandas framework.
       stockData = pandas dataFrame; data of stock
       fileName = name of Excel file
    """
    stockData.to_excel(fileName)
    print('DataFrame is written to Excel File successfully.')

def main():
    stock = 'SPY'
    endDate = dt.datetime.now()
    startDate = endDate - dt.timedelta(days=365)
    newFileName = stock + ".xlsx"

    SPYData = getData(stock, startDate, endDate)
    exportFromDF(SPYData, newFileName)

main()
