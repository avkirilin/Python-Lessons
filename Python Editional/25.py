# Даны два списка. Определите, существуют ли в первом списке такие два элемента,
# что их сумма равна сумме каких-либо трех элементов второго списка.
import random
list_1 = [random.randint(10, 99) for i in range(random.randint(5, 10))]
print(list_1)
print(f'Список состоит из {len(list_1)} значений')
print()
list_2 = [random.randint(10,99) for i in range(random.randint(5, 10))]
print(list_2)
print(f'Список состоит из {len(list_2)} значений')
print()
sum_list_1 = []
for i in range(len(list_1)):  
  for j in range(len(list_1)):
    if i != j:
      sum_list_1.append(list_1[i] + list_1[j])
print (sum_list_1)
print(f'Список состоит из {len(sum_list_1)} значений')
print()
sum_list_2 = []
for i in range(len(list_2)):
  for j in range(len(list_2)):
    for k in range(len(list_2)):
      if i != j and i != k and j != k:
        sum_list_2.append(list_2[i] + list_2[j] + list_2[k])
print (sum_list_2)
print(f'Список состоит из {len(sum_list_2)} значений')
print()
count = 0
for i in range(len(sum_list_1)):
  for j in range(len(sum_list_2)):
    if sum_list_1[i] == sum_list_2[j]:
      count += 1
word = str()
if 10 < count % 100 < 15:
  word = 'совпадений'
elif 1 < count % 10 < 5:
  word = 'совпадения'
elif count % 10 == 1:
  word = 'совпадение'
else:
  word = 'совпадений'
if count > 0:
  print (f'В данных списках существует {count} {word} сумм чисел')
else: 
  print('В данных списках нет совпадений сумм чисел')