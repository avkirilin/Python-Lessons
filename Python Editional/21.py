# Заполните список случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.
import random
length_string = random.randint(10, 100)
list = []
def specific_string(length): 
    sample_string = '011' 
    result = ''.join((random.choice(sample_string)) for x in range(length)) 
    return result

for i in range (length_string):
    list.append(int(specific_string(1)))
print(list)
count_0 = 0
count_1 = 0
for i in range (length_string):
  if list[i] == 0:
    count_0 += 1
  else: count_1 +=1
word = str()
if 9 < length_string < 15:
  word = 'элементов'
elif length_string % 10 == 1:
  word = 'элемент'
elif 1 < length_string % 10 < 5:
  word = 'элемента'
else: word = 'элементов'
print (f' Длина списка {length_string} {word}. Кол-во 0 = {count_0}; Кол-во 1 = {count_1};')