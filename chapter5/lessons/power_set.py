from sympy import FiniteSet
s = FiniteSet(1, 2, 3)
ps = s.powerset()
print(ps)

# from sympy import FiniteSet
# s = FiniteSet(1, 2, 3)
# t = FiniteSet(2, 4, 6)
# unioned = s.union(t)
# print(unioned)

# from sympy import FiniteSet
# s = FiniteSet(1, 2)
# t = FiniteSet(2, 3)
# intersected = s.intersect(t)
# print(intersected)

# from sympy import FiniteSet
# s = FiniteSet(1, 2)
# t = FiniteSet(3, 4)
# p = s*t
# # u = FiniteSet(5, 6)
# # p = s*t*u
# for elem in p:
#         print(elem)
