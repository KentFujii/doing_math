from sympy import Symbol, pprint, init_printing
def print_series(n, x_value):
    # initialize printing system with
    # reverse order
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
    # evaluate the series at x_value
    series_value = series.subs({x:x_value})
    print('Value of the series at {0}: {1}'.format(x_value, series_value))

n = input('Enter the number of terms you want in the series: ')
x_value = input('Enter the value of x at which you want to evaluate the series: ')
print_series(int(n), float(x_value))
