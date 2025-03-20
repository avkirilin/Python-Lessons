# Дан email в строке. Определить, является ли он корректным (наличие символа @ и точки, наличие не менее двух символов после последней точки и т.д.).
mail = input('Введите email: ')
count_dog = 0
count_dot = 0
last_symbols = False
for i in range(len(mail)):
  if mail[i] == '@':
    count_dog += 1
  if mail[i] == '.':
    count_dot += 1
  if mail[-1].isalpha() and mail[-2].isalpha() and (mail[-3].isalpha() or mail[-3] == '.'):
    last_symbols = True
if count_dog == 1 and count_dot >= 1 and last_symbols == True:
  print(f"Введенный email {mail} является корректным")
else:
  print(f"Введенный email {mail} не является корректным")