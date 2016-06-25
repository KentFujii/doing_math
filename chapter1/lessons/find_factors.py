def factors(a):
    for i in range(1, a+1):
        if a % i == 0:
            print(i)

a = input('Your Number Please: ')
a = float(a)
if a > 0 and a.is_integer():
    factors(int(a))
else:
    print('Please enter a positive integer')
