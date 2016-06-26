from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})
print(res)
