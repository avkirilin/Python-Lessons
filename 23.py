# Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.
import random
length_list = random.randint(10, 100)
if 9 < length_list < 15:
  word = 'элементов'
elif length_list % 10 == 1:
  word = 'элемент'
elif 1 < length_list % 10 < 5:
  word = 'элемента'
else: word = 'элементов'
print(f'Длина списка {length_list} {word}: ')
list = [random.randint(0, 100) for _ in range(length_list)]
print(list)
max_sum = 0
first_num = 0
second_num = 0
third_num = 0
for i in range(len(list)):
  if i > 1:
    if list[i-2] + list[i-1] + list[i] > max_sum:
      max_sum = list[i-2] + list[i-1] + list[i]
      first_num, second_num, third_num = list[i-2], list[i-1], list [i]
      
print(f'Максимальная сумма трёх последовательных элементов списка равна: {max_sum}')
print(f'Данные элементы: {first_num}, {second_num}, {third_num}')