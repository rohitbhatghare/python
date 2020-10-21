rows = 6
for i in range(1, rows):
    num = 1
    for l in range(i):
        print('   ', end='')
    for k in range(i , rows):
        print(num,' ', end='')
        num += 1
    print('\n')
