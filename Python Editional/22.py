# Найти количество чисел в списке, которые делятся на 3, но не делятся на 7.
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

count = 0
for i in range(len(list)):
  if list[i] % 3 == 0 and list[i] % 7 != 0:
    count += 1
print(f'Кол-во чисел в списке, которые делятся на 3, но не делятся на 7 равно: {count}')