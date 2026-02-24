'''
Exempel på linjära minstakvadratmetoden. Frl 9 (2026-02-24).
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.clf()
    # Prova polynomanpassning med olika gradtal
    polynom(0)
    polynom(1)
    polynom(2)
    polynom(3)
    # Prova anpassningar med modellen
    # g(x) = c0*exp(-0*x) + c1*exp(-1*x) + ... cm*exp(-m*x)
    exp_modell(1)
    exp_modell(3)
    return

def datapunkter(num=50):
    '''
    Skapa och returnera datapunkter med brus
    '''
    x = np.linspace(0, 1, num)
    rng = np.random.default_rng(20260224) # ger samma brus varje gång
    y = 1 - np.exp(-5*x) + 0.1*rng.random(x.shape)
    return x, y

def polynom(m):
    '''
    Polynomanpassning med gradtal m.
    '''
    x, y = datapunkter()

    # Anpassa polynom med minstakvadratmetoden
    p = np.polynomial.Polynomial.fit(x, y, m)
    print(p)

    # Rita datapunkter och modellen
    plt.subplot(2, 1, 1)
    plt.plot(x, y, '.k')
    xfin = np.linspace(0, 1, 200)
    plt.plot(xfin, p(xfin), label=f'Poly $m={m}$')
    plt.title('Data och modell')
    plt.legend()

    # Rita residualvektorns komponenter
    r = p(x) - y
    plt.subplot(2, 1, 2)
    plt.plot(x, r, label=f'Poly $m={m}$')
    plt.title('Residualer')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return

def exp_modell(m):
    '''
    Modell g(x) = c0*exp(-0*x) + c1*exp(-1*x) + ... cm*exp(-m*x)
    '''
    x, y = datapunkter()

    # Anpassa modell med minstakvadratmetoden
    mv = np.arange(m+1).reshape(1, -1) # radvektor
    xv = x.reshape(-1, 1) # kolumnvektor
    V = np.exp(-mv*xv) # matris (xv.size, mv.size)
    c = np.linalg.lstsq(V, y)[0]
    print('Exp-modell:', c)

    # Funktion för anpassad modell
    def g(x):
        y = np.zeros(x.shape)
        for k in range(c.size):
            y += c[k] * np.exp(-k*x)
        return y
    #g = lambda x: np.exp(-mv*x.reshape(-1,1)) @ c # ekvivalent

    # Rita datapunkter och modellen
    plt.subplot(2, 1, 1)
    plt.plot(x, y, '.k')
    xfin = np.linspace(0, 1, 200)
    plt.plot(xfin, g(xfin), '--', label=f'Exp $m={m}$')
    plt.title('Data och modell')
    plt.legend()

    # Rita residualvektorns komponenter
    r = g(x) - y
    plt.subplot(2, 1, 2)
    plt.plot(x, r, '--', label=f'Exp $m={m}$')
    plt.title('Residualer')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return

if __name__ == '__main__':
    main()
    plt.show()
