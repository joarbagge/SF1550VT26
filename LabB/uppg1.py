'''
SF1550, Lab B, Uppgift 1, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import trussplot
import trussanim


def main():
    uppg1b()
    uppg1c()
    uppg1d()


def uppg1b():
    '''
    Uppgift 1b - visualisering
    '''
    # TODO: skriv kod här ...


def uppg1c():
    '''
    Uppgift 1c - beräkning av största och minsta egenvärdena
    '''
    # TODO: skriv kod här ...


def uppg1d():
    '''
    Uppgift 1d - beräkning av andra egenvärden
    '''
    # TODO: skriv kod här ...


def potens(A, tol):
    '''
    Indata:
    A -- matrisen (kvadratisk)
    tol -- feltolerans (skalär)

    Utdata:
    tuple med två element:
    - största egenvärdet till A (skalär)
    - array eller lista med ändringen i egenvärdesapproximationen
      för varje iteration, dvs my_{k+1} - my_k.
    '''
    # TODO: skriv kod här ...
    return # TODO


def inverspotens(A, tol):
    '''
    Indata:
    A -- matrisen (kvadratisk)
    tol -- feltolerans (skalär)

    Utdata:
    tuple med två element:
    - minsta egenvärdet till A (skalär)
    - array eller lista med ändringen i egenvärdesapproximationen
      för varje iteration, dvs my_{k+1} - my_k.
    '''
    # TODO: skriv kod här ...
    return # TODO


if __name__ == '__main__':
    main()
    plt.show()
