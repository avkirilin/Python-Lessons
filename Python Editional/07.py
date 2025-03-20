# Удалить в строке все лишние пробелы, то есть серии подряд идущих пробелов заменить на одиночные пробелы. Крайние пробелы в строке удалить.
my_string = '       dsfdsf  dsf    sfs   dsfsdg   dsfs  gfs       dsfsfs     fsfs'
print(my_string)
my_list = my_string.split()
another_list = []
for i in range(len(my_list)):
  if i != len(my_list) - 1:
    my_list[i] += ' '
    another_list.append(my_list[i])
  else:
    another_list.append(my_list[i])
new_string = ' '.join(another_list)
print(new_string)