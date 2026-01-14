'''
SF1550, Lab A, Uppgift 2, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt


def main():
    uppg2b()
    uppg2c()
    uppg2d()


def uppg2b():
    '''
    Uppgift 2b
    '''
    # TODO: skriv kod här ...


def uppg2c():
    '''
    Uppgift 2c
    '''
    # TODO: skriv kod här ...


def uppg2d():
    '''
    Uppgift 2d
    '''
    # TODO: skriv kod här ...


def punkter(X0, ra, rb, a, b, tol=1e-10):
    '''
    Indata:
    X0 -- vektor med startgissningarna, np.array([x1,y1,x2,y2])
    ra -- radie för cirkel a (skalär)
    rb -- radie för cirkel b (skalär)
    a -- vektor med koordinater för mittpunkt a, np.array([xa,ya])
    b -- vektor med koordinater för mittpunkt b, np.array([xb,yb])
    tol -- feltolerans (skalär), valfri

    Utdata:
    tuple med två element:
    - vektor med lösningen, np.array([x1,y1,x2,y2])
    - antal iterationer som använts
    '''
    # TODO: skriv kod här ...
    return # TODO


def langd(ra, rb, rc, a, b, c):
    '''
    Indata:
    ra -- radie för cirkel a (skalär)
    rb -- radie för cirkel b (skalär)
    rc -- radie för cirkel c (skalär)
    a -- vektor med koordinater för mittpunkt a, np.array([xa,ya])
    b -- vektor med koordinater för mittpunkt b, np.array([xb,yb])
    c -- vektor med koordinater för mittpunkt c, np.array([xc,yc])

    Utdata:
    tuple med två element:
    - längden på snöret (skalär)
    - de tre lösningsvektorerna samlade i en matris (4 rader, 3 kolumner),
      np.column_stack([Xab, Xbc, Xca])
    '''
    # TODO: skriv kod här ...
    return # TODO


if __name__ == '__main__':
    main()
    plt.show()
