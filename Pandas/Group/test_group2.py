import pandas as pd

df = pd.read_csv('GoogleApps.csv')

temp = df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max'])
print('Рейтинг приложений:')
print(round(temp, 1))

temp = df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max'])
print(temp)

temp = df.pivot_table(index='Content Rating', columns='Category', values='Reviews', aggfunc='max')
print(temp[['EDUCATION', 'GAME', 'FAMILY']])