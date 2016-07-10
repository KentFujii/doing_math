import math
import matplotlib.pyplot as plt
from sympy import Derivative, Symbol, sin, cos, solve

# def plot_range_theta(u):
#     g = 9.8
#     angles = range(0, 90, 1)
#     R = [u**2*math.sin(math.radians(2*angle))/g for angle in angles]
#     plt.plot(angles, R)
#     # Use LaTex for the X-axis label
#     #plt.rc('text', usetex=True)
#     plt.plot(angles, R)
#     #plt.xlabel(r'$\theta$ : Angle of projection (degrees)')
#     plt.ylabel('R: Distance traveled by projectile (meters)')

def grad_ascent(x0, f1x):
    theta = Symbol('theta')
    epsilon =  1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({theta:x_old}).evalf()

    X = []
    while abs(x_old - x_new) > epsilon:
        X.append(x_new)
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({theta:x_old}).evalf()

    return x_new, X

def find_max_theta(R, theta):
    # Calculate the first derivative
    R1theta = Derivative(R, theta).doit()
    theta0 = 1e-3
    theta_max, X = grad_ascent(0.001, R1theta)
    return math.degrees(theta_max.evalf()), X

g = 9.8
# Assume initial velocity
u = 25
# plot_range_theta(u)
theta = Symbol('theta')
# Expression for range
R = u**2*sin(2*theta)/g
theta_max, X = find_max_theta(R, theta)

# calculate R for all theta's traversed
Y = [u**2*math.sin(2*angle)/g for angle in X]
X = [math.degrees(angle) for angle in X]
plt.plot(X, Y, 'ro')
plt.show()
print('Theta: {0}, Max. Range: {1}'.format(theta_max, R.subs({theta:theta_max})))
