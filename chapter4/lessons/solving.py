# from sympy import Symbol, solve
# x = Symbol('x')
# expr = x - 5 - 7
# print(solve(expr))

# from sympy import Symbol, solve
# x = Symbol('x')
# expr = x**2 + 5*x + 4
# print(solve(expr, dict=True))

# from sympy import Symbol, solve
# x=Symbol('x')
# expr = x**2 + x + 1
# print(solve(expr, dict=True))

# from sympy import Symbol, solve
# x = Symbol('x')
# a = Symbol('a')
# b = Symbol('b')
# c = Symbol('c')
# expr = a*x*x + b*x + c
# print(solve(expr, x, dict=True))

# from sympy import Symbol, solve, pprint
# s = Symbol('s')
# u = Symbol('u')
# t = Symbol('t')
# a = Symbol('a')
# expr = u*t + (1/2)*a*t*t - s
# t_expr = solve(expr,t, dict=True)
# pprint(t_expr)

from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
print(solve((expr1, expr2), dict=True))
