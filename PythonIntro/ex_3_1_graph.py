import numpy as np
import matplotlib.pyplot as plt

# Funktion att plotta
f = lambda x: np.sin(x) / x

plt.figure() # skapar en ny figur
x = np.linspace(-20, 20, 200)
y = f(x)
plt.plot(x, y, label='$f(x)$') # Plotta
plt.grid() # Lägg till rutnät
plt.legend() # Lägg till förklaring (använder label från plt.plot)
plt.xlabel('$x$') # Lägg till etikett på x-axeln
plt.ylabel('$y$') # Lägg till etikett på y-axeln
plt.title(r'Funktionsgraf för $f(x) = \sin(x)/x$') # Lägg till rubrik
plt.ylim([-0.5, 1.5]) # Ändra y-axelns gränser

if __name__ == '__main__':
    plt.show()
