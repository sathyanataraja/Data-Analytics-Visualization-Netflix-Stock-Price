import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

df = pd.read_csv('netflix.csv')
df = df.drop(columns=['Adj Close'])

#A cumulative return on an investment is the aggregate amount that the investment has gained or lost over time, independent of the amount of time involved.
df['Cumulative Return'] = (1 + df['vol']).cumprod()

fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(df['Date'], df['Cumulative Return'], color='green')
axis1.xaxis.set_major_locator(plt.MaxNLocator(15))
axis1.set_xlabel('Date', fontsize='11')
axis1.set_ylabel('Cumulative Return', fontsize='11')
plt.title('Cumulative Return')
plt.grid()
plt.show()

ohlc = df[(df['Date'] > '2018-04-13')]
ohlc = ohlc.loc[:, ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap', 'Cumulative Return']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'], format='%Y-%m-%d')
fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(ohlc['Date'], ohlc['Cumulative Return'], color='green')
axis1.xaxis.set_major_locator(plt.MaxNLocator(5))
axis1.set_xlabel('Date', fontsize='11')
axis1.set_ylabel('Cumulative Return', fontsize='11')
plt.grid()
plt.title('Cumulative Return (After 04 April, 2018)', fontsize='20')
plt.show()

df.iloc[df['Cumulative Return'].argmax()]
