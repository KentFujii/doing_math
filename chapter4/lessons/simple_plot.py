# from sympy.plotting import plot
# from sympy import Symbol
# x = Symbol('x')
# plot(2*x+3)

from sympy import plot, Symbol
x = Symbol('x')
plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3')
