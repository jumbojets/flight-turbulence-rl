import matplotlib.pyplot as plt
import numpy as np
import math

bound_options = {
    "Light" : (0.64, 0.12),
    "Medium" : (0.79, 0.16),
    "Heavy" : (0.96, 0.18)
}
def f(x, bounds):
    u = bounds[0]
    v = bounds[1]
    if x > bounds[0]:
        m = 1 / (1 - u)
        b = 100 - m
        return m * x + b
    elif x > bounds[1]:
        a = 98 / (math.exp(u) - math.exp(v))
        b = 1 - a * math.exp(v)
        return a * math.exp(x) + b
    else:
        m = 1 / v
        return m * x

for size, bounds in bound_options.iteritems():

    edr = np.arange(0, 1, 0.005)
    c = [f(val, bounds) for val in edr]

    plt.plot(edr, c)

    plt.title('Turbulence Cost For ' + size + ' Plane')
    plt.xlabel('EDR')
    plt.ylabel('Cost')

    plt.show()
