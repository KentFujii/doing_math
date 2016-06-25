# import matplotlib.pyplot
#
# def create_graph():
#     x_numbers=[1,2,3]
#     y_numbers=[2,4,6]
#     matplotlib.pyplot.plot(x_numbers, y_numbers)
#     matplotlib.pyplot.show()
#
# create_graph()

import matplotlib.pyplot as plt
from pylab import plot, savefig
def create_graph():
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]
    plt.plot(x_numbers, y_numbers)
    plt.show()
    plot(x_numbers, y_numbers)
    savefig('mygraph.png')

create_graph()
