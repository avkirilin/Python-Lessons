# Создать список, который одинаково читается как слева направо, так и справа налево.
import random
range_list = random.randint(5, 10)
list = []
for i in range(range_list):
  list.append(random.randint(1, 9))
new_list = []
for i in range(range_list * 2):
  if i < range_list:
    new_list.append(list[i])
  else:
    new_list.append(list[range_list - 1 - i])
random_num = random.randint(0, 1)
if random_num == 1:
  new_list.insert(range_list, random.randint(1, 9))
print(new_list)