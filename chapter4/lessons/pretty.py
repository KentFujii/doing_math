from sympy import Symbol, pprint, init_printing
x = Symbol('x')
y = Symbol('y')
expr = x*x + 2*x*y + y*y
pprint(expr)
# Reverse order lexicographical
init_printing(order='rev-lex')
expr = 1 + 2*x + 2*x**2
pprint(expr)
