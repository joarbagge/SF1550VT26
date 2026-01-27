import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Parametervärden
k1 = 0.12
k2 = 0.22
atot = 0.60
btot = 1.0

# Startgissning, x = [a, b]
x = np.array([atot/2, btot/2])

# Newtons metod
delta = np.inf # stort tal för att komma in i slingan
i = 0
# Tre decimaler = 0.5e-3, här tar vi i lite mer med 1e-4
while np.max(np.abs(delta)) > 1e-4 and i < 10:
    a = x[0]
    b = x[1]
    f = np.array([a + k1*a*b + k2*a*b**2 - atot,
                  b + k1*a*b + 2*k2*a*b**2 - btot])
    J = np.array([[1 + k1*b + k2*b**2, k1*a + 2*k2*a*b],
                  [k1*b + 2*k2*b**2, 1 + k1*a + 4*k2*a*b]])
    delta = -np.linalg.solve(J, f)
    print(i, x, delta)
    x += delta
    i += 1

if __name__ == '__main__':
    plt.show()
