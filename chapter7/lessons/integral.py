# from sympy import Integral, Symbol
# x = Symbol('x')
# k = Symbol('k')
# intg = Integral(k*x, x).doit()
# print(intg)

# from sympy import Integral, Symbol
# x = Symbol('x')
# k = Symbol('k')
# intg = Integral(k*x, (x, 0, 2)).doit()
# print(intg)

# from sympy import Symbol, exp, sqrt, pi, Integral
# x = Symbol('x')
# p = exp(-(x - 10)**2/2)/sqrt(2*pi)
# intg = Integral(p, (x, 11, 12)).doit().evalf()
# print(intg)

from sympy import Symbol, exp, sqrt, pi, Integral, S
x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
intg = Integral(p, (x, S.NegativeInfinity, S.Infinity)).doit().evalf()
print(intg)
