# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
count_in_class1 = int(input('Введите кол-во учеников, которые будут обучаться в классе А: '))
count_in_class2 = int(input('Введите кол-во учеников, которые будут обучаться в классе Б: '))
count_in_class3 = int(input('Введите кол-во учеников, которые будут обучаться в классе В: '))
count_desk_inn_class1 = int((count_in_class1 / 2) + count_in_class1 % 2)
count_desk_inn_class2 = int((count_in_class2 / 2) + count_in_class2 % 2)
count_desk_inn_class3 = int((count_in_class3 / 2) + count_in_class3 % 2)
print('Необходимое кол-во парт:')
print('в классе А:', count_desk_inn_class1)
print('в классе Б:', count_desk_inn_class2) 
print('в классе В:', count_desk_inn_class3)
print(f'Суммарно необходимо преобрести {(count_desk_inn_class1 + count_desk_inn_class2 + count_desk_inn_class3)} парт(ы)')