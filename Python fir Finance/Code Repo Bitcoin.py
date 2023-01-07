import yfinance as yf 
import numpy as np
import matplotlib.pyplot as plt

data = yf.Ticker("BTC-USD") 
x = data.history('1Y')['Close'].pct_change()

plt.plot((x+1).cumprod())
plt.savefig('plot.png')

annual_std = np.std(x) * np.sqrt(252)
sharpe = (np.mean(x) / np.std(x))*np.sqrt(252)
print(sharpe)