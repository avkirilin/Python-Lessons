# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
ticket_number = int(input("Введите шестизначный номер билета: "))
if ticket_number > 99999 and ticket_number < 1000000:
    first_num = int((ticket_number / 100000) % 10)
    second_num = int((ticket_number / 10000 ) % 10)
    third_num = int((ticket_number / 1000 ) % 10)
    fourth_num = int((ticket_number / 100 ) % 10)
    fifth_num = int((ticket_number / 10 ) % 10)
    sixth_num = int(ticket_number % 10)
    if first_num + second_num + third_num == fourth_num + fifth_num + sixth_num:
        print(f"Данный билет счастливый, т.к. сумма чисел {first_num}, {second_num}, {third_num} равна сумме чисел {fourth_num}, {fifth_num}, {sixth_num}")
    else:
        print(f"Данный билет не счастливый, т.к. сумма чисел {first_num}, {second_num}, {third_num} не равна сумме чисел {fourth_num}, {fifth_num}, {sixth_num}")
else:
    print("Введен некорректный номер билета")