# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

our_number = int(input("Введите любое целое трехзначное число: "))
if our_number > 99 and our_number < 1000:
    first_num = int((our_number / 100) % 10)
    second_num = int((our_number / 10 ) % 10)
    third_num = int(our_number % 10)
    print (f"Сумма цифр {first_num}, {second_num}, {third_num} данного числа равна: {first_num + second_num + third_num}")
else:
    print("Введено не корректное значение")    