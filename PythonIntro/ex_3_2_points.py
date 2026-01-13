import numpy as np
import matplotlib.pyplot as plt

def main():
    # Datapunkter att plotta
    x = np.arange(0, 5+0.5, 0.5)
    y = np.array([-1.2, -0.15, -0.01, -0.83, 0.68, -0.68, 1.5, -1.4,
                  -1.3, 0.65, 0.57])

    fig = plt.figure(5) # skapar ny figur med givet nummer
    plt.clf() # rensar figuren innan plottning
    # Låt oss filtrera datapunkterna baserat på om deras y-värde
    # är positivt eller negativt, och plotta med olika stilar.
    neg = (y < 0)
    pos = ~neg
    plt.plot(x[pos], y[pos], 'o', markerfacecolor='none',
             label='Datapunkter ($+$)')
    plt.plot(x[neg], y[neg], 'x', label='Datapunkter ($-$)')

    plt.grid() # Lägg till rutnät
    plt.legend() # Lägg till förklaring (använder label från plt.plot)
    plt.xlabel('$x$') # Lägg till etikett på x-axeln
    plt.ylabel('$y$') # Lägg till etikett på y-axeln
    plt.title('Datapunkter') # Lägg till rubrik
    plt.ylim([-2, 2]) # Ändra y-axelns gränser

if __name__ == '__main__':
    main()
    plt.show()
