import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()
def generate_F_r():
    r = range(100, 1001, 50)
    F = []
    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    draw_graph(r, F)

generate_F_r()
