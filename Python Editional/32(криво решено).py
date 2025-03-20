# Даны n целых чисел. Расставить между ними знаки + и - так, чтобы значение получившегося выражения было равно заданному целому s.
import random
our_number = random.randint(20, 50)
print(f'Число, которое необходимо получить из заданного списка = {our_number}')
length_list = random.randint(30, 100)
my_list = [random.randint(1, 5) for i in range(length_list)]
print(f' Длина заданного списка: {length_list}')
print(my_list)
my_list.sort()
my_list.reverse()
print()
print(my_list)
count = 0
print('0', end=' ')
for i in range(len(my_list)):
    if count < our_number:
        count += my_list[i]
        if i != len(my_list) - 1:
            print(f'+ {my_list[i]}', end=' ')
        else:
            print(f'+ {my_list[i]}', end='')
    else:
        count -= my_list[i]
        if i != len(my_list) - 1:
            print(f'- {my_list[i]}', end=' ')
        else:
            print(f'- {my_list[i]}', end='')
if count == our_number:
    print(f' = {our_number}')
    print()
    print('Задача успешно реализована')
else:
    print()
    print('ОШИБКА')
