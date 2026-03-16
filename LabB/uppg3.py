'''
SF1550, Lab B, Uppgift 3, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def main():
    '''
    Uppgift 3 - minsta kvadratmetoden
    '''
    t, y = load_data()
    # t -- antal år efter januari 1980 (en datapunkt per månad)
    # y -- konsumentprisindex (KPI)
    # TODO: skriv kod här ...


def load_data():
    # Läs in kolumn nummer två från filen (KPI-värdena).
    # Hoppa över de tre första raderna eftersom de inte innehåller data.
    y = np.loadtxt('KPI.csv', delimiter=',', skiprows=3, usecols=1)
    # Skapa en vektor t som innehåller antal år från januari 1980
    # (första datapunkten). Vi delar med 12 eftersom det är en
    # datapunkt per månad och vi vill ha antal år (som flyttal).
    t = np.arange(y.size) / 12
    return t, y


if __name__ == '__main__':
    main()
    plt.show()
