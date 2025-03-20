# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12.
import random, string
string_lenght = random.randint(2, 18)
print(string_lenght)
my_string = str()
for i in range(string_lenght):
    my_string += str(random.choice(string.ascii_letters))
print(my_string)
my_list = list(my_string)
new_list = []
if len(my_list) > 10:
    for i in range(6):
        new_list.append(my_list[i])
    print('' .join(new_list))
else:
    for i in range(string_lenght):
        new_list.append(my_list[i])
    for j in range(12 - string_lenght):
        new_list.append('o')
    print('' .join(new_list))