# def make_salary(salary):
#     salary = salary.replace('(sadsadsa)', '')
#     salary = salary.replace('$', '')
#     salary = salary.replace('K', '')
#     if len(salary) > 4:
#         salary = salary.split('-')
#         min_salary = int(salary[0])
#         max_salary = int(salary[1])
#         return (min_salary + max_salary) / 2
#     else:
#         return 0


# df['Mid salary'] = df['Salary Estimate'].apply(make_salary)

cost = '29.75'
index = cost.find('.')
print(cost[:index])