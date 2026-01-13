import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def main():
    f = lambda x: sp.special.erf(x)
    plt.figure()
    x = np.linspace(-4, 4, 200)
    y = f(x)
    plt.plot(x, y, label='$f(x)$')
    plt.plot(x, (2/np.sqrt(np.pi))*x, 'k--', linewidth=1,
             label='Tangentlinje')
    plt.grid()
    plt.legend()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title(r'Funktionsgraf för $f(x) = \text{erf}(x)$')
    plt.ylim([-2, 2])

if __name__ == '__main__':
    main()
    plt.show()
