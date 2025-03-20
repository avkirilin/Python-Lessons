# Даны две строки. Определите, можно ли из некоторых символов первой строки составить вторую строку.

import random, string
def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
random_length_1 = random.randint(30, 62)
random_string_1 = generate_alphanum_random_string(random_length_1)
print(f'{random_length_1}\t{random_string_1}')
random_length_2 = random.randint(5, 10)
random_string_2 = generate_alphanum_random_string(random_length_2)
print(f'{random_length_2}\t{random_string_2}')
count = 0
for i in random_string_2:
  for j in random_string_1:
    if i == j:
      count += 1
if count >= len(random_string_2):
  print("Из символов первой строки можно составить вторую")
else:
  print("Из символов первой строки невозможно составить вторую")