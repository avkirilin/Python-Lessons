# Дана строка. Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ, не совпадающий 
# ни с одним из символов этого фрагмента. Показать фрагменты, упорядоченные по алфавиту.
import random, string
string_lenght = random.randrange(9, 99, 3)
print(f"Длина строки: {string_lenght}")
my_string = str()
for i in range(string_lenght):
    my_string += str(random.choice(string.ascii_letters))
print(f"Произвольная строка: \n{my_string}")
three_symbol_split_list = [my_string[i:i+3] for i in range(0, len(my_string), 3)]
print(f"Строка разбитая по 3 символа: \n{three_symbol_split_list}")
my_split_list = [my_string[i:i+1] for i in range(0, len(my_string), 1)]
new_list = []
for i in range(len(my_split_list)):
    new_num = 0
    if (i + 2) % 3 == 0:
        new_num = str(random.choice(string.ascii_letters))
        while new_num == my_split_list[i - 1] or new_num == my_split_list[i + 1]:
            new_num = str(random.choice(string.ascii_letters))
        new_list.append(new_num)
    else:
        new_list.append(my_split_list[i])
new_string = ''.join(new_list)
another_split_list = [new_string[i:i+3] for i in range(0, len(new_string), 3)]
print(f"Строка разделенная на фрагменты с замененными средними символами: \n{another_split_list}")
last_list = list.sort(another_split_list)
print(f"Упорядоченые по алфавиту фрагменты строки: \n{another_split_list}")