import pandas as pd

df = pd.read_csv('countries of the world.csv')

# agricultural = df[df[]]
def clear_type(country_type):
    if pd.isnull(country_type):
        return 0
    country_type = country_type.replace(',', '.')
    return float(country_type)

df['Agriculture'] = df['Agriculture'].apply(clear_type)
df['Industry'] = df['Industry'].apply(clear_type)
df['Service'] = df['Service'].apply(clear_type)

def check_type(row):
    if row['Agriculture'] > row['Industry']:
        if row['Agriculture'] > row['Service']:
            return 'Agriculture'
        else:
            return 'Service'
    else:
        if row['Industry'] > row['Service']:
            return 'Industry'
        else:
            return 'Service'

df['Type'] = df.apply(check_type, axis=1)
print(df.groupby(by = 'Type')['GDP ($ per capita)'].mean())