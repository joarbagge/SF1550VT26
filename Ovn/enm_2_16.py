import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.array([1, 2.1314, 3.0365, 3.7605, 4.3398, 4.8032, 5.1739, 5.4705])
d = np.abs(np.diff(x))
S = d[1:] / d[:-1]
print('S =', S)

S = 0.8
r = (S*x[-2] - x[-1]) / (S-1)
print('r =', r)

e = np.abs(x[-1] - r)
print('e =', e)

e_trg = 0.5e-3
k = np.log(e_trg/e) / np.log(S)
print('k =', k)

if __name__ == '__main__':
    plt.show()
