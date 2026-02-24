'''
Exempel på icke-linjära minstakvadratmetoden. Frl 9 (2026-02-24).
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Datapunkter
    # Mät tiden som antal år efter 1950
    t = np.array([1950, 1955, 1960, 1965, 1970, 1975, 1980]) - 1950
    y = np.array([53.05, 73.04, 98.31, 139.78, 193.48, 260.20, 320.39])

    # Testa Gauss-Newtons metod
    g1 = gauss_newton(t, y, c0=np.array([0.0, 0.0]))

    # Testa linjär ersättningsmodell
    g2 = linear(t, y)

    # Mät residualvektorns norm i de båda fallen
    r1 = np.linalg.norm(g1(t) - y)
    r2 = np.linalg.norm(g2(t) - y)
    print('Residual för Gauss-Newton:', r1)
    print('Residual för linjäriserade modellen:', r2)

    # Plotta resultaten
    plt.clf()
    plt.subplot(2, 1, 1)
    plt.plot(t+1950, y, 'k.')
    tfin = np.linspace(1950, 1980) - 1950
    plt.plot(tfin+1950, g1(tfin), label='Gauss-Newton')
    plt.plot(tfin+1950, g2(tfin), label='Linjäriserad')
    plt.legend()
    plt.title('Data och modell')

    plt.subplot(2, 1, 2)
    plt.plot(t+1950, g1(t)-y, label='Gauss-Newton')
    plt.plot(t+1950, g2(t)-y, label='Linjäriserad')
    plt.legend()
    plt.grid(True)
    plt.title('Residualer')
    plt.tight_layout()

    return

def gauss_newton(t, y, c0):
    '''
    Modellanpassning y = a*exp(b*t) med Gauss-Newton.
    '''
    # Definiera residualvektorn
    # c = [a, b]
    F = lambda c: c[0]*np.exp(c[1]*t) - y
    # Definiera Jacobimatrisen till F
    J = lambda c: np.column_stack((
        np.exp(c[1]*t), # dF/da
        c[0]*np.exp(c[1]*t)*t, # dF/db
    ))

    # Gauss-Newtons metod
    c = c0 # Startgissning
    tol = 1e-10
    delta = np.inf
    i = 0
    while np.linalg.norm(delta) >= tol:
        delta = np.linalg.lstsq(J(c), -F(c))[0]
        c += delta
        i += 1
        print(i, c, delta)

    # Definiera modellen
    a, b = c
    g = lambda t: a*np.exp(b*t)
    print(f'Gauss-Newton: a={a}, b={b}')
    return g

def linear(t, y):
    '''
    Modellanpassning linjär ersättningsmodell.
    '''
    # Logaritmering ger log(y) = log(a) + b*t.
    # Inför c = [log(a), b] som okända.
    # Linjärt system [1, t] @ c = log(y)
    A = np.column_stack((np.ones(t.shape), t))
    c = np.linalg.lstsq(A, np.log(y))[0]

    # Definiera modellen
    loga, b = c
    a = np.exp(loga)
    g = lambda t: a*np.exp(b*t)
    print(f'Linjäriserad: a={a}, b={b}')

    # Obs: Den residual som den linjära ersättningsmodellen
    # minimerar är följande:
    resnorm_lin = np.linalg.norm(A @ c - np.log(y))
    # Detta är inte samma storhet som residualen till det
    # ursprungliga systemet.
    print('Linjär ersättningsresidual:', resnorm_lin)

    return g

if __name__ == '__main__':
    main()
    plt.show()
