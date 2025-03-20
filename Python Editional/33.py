# Напишите программу, которая будет запрашивать у пользователя строку из различных значений
# (числа, символы, слова), разделенных запятыми. На основе введенных данных создавать из него
# словарь, в который будут включены только числа. Ключами словаря будут являться числа, а
# значениями - их квадраты.
import random
import string
length_string = random.randint (30, 100)
my_string = str()
for i in range(length_string):
  data_type = random.randint(1, 3)
  data_length = random.randint(1, 10)
  if data_type == 1:
   my_string += ''.join(random.sample(string.ascii_letters, data_length))
  elif data_type == 2:
    my_string += ''.join(random.sample(string.digits, data_length))
  elif data_type == 3:
    my_string += ''.join(random.sample((string.digits + string.ascii_letters), data_length))
  split_string = random.randint(1, 4)
  if split_string == 1:
    my_string += ', '
  elif split_string == 2:
    my_string += ' ,'
  elif split_string == 3:
    my_string += ','
  elif split_string == 4:
    my_string += ' , '
print('Заданная строка с произвольными данными:')
print(my_string)
print()
my_string = my_string.replace(' ', '')
print('Удалили из строки все лишние пробелы:')
print(my_string)
print()
my_list = my_string.split(',')
if my_list[-1] == '':
  my_list.pop(-1)
print('Данные строки перевели в список:')
print(my_list)
print()
new_list = []
for i in range (len(my_list)):
  count = 0
  for j in my_list[i]:
      if j.isdigit():
        # print(j)
        count += 1
        # print(f'    {count} ')
  if count == len(my_list[i]):
    # print(my_list[i])
    new_list.append(int(my_list[i]))
print('Из списка выбрали только те данные, исключительно из цифр, изменили тип данных: ')
print(new_list)
my_dict = {}
for i in new_list:
  my_dict[i] = i * i
print()
print('Сделали словарь, где ключи - числа из списка, значения - это квадраты этих чисел: ')
print(my_dict)