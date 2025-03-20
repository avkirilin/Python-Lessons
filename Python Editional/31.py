# Удалить в заданном списке элементы так, чтобы оставшиеся образовывали возрастающую последовательность наибольшей длины.
import random
length_list = random.randint(10, 100)


def name(x):
    word = str()
    if 10 < x < 15:
        word = 'элементов'
    elif 1 < x < 5:
        word = 'элемента'
    elif x % 10 == 1:
        word = 'элемент'
    elif 1 < x % 10 < 5:
        word = 'элемента'
    else:
        word = 'элементов'
    return word


print(f'В списке {length_list} {name(length_list)}:')
my_list = [random.randint(10, 99) for i in range(length_list)]
print(my_list)
max_count = 0
count = 0
new_list = []
for i in range(length_list):
    if my_list[i] > my_list[i-1]:
        count += 1
        # print(count, end=', ')
    else:
        count = 0
        # print(count)
    if max_count < count:
        max_count = count
        new_list.clear()
        for j in range(max_count, -1, -1):
            new_list.append(my_list[i-j])
print()
print(f'В списке {len(new_list)} {name(len(new_list))}:')
print(new_list)
