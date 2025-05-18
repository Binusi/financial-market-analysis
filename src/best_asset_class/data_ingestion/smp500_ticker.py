import yfinance as yf

# Get historical price data eg. for Apple this would be 'ticker = yf.Ticker("AAPL")'
ticker = yf.Ticker("AAPL")
df = ticker.history(period="5y")  # period of data being read