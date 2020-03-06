# Задача: Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
from datetime import datetime
import time

start_time = datetime.now()
number = 600851475#143
dividers_list = list()

#Находим делители числа. Если остаток от деления на некоторое число i равен 0, то i является делителем n
for numbers in range(1, number):
    if number % numbers == 0:
        dividers_list.append(numbers)
        print('Итерация {}'.format(numbers), 'Время исполнения: ', datetime.now() - start_time)

    else:
        continue
print(dividers_list)
print(datetime.now() - start_time)
