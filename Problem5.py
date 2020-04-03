## -*- coding: utf-8 -*-
def list_generator(max_val):
    val = 1
    list = []
    while val != max_val+1:
        list.append(val)
        val += 1
    return list

# Ф-я для нахождения простых множителей
def multipliers(n):
    factors = []
    d = 2
    m = n
    while d * d <= n:
            if n % d == 0:
                factors.append(d)
                n //= d
            else:
                d += 1
    factors.append(n)
    return factors
    # print('{} = {}' .format(m, factors))

# Создает список из всех простых множителей каждого числа в списке
fac_list = list()
for el in list_generator(20):
    fac_list.append(multipliers(el))

# Находим наибольшее количество вхождений введенного простого числа в рамках списка
def degree_of_number(value):
    multip = list()
    for el in fac_list:
        el = el.count(value)
        multip.append(el)

    #print(multip)
    max_mult = max(multip)
    #print(max_mult)
    if max_mult != 0:
        degree = value ** max_mult
        return degree
    else:
        return 1


degree_of_number_lst = list()
for i in range(1, 20):
    degree_of_number_lst.append(degree_of_number(i))
#print(degree_of_number_lst)

def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer


print(multiply(degree_of_number_lst))




