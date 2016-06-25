def is_factor(a, b):
    if int(b) % int(a) == 0:
        return True
    else:
        return False

a = input('Checking if a number is a factor of another(denominator): ')
b = input('Checking if a number is a factor of another(numerator): ')
print(is_factor(a, b))
