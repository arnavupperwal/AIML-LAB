import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")

"""
print(df.head(10))
print(df.describe())
df.info()
print(df.columns)
print(df.dtypes)
print(df.shape)
print(df.tail(5))
print(df['total_bill'])
print(df[['total_bill','tip']])
print(df.loc[0:4])
print(df.iloc[0:4,0:3])
print(df[df['total_bill']>20])
print(df.groupby('day')['total_bill'].mean())

#histogram
plt.hist(df['total_bill'], bins = 10, color = 'blue', alpha = 0.7)
plt.xlabel('Total bill')
plt.ylabel('count')
plt.title('histogram of total bill')
plt.show()
"""
"""
#bar graphg
plt.figure()
df.groupby('day')['total_bill'].mean().plot(kind='bar',color='green')
plt.xlabel('Day')
plt.ylabel('Total bill')
plt.title('Average Total bill per day')
plt.show()
"""
"""
#scatter plot
plt.figure()
df.plot(kind = 'scatter', x = 'total_bill', y = 'tip', color = 'green', alpha = 0.5)
plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.title('Scatter plot of total bill vs tip')
plt.show()
"""

#line graph partysize vs average tip 
plt.figure()
df.groupby('size')['tip'].mean().plot(kind = 'line', color= 'red')
plt.xlabel('party size')
plt.ylabel('average tip')
plt.title('average tip by party size')
plt.show()