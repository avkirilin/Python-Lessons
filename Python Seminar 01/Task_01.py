# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

per_day = int(input('Введите количество километров, которое проезжает машина за день '))
total_distance = int(input('Введите количество километров, которое необходимо проехать '))
print ('Чтобы проехать заданное кол-во километров, машине необходимо ехать', int((total_distance + per_day - 1) / per_day), 'дня(ей)')