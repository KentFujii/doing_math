from sympy import Symbol, factor, expand
x = Symbol('x')
y = Symbol('y')
expr = x**2 - y**2
f = factor(expr)
print(f)
# Expand
print(expand(f))
