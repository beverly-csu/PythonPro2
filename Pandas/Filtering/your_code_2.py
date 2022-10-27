import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
min_price = df[df['Type'] == 'Paid']['Price'].min()
print('Самое дешёвое платное приложение стоит', min_price, '$')

# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?
median_installs = df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median()
print('Медианное количество установок приложений из категории "ART_AND_DESIGN":', median_installs)

# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?
max_free = df[df['Type'] == 'Free']['Reviews'].max()
max_paid = df[df['Type'] == 'Paid']['Reviews'].max()
print('На', max_free - max_paid, 'отзывов')


# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?
min_size = df[df['Content Rating'] == 'Teen']['Size'].min()
print('Минимальный размер приложения для тинейджеров =', min_size, 'Мб')

# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?


# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
