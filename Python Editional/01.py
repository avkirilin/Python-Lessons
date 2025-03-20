# Сформировать строку из 10 символов. На четных позициях должны находится четные цифры, на нечетных позициях - буквы.
import random, string
my_string = str()
for i in range(9):
    if i % 2 != 0:
        i = str(random.randrange(2, 10, 2))
        my_string += i
    else:
        i = random.choice(string.ascii_letters)     #генерирует случайную букву из англ. алфавита (не забыть сделать import random, string)
        my_string += i
print(my_string)
