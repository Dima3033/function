def more(x,y):
    try:
        if x>y:
            print(f'{x} більше ніж {y}')
        if x<y:
            print(f'{y} більше ніж {x}')
    except Exception as ex:
        print(f'Erorr information: {ex}')
print(more(4,5))