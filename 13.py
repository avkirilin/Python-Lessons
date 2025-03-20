# Дано натуральное число. Получить строку, в которой тройки цифр этого числа разделены пробелом, начиная с правого конца. Например, число 1234567 преобразуется в 1 234 567.

import random
our_random_str = str(random.randint(4, 99999999999999999999))
print(our_random_str)
our_list = []
for i in range(len(our_random_str)):
  our_list.append(our_random_str[i])
new_list = []
for i in range(len(our_list)):
  if (len(our_list) - i) % 3 == 0:
    new_list.append(' ')
    new_list.append(our_list[i])
  else:
    new_list.append(our_list[i])
new_random_str = ''.join(new_list)
print(new_random_str)
