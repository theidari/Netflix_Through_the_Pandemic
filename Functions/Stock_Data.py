def StockData(stocksymbol):
    import pandas as pd
    import yfinance as yf
    from datetime import datetime
    today = datetime.today().strftime('%Y-%m-%d')
    # margins for the data
    start_date = datetime.strptime("2019-01-01", '%Y-%m-%d')
    end_date = datetime.strptime(str(today), '%Y-%m-%d')
    # fetch stocks data from yfinance
    stocks_data = yf.download(stocksymbol, start = start_date, end=end_date)
    stocks_data = pd.DataFrame(stocks_data)
    return  stocks_data.reset_index()