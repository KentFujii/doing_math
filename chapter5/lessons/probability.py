from sympy import FiniteSet
s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.union(b)
print(len(e)/len(s))

# from sympy import FiniteSet
# s = FiniteSet(1, 2, 3, 4, 5, 6)
# a = FiniteSet(2, 3, 5)
# b = FiniteSet(1, 3, 5)
# e = a.intersect(b)
# print(len(e)/len(s))
