# Вывести в алфавитном порядке все слова, содержащие наибольшее количество гласных букв; найти все слова, в которые буква а входит не менее двух раз.

import random

def specific_string(length): 
    sample_string = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя' 
    result = ''.join((random.choice(sample_string)) for x in range(length)) 
    return result
length_string = random.randint(5, 50)
word = str()
if length_string % 10 == 1:
  word = 'слова'
else:
  word = 'слов'
my_list = []
for i in range (length_string):
  random_lenght_word = random.randint(5, 62)
  my_list.append(specific_string(random_lenght_word))
print(f"Изначально заданный список из {length_string} {word}: ")
print()
print(my_list)
print()
new_list =[]
for i in range(len(my_list)):
  count = 0
  for j in my_list[i]:
    if j in 'аеёиоуыэюя':
      count += 1
  new_list.append(count)
another_list = list(zip(new_list, my_list))
another_list = sorted(another_list, reverse = True)
pre_pre_last_list = []
for i in range(len(another_list)):
  another_list[i] = list(another_list[i])
  pre_pre_last_list.append(another_list[i])
pre_last_list = []
for i in pre_pre_last_list:
  for j in i:
    pre_last_list.append(j)
last_list = []
for i in range(len(pre_last_list)):
  if i % 2 != 0:
    last_list.append(pre_last_list[i])
print("Отсортированный список по количеству гласных букв в слове от наибольшего к наименьшему: ")
print()
print(last_list)
print()
list_with_twice_a = []
for i in last_list:
  count = 0
  for j in i:
    if j == 'а':
      count += 1
  if count >= 2:
    list_with_twice_a.append(i)
print('Список слов с двумя и более буквами "а": ')
print()
print(list_with_twice_a)