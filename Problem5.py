def min_multiple(list):
    div_val = []
    for i in range(1000000000):
        if all([i % items == 0 and i != 0 for items in list]):
            div_val.append(i)
    #minimum = min(div_val)
    print(div_val)
    #return minimum

def list_gen(max_val):
    val = 1
    list = []
    while val != max_val+1:
        list.append(val)
        val += 1
    print(list)
    return list


list = list_gen(max_val=20)
print(min_multiple(list))






