'''
Exempel från Föreläsning 4 (2026-01-27)
'''

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Lös f(x) = 0
    f = lambda x: x**2 - 6*x + 4
    fprim = lambda x: 2*x - 6

    # Plotta funktionen för att hitta startgissningar
    plt.clf()
    x = np.linspace(0, 6, 200)
    plt.plot(x, f(x))
    plt.grid()

    # Startgissning
    x = 5
    diff = np.inf # tal större än toleransen
    tolerans = 1e-12
    # Newtons metod
    while np.abs(diff) >= tolerans:
        diff = -f(x)/fprim(x)
        x += diff
        print(x, diff)
    plt.plot(x, f(x), '*')
    return


if __name__ == '__main__':
    main()
    plt.show()
