import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

av = np.array([0.8, 1.6, 2.4, 3.2])

# Newtons metod för system för att hitta maxpunkten
for i, a in enumerate(av):
    print(f'a={a}')
    if i == 0:
        x = np.array([0., 1]) # startgissning för första a-värdet
    delta = np.inf
    while np.max(np.abs(delta)) > 0.5e-4:
        sxy = np.sin(x[0]*x[1])
        cxy = np.cos(x[0]*x[1])
        f = np.array([2*x[0] - a*x[1]*cxy,
                      x[0]**2 + x[1]**2 - 1 - a*sxy])
        J = np.array([[2 + a*x[1]**2*sxy, -a*cxy + a*x[0]*x[1]*sxy],
                      [2*x[0] - a*x[1]*cxy, 2*x[1] - a*x[0]*cxy]])
        delta = -np.linalg.solve(J, f)
        x += delta
    print('(x,y) =', np.round(x, 4))

# Metod för att rita upp kurvorna (polära koordinater + Newton)
n = 100
Fi = np.linspace(0, 2*np.pi, n+1)
colors = ['orange', 'red', 'green', 'blue']
for i, a in enumerate(av):
    R = np.zeros(Fi.size)
    # Första vinkelvärdet (fi=0) ger r=1
    fi = 0
    r = 1
    R[0] = r
    # Använd en loop för övriga vinkelvärden
    for j, fi in enumerate(Fi[1:], start=1):
        h = np.inf
        # Bestäm r(fi) med Newtons metod
        while np.abs(h) > 1e-10:
            f = r**2 - 1 - a*np.sin(0.5*r**2*np.sin(2*fi))
            fprim = 2*r - a*np.cos(0.5*r**2*np.sin(2*fi)) * r*np.sin(2*fi)
            h = -f/fprim
            r += h
        R[j] = r
    # Plotta kurvan
    x = R*np.cos(Fi)
    y = R*np.sin(Fi)
    plt.plot(x, y, color=colors[i], linewidth=1)
plt.axis('equal')

if __name__ == '__main__':
    plt.show()
