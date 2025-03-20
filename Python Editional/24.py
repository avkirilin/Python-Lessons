# Проверьте, содержит ли данный массив из n чисел, все числа от 1 до n.
import random
length_list = random.randint(5, 10)
print(f'Список составлен из {length_list - 1} значений')
list_value = random.randint(0, 1)
if list_value == 0:
    list = [random.randint(1, 10) for _ in range(1, length_list)]
else:
    list = [i for i in range(1, length_list)]
print(list)
count = 0
for i in range(1, length_list):
    for j in range(0, length_list - 1):
        if list[j] == i:
            print(i, list[j])
            count += 1
            break

if count == length_list - 1:
    print(f'Кол-во уникальных совпадений индекса со значением в списке: {count}')
    print (f'Список из {length_list - 1} значений, содержит все значения от 1 до {length_list - 1}')
else: print (f'Список не содержит все значения от 1 до {length_list - 1}')
