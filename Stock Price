import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

df = pd.read_csv('netflix.csv')
df = df.drop(columns=['Adj Close'])

fig, axis1 = plt.subplots(figsize=(20,8))
axis1.plot(df['Date'], df['Close'], color='Red')
axis1.xaxis.set_major_locator(plt.MaxNLocator(15))
axis1.set_xlabel('Date', fontsize='11')
axis1.set_ylabel('Price in USD', fontsize='11')
plt.title('Netflix Stock Prices')
plt.grid()
plt.show()
