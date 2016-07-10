# from sympy import Symbol, Derivative
# t = Symbol('t')
# t1 = Symbol('t1')
# St = 5*t**2 + 2*t + 8
# d = Derivative(St, t)
# delivative = d.doit().subs({t:t1})
# print(delivative)

from sympy import Derivative, Symbol
x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)
delivative = Derivative(f, x).doit()
print(delivative)
