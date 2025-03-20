# Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'
my_string = 'abcsdfasflk;jsafsagjhasdgkjhasdghadskgjhasd;kjgaksd;g'
my_list = list(my_string)
if my_list[0] == 'a' and my_list[1] == 'b' and my_list[2] == 'c':
    my_list.pop(0)
    my_list.pop(0)
    my_list.pop(0)
    my_list.insert(0, 'w')
    my_list.insert(0, 'w')
    my_list.insert(0, 'w')
    print(''.join(my_list))
else:
    my_new_string = my_string + 'zzz'
    print(my_new_string)