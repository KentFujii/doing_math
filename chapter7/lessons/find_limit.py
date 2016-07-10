# # Simple example of finding the limit
# from sympy import Limit, Symbol, S
# x = Symbol('x')
# limit = Limit(1/x, x, S.Infinity).doit()
# print(limit)

# # Specifying the limit direction: positive
# from sympy import Limit, Symbol
# x = Symbol('x')
# limit = Limit(1/x, x, 0, dir='+').doit()
# print(limit)

# # Specifying the limit direction: negative
# from sympy import Limit, Symbol
# x = Symbol('x')
# limit = Limit(1/x, x, 0, dir='-').doit()
# print(limit)

# Indeterminate limit example
from sympy import Limit, Symbol, sin
x = Symbol('x')
limit = Limit(sin(x)/x, x, 0).doit()
print(limit)
