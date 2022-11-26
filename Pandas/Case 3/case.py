import pandas as pd

df = pd.read_csv('menu.csv')

# df.info()
breakfasts = df[df['Category'] == 'Breakfast']

print(breakfasts['Calories'].median())
print(breakfasts['Calories'].median())