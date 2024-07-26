import yfinance as yf
import pandas as pd

def get_nifty_500_list():
    # Here, we're using a CSV file as an example. Replace this with your actual source.
    url = 'https://archives.nseindia.com/content/indices/ind_nifty500list.csv'
    nifty_500_df = pd.read_csv(url)
    return nifty_500_df['Symbol'].tolist()

def get_stock_performance(stock):
    ticker = yf.Ticker(stock + ".NS")
    hist = ticker.history(period="1y")
    if hist.empty:
        return None
    start_price = hist['Close'][0]
    end_price = hist['Close'][-1]
    performance = ((end_price - start_price) / start_price) * 100
    return performance

def get_top_stocks_with_performance():
    # Get the list of Nifty 500 stocks
    ticker_list = get_nifty_500_list()
    
    # Initialize a DataFrame to hold the stock data
    stock_data = []

    for ticker in ticker_list:
        stock_info = yf.Ticker(ticker + ".NS").info

        market_cap = stock_info.get('marketCap', 0)
        if market_cap >= 1000 * 10**7:  # 1000 crore in INR is 1000 * 10**7 in USD
            performance = get_stock_performance(ticker)
            if performance is not None:
                stock_info['1yr_performance'] = performance
                stock_data.append(stock_info)
    
    # Convert to DataFrame
    df = pd.DataFrame(stock_data)
    
    # Sort by market cap
    df = df.sort_values(by='marketCap', ascending=False)
    
    # Get top 200 stocks
    top_200_stocks = df.head(200)
    
    return top_200_stocks

top_stocks = get_top_stocks_with_performance()
print(top_stocks)