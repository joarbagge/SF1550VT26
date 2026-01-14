'''
SF1550, Lab A, Uppgift 1, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt


def main():
    uppg1a()
    uppg1b()
    uppg1c()
    uppg1d()


def uppg1a():
    '''
    Uppgift 1a - plotta f(x)
    '''
    plt.figure(1)
    # TODO: skriv kod här ...


def uppg1b():
    '''
    Uppgift 1b - fixpunktiterationer
    '''
    # TODO: skriv kod här ...


def uppg1c():
    '''
    Uppgift 1c - Newton
    '''
    # TODO: skriv kod här ...


def uppg1d():
    '''
    Uppgift 1d - konvergensplottar
    '''
    plt.figure(2)
    # TODO: skriv kod här ...


def fixpunkt(x0, tol):
    '''
    Indata:
    x0 -- startgissning (skalär)
    tol -- feltolerans (skalär)

    Utdata:
    lista eller vektor av alla approximationer [x0,x1,x2,x3,...]
    '''
    # TODO: skriv kod här ...
    return # TODO


def newton(x0, tol):
    '''
    Indata:
    x0 -- startgissning (skalär)
    tol -- feltolerans (skalär)

    Utdata:
    lista eller vektor av alla approximationer [x0,x1,x2,x3,...]
    '''
    # TODO: skriv kod här ...
    return # TODO


if __name__ == '__main__':
    main()
    plt.show()
