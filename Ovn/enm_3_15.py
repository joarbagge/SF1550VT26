import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Rita polynomkurvan
P = lambda x: x**3 - 6*x**2 + 11*x - 6
Pprim = lambda x: 3*x**2 - 12*x + 11 # behövs senare
x = np.linspace(0.5, 3.5, 200)
plt.plot(x, P(x), color='black', linewidth=1)

# Definiera en funktion för att hantera ett cirkelfall
def fall(R, rikt, a0, b0, color='white'):
    '''
    Indata:
    R -- cirkelns radie
    rikt -- 1 för ovanpå, -1 för under
    (a0, b0) -- startgissningar
    color -- färg för plottning av cirkel
    '''
    # Hjälpfunktioner för p(x) och n(x)
    p = lambda x: np.array([x, P(x)])
    n = lambda x: rikt*np.array([-Pprim(x), 1]) / np.sqrt(1 + Pprim(x)**2)
    # Funktion för själva ekvationen som ska lösas
    f = lambda a,b: p(a) - p(b) + R*(n(a) - n(b))
    # Newtons metod för system
    delta = np.inf
    i = 0
    x = np.array([a0, b0])
    h = 0.01 # steglängd för derivataapproximation
    while np.max(np.abs(delta)) > 0.5e-4 and i < 10:
        fval = f(x[0], x[1])
        # Approximera derivatorna (modifierade Newton)
        dfda = (f(x[0]+h, x[1]) - fval) / h
        dfdb = (f(x[0], x[1]+h) - fval) / h
        Jval = np.column_stack((dfda, dfdb))
        delta = -np.linalg.solve(Jval, fval)
        x += delta
        i += 1
    # Skriv ut lösningen
    print(f'R={R}: (a,b) = {x} efter {i} iterationer')
    # Rita cirkel och tangeringspunkter
    a, b = x
    p1 = p(a)
    p2 = p(b)
    n1 = n(a)
    c = p1 + R*n1 # cirkelns mittpunkt
    t = np.linspace(0, 2*np.pi, 100)
    xx = c[0] + R*np.cos(t)
    yy = c[1] + R*np.sin(t)
    plt.fill(xx, yy, color=color, edgecolor='black')
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k*')
    return

# Använd funktionen för att hantera tre fall
fall(R=0.8, rikt=1, a0=2.6-0.8, b0=2.6+0.8, color='yellow')
fall(R=0.5, rikt=1, a0=2.6-0.5, b0=2.6+0.5, color='magenta')
fall(R=0.6, rikt=-1, a0=1.4-0.6, b0=1.4+0.6, color='lightgreen')
plt.axis('equal')
plt.title('Tre cirklar i en polynomkurva')

if __name__ == '__main__':
    plt.show()
