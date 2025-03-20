# Дан текст. Найдите наибольшее количество идущих подряд цифр.
import random
import string
letters_and_digits = string.ascii_letters + string.digits * 4
string = ''.join(random.sample(letters_and_digits, 62)) + ''.join(random.sample(letters_and_digits, 62)) + ''.join(random.sample(letters_and_digits, 62)) + ''.join(random.sample(letters_and_digits, 62))
print(string)
list = []
for i in string:
  list.append(i)
new_list = []
for i in list:
  if i.isalpha():
    new_list.append(' ')
  else:
    new_list.append(i)
new_new_list = []
for i in new_list:
  if i == ',' or i == ';' or i == '.' or i == '!' or i == '?' or i == '-':
    new_new_list.append(' ')
  else: 
    new_new_list.append(i)
another_list = []
for i in range(len(new_new_list) - 1):
  if new_new_list[i] == ' ' and new_new_list[i + 1] != ' ':
    another_list.append(new_new_list[i])
  elif new_new_list[i] != ' ':
    another_list.append(new_new_list[i])
count = 0
max_count = 0
for i in another_list:
  if i != ' ':
    count += 1
    if max_count < count:
      max_count = count
  else: 
    count = 0
print(f"Наибольшее кол-во подряд идущих цифр в тексте равно: {max_count}")
    