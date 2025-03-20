# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
getting_number = int(input("Введите целое не отрицательное число n для нахождения его факториала: "))
count = 2
pre_fibonaci_number = 1
fibonaci_number = 1
while fibonaci_number < getting_number:
    temp = fibonaci_number
    fibonaci_number = fibonaci_number + pre_fibonaci_number
    pre_fibonaci_number = temp
    count += 1
print(count if getting_number == fibonaci_number else '-1')