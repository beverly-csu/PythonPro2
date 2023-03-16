import sqlite3

conn = sqlite3.connect('Artistc.sqlite')
cursor = conn.cursor()
# Вопрос 1. Информация о скольких художниках представлена в базе данных? 
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Всего художников:', len(data))
# Вопрос 2. Сколько женщин (Female) в базе?
cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
data = cursor.fetchall()
print('Всего женщин-художников:', len(data))
# Вопрос 3. Сколько человек в базе данных родились до 1900 года?
cursor.execute('SELECT * FROM artists WHERE "Birth year" < 1900')
data = cursor.fetchall()
print('Всего художников, которые родились ранее 1900г:', len(data))
# Вопрос 4*. Как зовут самого пожилого художника?
# Решение супер короткое #1
cursor.execute('SELECT name FROM artists ORDER BY "Birth Year"')
data = cursor.fetchall()
print('Самый пожилой художник #1:', data[0][0])
# Решение супер не короткое #2
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
year = 2000
name = ''
for artist in data:
    if artist[4] < year:
        year = artist[4]
        name = artist[1]
print('Самый пожилой художник #2:', name)