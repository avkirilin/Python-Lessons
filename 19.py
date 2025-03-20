# Создать список, на четных местах в котором стоят единицы, а на нечетных местах - числа, равные остатку от деления своего номера на 5

import random
range_list = random.randint(10, 50)
# print(range_list)
list = []
for i in range(range_list):
    if i % 2 == 0:
        list.append(i % 5)
        # print(f'остаток от деления {i} на 5 = {i % 5}')
    else:
        list.append(1)
print(list)
