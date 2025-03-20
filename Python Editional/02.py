# Дана строка. Показать номера символов, совпадающих с последним символом строки.
import random, string
string_lenght = int(input("Введите длину строки: "))
my_string = str()
for i in range(string_lenght):
    my_string += str(random.choice(string.ascii_letters))
print(my_string)
my_list = []
print(f"Последний символ строки: {my_string[string_lenght - 1]}")
for i in range(string_lenght - 1):
    if my_string[i] == my_string[string_lenght - 1]:
        my_list.append(i + 1)
print(f"Порядковые номера символов совпадающие с \"{my_string[string_lenght - 1]}\": ")
print(*my_list)
