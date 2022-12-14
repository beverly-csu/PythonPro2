import pandas as pd

# Загружаем датафрейм 
df = pd.read_csv('GoogleApps.csv')


# Как называется приложение, расположенное первым в наборе данных?
print(df.head(1))

# К какой категории (Category) относится приложение, расположенное последним в наборе данных?
print(df.tail(1))

# Сколько столбцов содержится в наборе данных?
# Данные какого типа хранятся в каждом из столбцов?
df.info()

# Укажите среднее арифметическое и медиану размера приложений (Size)
# Сколько стоит самое дорогое приложение?
# *Укажите среднее арифметическое и медиану количества установок приложений (Installs)
print(df.describe())