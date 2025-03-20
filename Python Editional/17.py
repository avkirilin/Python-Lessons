# Проверить, соблюдается ли в заданном тексте баланс открывающих и закрывающих круглых скобок,
# то есть можно ли установить взаимно однозначное соответствие открывающих и закрывающих
# скобок, причем открывающая скобка всегда предшествует соответствующей закрывающей.
import random
sample_string = 'a()'
my_string = ''.join((random.choice(sample_string)) for x in range(6))
print(my_string)
my_list = list(my_string)
my_count_open_scobe = 0
my_count_close_scobe = 0
flag = False
for i in range(len(my_list)):
    if my_list[i] == '(':
        my_count_open_scobe += 1
    elif my_list[i] == ')':
        my_count_close_scobe += 1
if my_count_open_scobe == my_count_close_scobe:
    scobe_list = []
    for i in my_list:
        if i in '()':
            scobe_list.append(i)
    print(scobe_list)
    i = 0
    while scobe_list != []:
        if 0 <= i < len(scobe_list) - 1:
            if scobe_list[i] == '(' and scobe_list[i+1] == ')':
                scobe_list.pop(i + 1)
                scobe_list.pop(i)
                print(scobe_list)
                i = 0
            elif scobe_list[0] == ')' or scobe_list[-1] == '(':
                break
            else:
                i += 1
        if i == len(scobe_list):
            i = 0
    if scobe_list == []:
        print()
        print('В тексте ЕСТЬ соответствие открывающихся и закрывающихся скобок')
        print(
            f"Количество '(' = {my_count_open_scobe}, Количество ')' = {my_count_close_scobe}")
    else:
        print()
        print('В тексте НЕТ соответствия открывающихся и закрывающихся скобок')
        print(
            f"Количество '(' = {my_count_open_scobe}, Количество ')' = {my_count_close_scobe}")
else:
    print()
    scobe_list = []
    for i in my_list:
        if i in '()':
            scobe_list.append(i)
    print(scobe_list)
    print()
    print('Количество открывающихся скобок не соответствует количеству закрывающихся')
    print(
        f"Количество '(' = {my_count_open_scobe}, Количество ')' = {my_count_close_scobe}")
