# def prime_numbers(rang, ind):
#     list = [x+1 for x in range(1, rang)]
#     for el in list:
#         if el % 2 == 0 and el != 2:
#             list.remove(el)
#     for el in list:
#         if el % 3 == 0 and el != 3:
#             list.remove(el)
#     for el in list:
#         if el % 5 == 0 and el != 5:
#             list.remove(el)
#     for el in list:
#         if el % 7 == 0 and el != 7:
#             list.remove(el)
#     print(list[ind-1])
#
# prime_numbers(100000, 10001)


def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
        else:
            counter += 1
        if counter == n:
            return i

print(nth_prime(10001))