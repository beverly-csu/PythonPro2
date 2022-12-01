import pandas as pd

df = pd.read_csv('Space_Corrected.csv')

df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])

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

def fix_failure(mission_status):
    if 'Failure' in mission_status:
        return 0
    else:
        return 1

df['Status Mission'] = df['Status Mission'].apply(fix_failure)

def get_country(location):
    location = location.split(',')
    country = location[-1]
    return country[1:]

df['Country'] = df['Location'].apply(get_country)

result = {}
for country in df['Country'].value_counts().keys():
    all_launches = len(df[df['Country'] == country])
    success_launches = len(df[(df['Country'] == country) & (df['Status Mission'] == 1)])
    success_procent = round(success_launches / all_launches * 100, 2) 
    result[country] = success_procent

result['Russia'] += result['Kazakhstan']
result['Russia'] /= 2
del result['Kazakhstan']

for country in result:
    print(country, '-', result[country], '%')