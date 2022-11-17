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

df['Profit'] = df['Price'] * df['Installs']

temp = df[df['Type'] == 'Paid']['Profit'].max()
print('Максимальный заработок на приложении:', temp)

def count_genres(genres):
    genres = genres.split(';') # 'Art & Design;Pretend Play' -> ['Art & Design', 'Pretend Play']
    return len(genres)

df['Number of genres'] = df['Genres'].apply(count_genres)

temp = df['Number of genres'].max()
print('Максимальное количество жанров:', temp)