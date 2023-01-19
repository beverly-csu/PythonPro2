# Задача №1. Подсчитай количество единиц в файле
count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            if int(symbol) == 1:
                count += 1
print(count)
# Задача №2. Найди и выведи на экран 8 элемент 14 строки
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    line = lines[13].split(' ')
    item = int(line[7])
    print('8 элемент 14 строки =', item)
# Задача №3. Найди сумму всех элементов в файле.
summ = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            summ += int(symbol)
print('Сумма всех элементов =', summ)