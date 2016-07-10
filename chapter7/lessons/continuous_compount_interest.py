from sympy import Symbol, Limit, S
n = Symbol('n')
p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
limit = Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit()
print(limit)
