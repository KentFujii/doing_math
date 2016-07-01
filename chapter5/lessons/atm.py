import random
import matplotlib.pyplot as plt
# from collections import Counter

def get_index(probability):
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    r = random.random()
    # print(sum_probability)
    for index, sp in enumerate(sum_probability):
        if r <= sp:
            # print(r)
            # print(sp)
            return index
    return len(probability)-1

# print(get_index([1/6, 1/6, 1/3, 1/3]))

def dispense():
    dollar_bills = [5, 10, 20, 50]
    probability = [1/6, 1/6, 1/3, 1/3]
    bill_index = get_index(probability)
    return dollar_bills[bill_index]

# Simulate a large number of bill withdrawls
bill_dispensed = []
for i in range(10000):
    bill_dispensed.append(dispense())
# plot a histogram
# print(Counter(bill_dispensed))
plt.hist(bill_dispensed)
plt.show()
