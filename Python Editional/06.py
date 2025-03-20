# Удалите в строке все буквы 'x'. за которыми следует 'abc'.
my_string = 'kjfdasjhfdsjhfdjashfdjashkjxabcjdfasxabc'
print(my_string)
new_string = my_string.replace('xabc', 'abc')
print(new_string)