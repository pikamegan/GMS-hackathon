import yfinance as yf
import matplotlib.pyplot as plt
import seaborn
import csv

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)


data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
data_df.to_csv('aapl.csv')

# get historical market data
hist = msft.history(period="5d")

# Plot everything by leveraging the very powerful matplotlib package
hist['Close'].plot(figsize=(16, 9))

