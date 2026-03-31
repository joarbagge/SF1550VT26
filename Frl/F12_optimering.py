'''
Exempel: optimering i 2 dimensioner. Frl 12 (2026-03-31).
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def main():
    # Rita funktionen i planet
    x1 = np.linspace(-1, 2)
    x2 = np.linspace(-2, 2)
    X1, X2 = np.meshgrid(x1, x2)
    f = X1**4 + X2**4 + 2*X1**2*X2**2 + 6*X1*X2 - 4*X1 - 4*X2 + 1
    plt.contourf(X1, X2, f)
    #plt.pcolormesh(X1, X2, f)
    plt.colorbar()

    # Newtons metod -- vi behöver gradienten och Hessianen
    gradf = lambda x1, x2: np.array([
        4*x1**3 + 4*x1*x2**2 + 6*x2 - 4,
        4*x2**3 + 4*x1**2*x2 + 6*x1 - 4,
    ])
    H = lambda x1, x2: np.array([
        [12*x1**2 + 4*x2**2, 8*x1*x2 + 6],
        [8*x1*x2 + 6, 12*x2**2 + 4*x1**2],
    ])

    # TODO

    # Gradientsökning
    # TODO

    return

if __name__ == '__main__':
    main()
    plt.show()
