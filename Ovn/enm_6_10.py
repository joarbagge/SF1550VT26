import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# (a)
f = lambda x: np.exp(x) / (1 + 2*x**3)
a = 0
b = np.arcsin(1)
I = sp.integrate.quad(f, a, b, epsrel=0.5e-8)[0]
print('I =', I)

# (b)
# Beräkning av I_L med L=10.99
f = lambda t: 2 / (t**4 + 2*t**2 + 2)**(3/2)
a = 0
b = 10.99
IL = sp.integrate.quad(f, a, b, epsabs=0.25e-5)[0]
print('IL =', IL)

if __name__ == '__main__':
    plt.show()
