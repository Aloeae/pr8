def square(s):
    for i in range(s):
        for j in range(s):
            if i == 0 or i == s - 1 or j == 0 or j == s - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  

square(10)
