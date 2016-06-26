from sympy import Symbol, factor, expand
x = Symbol('x')
y = Symbol('y')
expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3

print('Original expression: {0}'.format(expr))
factors = factor(expr)
print('Factors: {0}'.format(factors))


expanded = expand(factors)
print('Expansion: {0}'.format(expanded))
