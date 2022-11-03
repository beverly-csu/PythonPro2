import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print('Количество приложений с категорией BUSINESS =', df['Category'].value_counts()['BUSINESS'])

temp = df['Content Rating'].value_counts()
result = temp['Teen'] / temp['Everyone 10+']
print('Соотношение:', round(result, 2))

temp = df.groupby(by = 'Type')['Rating'].mean()
print('Средний рейтинг платных приложений:', round(temp['Paid'], 2))
print('Разница между средним рейтингом бесплатных и платных приложений:', round(temp['Paid'] - temp['Free'], 2))

temp = df.groupby(by = 'Category')['Size'].agg(['min', 'max'])
print('Минимальный размер:', round(temp.loc['COMICS']['min'], 2))
print('Максимальный размер:', round(temp.loc['COMICS']['max'], 2))