'''
SF1550, Lab B, Uppgift 5, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def main():
    '''
    Uppgift 5 - högdimensionell integration
    '''
    Iexact = 6.231467927023725 # Ett noggrannt värde för I
    # TODO: skriv kod här ...


def trapets10d(n):
    '''
    Indata:
    n -- antal delintervall i varje koordinatriktning

    Utdata:
    trapetsregel-approximationen av integralen
    '''
    L = 1.2
    h = L/n

    x = np.linspace(0, L, n+1)

    I1 = np.zeros(n+1)
    I2 = np.zeros(n+1)
    I3 = np.zeros(n+1)
    I4 = np.zeros(n+1)
    I5 = np.zeros(n+1)
    I6 = np.zeros(n+1)
    I7 = np.zeros(n+1)
    I8 = np.zeros(n+1)
    I9 = np.zeros(n+1)
    I10 = np.zeros(n+1)

    for j1 in range(n+1):
        for j2 in range(n+1):
            for j3 in range(n+1):
                for j4 in range(n+1):
                    for j5 in range(n+1):
                        for j6 in range(n+1):
                            for j7 in range(n+1):
                                for j8 in range(n+1):
                                    for j9 in range(n+1):
                                        for j10 in range(n+1):
                                            I10[j10] = np.exp(j1*j2*j3*j4*j5*j6*j7*j8*j9*j10*h**10)
                                        I9[j9] = h*(np.sum(I10) - I10[0]/2 - I10[-1]/2)
                                    I8[j8] = h*(np.sum(I9) - I9[0]/2 - I9[-1]/2)
                                I7[j7] = h*(np.sum(I8) - I8[0]/2 - I8[-1]/2)
                            I6[j6] = h*(np.sum(I7) - I7[0]/2 - I7[-1]/2)
                        I5[j5] = h*(np.sum(I6) - I6[0]/2 - I6[-1]/2)
                    I4[j4] = h*(np.sum(I5) - I5[0]/2 - I5[-1]/2)
                I3[j3] = h*(np.sum(I4) - I4[0]/2 - I4[-1]/2)
            I2[j2] = h*(np.sum(I3) - I3[0]/2 - I3[-1]/2)
        I1[j1] = h*(np.sum(I2) - I2[0]/2 - I2[-1]/2)
    I = h*(np.sum(I1) - I1[0]/2 - I1[-1]/2)
    return I


if __name__ == '__main__':
    main()
    plt.show()
