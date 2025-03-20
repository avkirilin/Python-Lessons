# Дан список строк. Упорядочить массив по длине строк.
import random, string, operator


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def sort_list(list):
    length_list = []
    for i in range(len(list)):
        length_list.append(len(list[i]))
    my_dict = dict(zip(list, length_list))
    sorted_my_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
    last_list = []
    for key, item in sorted_my_dict.items():
        print(f"{item} \t\t {key}")
        last_list.append(key)
    print()
    print(last_list)


my_list = []
my_string = str()
rand_list_length = random.randint(5, 150)
word = str()
if rand_list_length % 10 == 1:
    word = 'слова'
else: word = 'слов'
print(f'Список состоит из {rand_list_length} {word}')
for i in range(rand_list_length):
    length = random.randint(1, 62)
    my_string = generate_alphanum_random_string(length)
    my_list.append(my_string)
print(my_list)
print()
another_list = sort_list(my_list)