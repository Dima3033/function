def print_rec(n1, n2):
    try:
        for i in range(n1):
            for j in range(n2):
                if i == 0 or i == n1 - 1:
                    print(f'* ', end=' ')
                else:
                    if j == 0 or j == n2 - 1:
                        print(f'* ', end=" ")
                    else:
                        print(f'  ', end=" ")
            print()
    except Exception as ex:
        print(f'Erorr information: {ex}')
print_rec(7, 9)