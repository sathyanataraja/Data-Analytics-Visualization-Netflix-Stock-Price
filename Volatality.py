import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

df = pd.read_csv('netflix.csv')
df = df.drop(columns=['Adj Close'])

#In order to know the volatility of the stock, we find the daily percentage change in the closing price of the stock
df['vol'] = (df['Close']/df['Close'].shift(1)) - 1

fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(df['Date'], df['vol'], color='purple')
axis1.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.title('Volatility')
plt.grid()
plt.show()

df['vol'].hist(bins=100, color='purple');
