#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DataAnalyst.csv')

#' Является ли Нью-Йорк первый по оплате труда Дата аналитиков? '
def make_stonks(salary):
    salary = salary.replace('(Glassdoor est.)','')
    salary = salary.replace('$','')
    salary = salary.replace('K','')
    if len(salary) > 4:
        salary = salary.split('-')
        min_salary = int(salary[0])
        max_salary = int(salary[1])
        return (min_salary + max_salary) / 2
    else:
        return 0

df['Mid salary'] = df['Salary Estimate'].apply(make_stonks)

result = {}
for city in df['Location'].value_counts().keys():
    mean = df[df['Location'] == city]['Mid salary'].mean()
    median = df[df['Location'] == city]['Mid salary'].median()
    mean = round(mean, 2)
    median = round(median, 2)
    result[city] = {'mean': mean, 'median': median}
    print(city, '- Средняя зарплата:', mean, '- Медианная зарплата:', median)