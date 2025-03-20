# Дан список, в котором количество отрицательных элементов равно количеству положительных.
# Поменяйте местами первый отрицательный и первый положительный, второй отрицательный и
# второй положительный и так далее.
import random
length_list = random.randint(2, 20) * 2
list = [random.randint(1, 9) for i in range(length_list)]
for i in range(len(list)):
  if i % 2 == 0:
    list[i] = list[i] * (-1)
print()
random.shuffle(list)
print(list)
positive_list = []
negative_list = []
for i in range(len(list)):
  if list[i] > 0:
    positive_list.append(i)
  else:
    negative_list.append(i)
for i in range(int(len(list) / 2)):
  list[positive_list[i]], list[negative_list[i]] = list[negative_list[i]], list[positive_list[i]]
print(list)