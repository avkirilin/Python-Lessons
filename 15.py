# Дан текст. Заменить все цифры соответствующими словами.

import random
def specific_string(length):
    sample_string = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789'
    result = ''.join((random.choice(sample_string)) for x in range(length))
    return result
length_string = random.randint(5, 62)
word = str()
if length_string % 10 == 1:
    word = 'слова'
else:
    word = 'слов'
my_list = []
for i in range(length_string):
    random_lenght_word = random.randint(5, 62)
    my_list.append(specific_string(random_lenght_word))
print(f"Изначально заданный список из {length_string} {word}: ")
print()
print(my_list)
print()
my_dict = {'0': 'НОЛЬ', '1': 'ОДИН', '2': 'ДВА', '3': 'ТРИ', '4': 'ЧЕТЫРЕ',
           '5': 'ПЯТЬ', '6': 'ШЕСТЬ', '7': 'СЕМЬ', '8': 'ВОСЕМЬ', '9': 'ДЕВЯТЬ'}
new_list = []
for i in my_list:
    count = str()
    for j in i:
        if j.isdigit():
            count += my_dict.get(j)
        else:
            count += j
    new_list.append(count)
print('Список с замененными цифрами на слова: ')
print()
print(new_list)
