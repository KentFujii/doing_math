def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

a = input('Enter a number: ')
multi_table(float(a))
