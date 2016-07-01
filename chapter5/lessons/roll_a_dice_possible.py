from sympy import FiniteSet
import random
def find_prob(target_score, max_rolls):
    die_sides = FiniteSet(1, 2, 3, 4, 5, 6)
    # sample space
    s = die_sides**max_rolls
    # Find the event set
    if max_rolls > 1:
        success_rolls = []
        for elem in s:
            if sum(elem) >= target_score:
                success_rolls.append(elem)
    else:
        if target_score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in die_sides:
                if roll >= target_score:
                    success_rolls.append(roll)
    e = FiniteSet(*success_rolls)
    # calculate the probability of reaching target score
    print(e)
    print(s)
    return len(e)/len(s)

target_score = int(input('Enter the target score: '))
max_rolls  = int(input('Enter the maximum number of rolls allowed: '))
p = find_prob(target_score, max_rolls)
print('Probability:  {0:.5f}'.format(p))
