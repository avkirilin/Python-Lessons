# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной
# последовательности bn удалили одно число, а оставшиеся перемешали. Найти
# удаленное число.
import random
lenght_list = random.randint(10, 15)
print(f'Кол-во элементов в заданном листе: {lenght_list - 1}')
list_1 = [i for i in range(lenght_list) if i > 0]
print('Первая последовательность: ')
print(list_1)
print()
list_2 = []
for i in range (lenght_list - 1):
  list_2.append(list_1[i])
# print(list_2)
list_2.pop(random.randint(0, len(list_2) - 1))
print('Копия последовательности с удаленным числом: ')
print(list_2)
print()
random.shuffle(list_2)
print('Перемешанная последовательность с удаленным числом:')
print(list_2)
print()
# print(f'Длина листа: {len(list_2)}')
count = 0
for i in range(1, len(list_2) + 2):
  for j in list_2:
    if i == j:
      count += 1
  if count == 0:
    print(f'Удаленное число из списка: {i}')
  count = 0