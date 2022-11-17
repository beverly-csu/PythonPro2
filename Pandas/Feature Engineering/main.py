import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

df['Rating'].fillna(-1, inplace=True)

def make_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    else:
        return -1

df['Size'] = df['Size'].apply(make_size)

def make_installs(installs):
    if installs[-1] == '+':
        installs = installs[:-1]
    installs = installs.replace(',', '') # 10,000,000+ -> 10000000
    return int(installs)

df['Installs'] = df['Installs'].apply(make_installs)

def make_price(price):
    if price[0] == '$':
        price = price[1:]
    return float(price)

df['Price'] = df['Price'].apply(make_price)

