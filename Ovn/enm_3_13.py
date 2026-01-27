import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Startgissning, x = [x1,x2,x3,x4,x5]
x = np.array([0.2, 1.2, 0.3, 0.3, 0])

# Newtons metod
delta = np.inf # stort tal för att komma in i slingan
i = 0
# Vi väljer här sex decimaler = 0.5e-6
while np.max(np.abs(delta)) > 0.5e-6 and i < 7:
    x1, x2, x3, x4, x5 = x
    xtot = np.sum(x)
    f = np.array([x1 + x3 + x5 - 0.5,
                  x2 + x3 - x5 - 1.5,
                  x3 - 3*x5 - x4,
                  x4*x3 - 0.5*x1*x2,
                  x5*x2*xtot**2 - 0.09*x1*x4**3])
    C = 2*x5*x2*xtot
    J = np.array([[1, 0, 1, 0, 1],
                  [0, 1, 1, 0, -1],
                  [0, 0, 1, -1, -3],
                  [-0.5*x2, -0.5*x1, x4, x3, 0],
                  [C-0.09*x4**3, x5*xtot**2+C, C, C-3*0.09*x1*x4**2, x2*xtot**2+C]])
    delta = -np.linalg.solve(J, f)
    print(i, x, np.max(np.abs(delta)))
    x += delta
    i += 1
print(i, x)

if __name__ == '__main__':
    plt.show()
