def largest_palindrom(a, b):
    for num in range(a, b, -1):
        for num2 in range(a, b, -1):
            multi_val = num * num2
            multi_val = str(multi_val)
            if multi_val[:] == multi_val[::-1]:
                multi_val = int(multi_val)
                print(multi_val)
                return multi_val


largest_palindrom(99, 9)
largest_palindrom(999, 99)