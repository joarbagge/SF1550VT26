'''
Exempel från Föreläsning 5 (2026-01-29)
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Definiera funktionen
    F = lambda x,y: np.array([
        np.tan(x) - np.cos(y/2),
        np.tan(y) + np.sin(x/2)
    ])
    # Ett annat sätt att representera F:
    f1 = lambda x,y: np.tan(x) - np.cos(y/2)
    f2 = lambda x,y: np.tan(y) + np.sin(x/2)
    F = lambda x,y: np.array([f1(x,y), f2(x,y)])
    # Definiera funktionens Jacobimatris (alla partiella derivator)
    J = lambda x,y: np.array([
        [1/np.cos(x)**2,   0.5*np.sin(y/2)],
        [0.5*np.cos(x/2),  1/np.cos(y)**2],
    ])

    # Bestäm startgissning med hjälp av konturlinjer
    x = np.linspace(-5, 5)
    y = x
    X, Y = np.meshgrid(x, y)
    Z1 = f1(X,Y)
    Z2 = f2(X,Y)
    plt.figure(1)
    plt.clf()
    plt.contour(X, Y, Z1, cmap='jet', levels=[-1, 0, 1])
    plt.contour(X, Y, Z2, cmap='jet', levels=[-1, 0, 1])
    plt.colorbar()
    plt.title('Nivåkurvor för $f_1$ och $f_2$')
    # Plotten visar att ett nollställe finns i närheten av (-2.5, 0.8)

    # Startgissning, xv = [x, y]
    xv = np.array([-2.5, 0.8])

    # Newtons metod
    tol = 1e-12 # feltolerans
    delta = np.inf # stort tal för att komma in i slingan
    i = 0
    maxiter = 100
    while np.linalg.norm(delta) > tol and i < maxiter:
        x, y = xv
        delta = -np.linalg.solve(J(x,y), F(x,y))
        # OBS: x = np.linalg.solve(A, b)
        # löser det linjära ekvationssystemet A @ x = b
        xv += delta
        i += 1
        print(i, xv, np.linalg.norm(delta))
        # Kolla att antalet nollor i delta dubbleras varje iteration

    x, y = xv
    plt.plot(x, y, 'k*')
    return


if __name__ == '__main__':
    main()
    plt.show()
