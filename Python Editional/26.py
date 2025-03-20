# Напишите программу, которая вводит с клавиатуры непустой список целых чисел,
# и выводит число локальных максимумов (элемент является локальным максимумом,
# если он не имеет соседей, больших, чем он сам).
import random
list = [random.randint(10, 99) for i in range (random.randint(5, 10))]
print(list)
print(f'Список состоит из {len(list)} значений')
count = 0
for i in range(len(list)):
  if i == 0:
    if list[i] > list[i+1]:
      count += 1
  if i > 0 and i < len(list) - 1:
    if list[i-1] < list[i] > list[i+1]:
      count += 1
  if i == len(list) - 1:
    if list[i] > list[i-1]:
      count += 1
print(f'Кол-во локальных максимумов в списке = {count}')