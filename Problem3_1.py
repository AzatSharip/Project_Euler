# Задача: Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
from datetime import datetime
import time

start_time = datetime.now()
def one():
    res = []
    x = 131195
    z = 2
    while z * z <= x:
        if x % z == 0:
            res.append(z)
            z += 1
        else:
            z += 1
    print(res)
    return res
one()



print(datetime.now() - start_time)
