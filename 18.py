# Дан список названий переменных в camelCase. Преобразовать названия в snake_case.
my_list = ['firstVariable', 'secondVariable', 'thirdVariable', 'fourVariable', 'fiveVariable', 'sixVariable',
           'sevenVariable', 'eightVariable', 'nineVariable', 'tenVariable', 'elevenVariable', 'twelveVariable']
print()
print('Список переменных, заданных в camelCase: ')
print(my_list)
print()
new_list = []
for i in my_list:
    for j in i:
        if j in 'ABCDEFGIJKLMNOPQRSTUVWXYZ':
            new_list.append('_')
            new_list.append(j.lower())
        else:
            new_list.append(j)
    if i != my_list:
        new_list.append(' ')
my_string = ''.join(new_list).split(' ')
my_string = list(my_string)
last_list = []
for i in range(len(my_string)):
    if my_string[i] != '':
        last_list.append(my_string[i])
print('Список переменных, переведенных в snake_case: ')
print(last_list)
