def print_fact(num):
    if num == 0:
        return 1
    return num*print_fact(num-1)
print(print_fact(7))

