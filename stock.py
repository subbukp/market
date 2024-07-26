import yfinance as yf
import pandas as pd

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.info['regularMarketPrice']

def get_stock_performance(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    if hist.empty:
        return None
    start_price = hist['Close'][0]
    end_price = hist['Close'][-1]
    performance = ((end_price - start_price) / start_price) * 100
    return performance

def main():
    ticker = input("Enter the stock ticker symbol (e.g., RELIANCE.NS): ")
    try:
        current_price = get_stock_price(ticker)
        one_year_return = get_stock_performance(ticker)

        print(f"Current price of {ticker}: {current_price}")
        if one_year_return is not None:
            print(f"1-year return of {ticker}: {one_year_return:.2f}%")
        else:
            print(f"No historical data available for {ticker}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
