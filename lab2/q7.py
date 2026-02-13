import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("~/Desktop/'aiml lab'/lab2/tips.csv")

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
print(df.ilocc[0:4,0:3])
print(df[df['total_bill']>20])
print(df.groupby('day')['total_bill'].mean())
plt.hist(df['total_bill'], bins = 10, colour = 'blue', alpha = 0.7)
plt.xlabel('Total bill')
plt.ylabel('count')
plt.title('histogram of total bill')
plt.show()
