1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

list = [1, 2, 3]
list2 = []

def list_sum(numList):
    the_Sum = 0
    for i in numList:
        the_Sum = the_Sum + i
    return the_Sum

for n in range(3, 100000):
    f = (list[n - 1]) + (list[n - 2])
    list.append(f)
    if f <= 100000 and f % 2 == 0:
        list2.append(f)
        print('List2: ', list2)
        print('List_sum: ', list_sum(list2))
