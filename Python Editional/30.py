# Удалите в целочисленном массиве все положительные числа, которые являются палиндромами
import random
length_list = random.randint(100, 500)
my_list = [random.randint(-999999, 999999) for i in range(length_list)]
my_list[5] = 99
my_list[6] = 949
my_list[7] = 7447
my_list[8] = 13531
my_list[9] = 654456
print(my_list)
print()
print(f'Длина изначального списка: {len(my_list)}')
print()
new_list = []
for i in range(len(my_list)):
    if 10 <= my_list[i] <= 99:
        if my_list[i] % 10 == (my_list[i] // 10) % 10:
            print(f'удален {i} элемент листа: {my_list[i]}')
        else:
            new_list.append(my_list[i])
    if 100 <= my_list[i] <= 999:
        if my_list[i] % 10 == my_list[i] // 100:
            print(f'удален {i} элемент листа: {my_list[i]}')
        else:
            new_list.append(my_list[i])
    if 1000 <= my_list[i] <= 9999:
        if my_list[i] % 10 == my_list[i] // 1000 and (my_list[i] // 10) % 10 == (my_list[i] // 100) % 10:
            print(f'удален {i} элемент листа: {my_list[i]}')
        else:
            new_list.append(my_list[i])
    if 10000 <= my_list[i] <= 99999:
        if my_list[i] % 10 == my_list[i] // 10000 and (my_list[i] // 10) % 10 == (my_list[i] // 1000) % 10:
            print(f'удален {i} элемент листа: {my_list[i]}')
        else:
            new_list.append(my_list[i])
    if 100000 <= my_list[i] <= 999999:
        if my_list[i] % 10 == my_list[i] // 100000 and (my_list[i] // 10) % 10 == (my_list[i] // 10000) % 10 and (my_list[i] // 100) % 10 == (my_list[i] // 1000) % 10:
            print(f'удален {i} элемент листа: {my_list[i]}')
        else:
            new_list.append(my_list[i])
    if -999999 <= my_list[i] <= 9:
        new_list.append(my_list[i])
print()
print(new_list)
print()
print(f'Длина списка с удаленными значениями: {len(new_list)}')
print()
word = str()
if len(my_list) - len(new_list) == 1:
    word = 'элемент'
elif 1 < len(my_list) - len(new_list) < 5:
    word = 'элемента'
else:
    word = 'элементов'
print(f'Удалено {len(my_list)-len(new_list)} {word} из изначального списка')
