# Дана строка. Придумать алгоритм шифрования данной строки и дешифрования.
import random

my_string = (
    'Привет! Это тестовый текст для шифрования. Попробуем его зашифровать и обратно расшифоровать?')
my_string = my_string.lower()
print('Введенный пользователем текст: ')
print()
print(my_string)
print()
my_dict = {'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ъ', 'д': 'ы', 'е': 'ь', 'ё': 'щ', 'ж': 'ш', 'з': 'ч',
           'и': 'ц', 'й': 'х', 'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о',
           'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к', 'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё',
           'ь': 'е', 'ы': 'д', 'ъ': 'г', 'э': 'в', 'ю': 'б', 'я': 'а', ' ': '@', ',': ';', '.': '!',
           ':': '?', '?': ':', '!': '.', ';': ',', '@': ' '}
my_list = list(my_string)
crypt_list = []
for i in my_list:
    crypt_list.append(my_dict.get(i))
crypt_string = ''.join(crypt_list)
print('Зашифованный текст: ')
print()
print(crypt_string)
decrypt_list = list(crypt_string)
print()
decrypted_list = []
for i in decrypt_list:
    decrypted_list.append(my_dict.get(i))
decrypted_string = ''.join(decrypted_list)
print('Расшифованный текст: ')
print()
print(decrypted_string)
