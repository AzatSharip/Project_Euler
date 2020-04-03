def square_sum(rang):
    lst = [x+1 for x in range(0-1, rang)]
    sum_sqr = sum(i**2 for i in lst)
    sqr_sum = sum(i for i in lst) ** 2
    difference = sqr_sum - sum_sqr
    print(difference)

square_sum(100)