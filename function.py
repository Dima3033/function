def print_defec(n):
    try:
        counter = 0
        for i in range(1, n +1):
            if n % i == 0:
                counter += 1
        if counter == 2:
            print(f'{n}просте число')
        else:
            print(f'{n}не просте число')
    except Exception as ex:
        print(f'Erorr information: {ex}')
number = int(input('numver->'))
print_defec(number)