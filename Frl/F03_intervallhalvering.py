'''
Exempel från Föreläsning 3 (2026-01-22)
'''

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Lös f(x) = 0
    f = lambda x: np.cos(x) - x

    # Startgissningar. OBS: f(a) och f(b) ska ha olika tecken.
    a = 0
    b = 1
    fa = f(a)
    fb = f(b)

    # Plotta funktionen på intervallet
    plt.clf()
    x = np.linspace(a, b, 200)
    plt.plot(x, f(x))
    plt.grid()

    # Starta metoden
    x = (a+b)/2
    fx = f(x)
    felgrans = (b-a)/2
    feltolerans = 1e-8
    i = 0 # räknare
    print(i, x, fx, felgrans)
    while felgrans >= feltolerans:
        if fa*fx < 0: # olika tecken
            (a, b) = (a, x)
            (fa, fb) = (fa, fx)
        elif fx == 0: # vi har hittat roten!
            break
        else: # fx*fb < 0, dvs behåll [x,b]
            (a, b) = (x, b)
            (fa, fb) = (fx, fb)
        x = (a+b)/2
        fx = f(x)
        felgrans = (b-a)/2
        i += 1
        print(i, x, fx, felgrans)
    return


if __name__ == '__main__':
    main()
    plt.show()
