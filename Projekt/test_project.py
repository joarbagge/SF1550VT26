'''
SF1550, Projekt, VT26

Exempelfil som visar hur lösaren används.
'''

import numpy as np
import matplotlib.pyplot as plt
import heatsolver


def main():
    # Testa att lösa problemet utan någon värmekälla
    sol = heatsolver.solve(N=28, temp_ute=5)

    # Plotta lösningen
    plt.figure(1)
    plt.clf()
    sol.plot() # plotta temperaturen som färg
    plt.colorbar(label='Temperatur (°C)')
    # Plotta även konturlinjer vid temperaturerna 10°C och 15°C:
    sol.plot_contours(colors='black', linewidths=0.6, alpha=0.5,
                      levels=[10, 15])
    plt.xlim([-0.5, 8.0])
    plt.title('Temperatur i ouppvärmt rum')
    return


if __name__ == '__main__':
    main()
    plt.show()
