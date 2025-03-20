# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
count = int(input("Введите кол-во арбузов в отделе на рынке: "))
count += 1
weight_watermelon = random.randint(3000, 15000)
print(f"Вес выбранного арбуза с прилавка равен: {weight_watermelon}г")
min_weght_watermelon = weight_watermelon
max_weght_watermelon = weight_watermelon
current_watermelon = 1
while current_watermelon < count:
    weigth_another_watermelon = random.randint(3000, 15000)
    print (f"Вес {current_watermelon} арбуза равен: {weigth_another_watermelon}г")
    current_watermelon += 1
    if min_weght_watermelon > weigth_another_watermelon:
        min_weght_watermelon = weigth_another_watermelon
    elif max_weght_watermelon < weigth_another_watermelon:
        max_weght_watermelon = weigth_another_watermelon
print(f"Минимальный вес арбуза на прилавке: {min_weght_watermelon}г, максимальный вес арбуза на прилавке: {max_weght_watermelon}г")