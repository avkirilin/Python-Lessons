# Создайте функцию, которая будет получать на вход два списка, один из ключей,
# другой из значений, и возвращать словарь, созданный из этих списков.
import random
length_list = random.randint(20, 50)
first_list = [i for i in range(length_list + 1) if i > 0]
second_list = [random.randint(10, 99) for i in range(length_list)]
print(length_list)
print(first_list)
print()
print(second_list)
print()


def get_dictionary(list_1, list_2, list_length):
    my_dict = {}
    for i in range(list_length):
        my_dict[list_1[i]] = list_2[i]
    return my_dict


dictionary = get_dictionary(first_list, second_list, length_list)
print(dictionary)
