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

