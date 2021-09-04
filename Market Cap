import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

df = pd.read_csv('netflix.csv')
df = df.drop(columns=['Adj Close'])

df['Market Cap'] = df['Open']*df['Volume']

fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(df['Date'], df['Market Cap'], color='orange')
axis1.xaxis.set_major_locator(plt.MaxNLocator(15))
axis1.set_xlabel('Date', fontsize='11')
axis1.set_ylabel('Market Cap', fontsize='11')
plt.title('Market Cap')
plt.grid()
plt.show()

df.iloc[df['Market Cap'].argmax()]

ohlc = df[(df['Date'] > '2018-04-13')]
ohlc = ohlc.loc[:, ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'], format='%Y-%m-%d')

fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(ohlc['Date'], ohlc['Market Cap'], color='orange')
axis1.xaxis.set_major_locator(plt.MaxNLocator(5))
axis1.set_xlabel('Date', fontsize='11')
axis1.set_ylabel('Market Cap', fontsize='11')
plt.grid()
plt.title('Market Cap (After 13 April, 2018)', fontsize='20')
plt.show()
