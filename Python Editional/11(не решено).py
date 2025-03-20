# В строке записано десятичное число. Запишите данное число римскими цифрами.
import random
import string
our_string_num = ''.join(str(random.randint(1, 3999)))
print(our_string_num)
print(type(our_string_num))
my_dict = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', 
           '9': 'IX', '10': 'X', '20': 'XX', '30': 'XXX', '40': 'XL', '50': 'L', '60': 'LX',
           '70': 'LXX', '80': 'LXXX', '90': 'XC', '100': 'C', '200': 'CC', '300': 'CCC', '400': 'CD',
           '500': 'D', '600': 'DC', '700': 'DCC', '800': 'DCCC', '900' : 'CM', '1000': 'M',
           '2000' : 'MM', '3000' : 'MMM'}
our_string_num = list(our_string_num)
for i in our_string_num:

    print(i)
