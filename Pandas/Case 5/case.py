import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Space_Corrected.csv')

df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])

# def fix_cost(cost):
#     if not pd.isnull(cost):
#         cost = cost.replace(',', '')
#         index = cost.find('.')
#         if index != -1:
#             cost = cost[:index]
#         return int(cost)

# df['Rocket'] = df['Rocket'].apply(fix_cost)
# df['Rocket'].fillna(-1, inplace=True)
# df = df.dropna()

# df['Rocket'] = df['Rocket'].apply(int)
# print(df.head())

def fix_mission_cost(cost):
    if not pd.isnull(cost):
        cost = cost.replace(',', '')
        return float(cost)

df['Rocket'] = df['Rocket'].apply(fix_mission_cost)
median_cost = df['Rocket'].median()

df['Rocket'].fillna(median_cost, inplace=True)

def is_morning(datum):
    string = datum.split(' ')
    if len(string) > 4:
        time = string[4]
        time = time.split(':')
        if len(time) == 2:
            hours = int(time[0])
            if hours >= 6 and hours < 12:
                return 1
            else:
                return 0
    return 0

df['Morning Start'] = df['Datum'].apply(is_morning)

print(len(df['Company Name'].value_counts()))