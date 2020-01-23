import pandas as pd

df = pd.read_csv('addresses.csv')


print(df)

df.to_csv('adress_2.csv')