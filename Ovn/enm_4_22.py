import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Datapunkter
fi = np.arange(12) * np.pi/6
r = np.array([3.3, 3.5, 2.7, 2.0, 1.4, 1.0, 0.7, 0.5, 0.4, 0.5, 0.9, 1.9])
fig = plt.figure(1)
ax = fig.add_subplot(projection='polar') # polär plot
ax.plot(fi, r, 'k*')

# a) Minstakvadratlösning till linjäriserade problemet
print('== a) Linjäriserad modell ==')
y = r
A = np.column_stack((np.ones(fi.shape), np.sin(fi), -r*np.cos(fi)))
x = np.linalg.lstsq(A, y)[0] # funktionen returnerar flera saker,
                             # [0] är lösningen (x)
print('x =', x)

# Rita ut modellen
a, b, c = x
R_lin = lambda fi: (a + b*np.sin(fi)) / (1 + c*np.cos(fi))
fif = np.linspace(0, 2*np.pi, 200)
ax.plot(fif, R_lin(fif), label='Linjäriserad')

# b) Gauss-Newton på den icke-linjära modellen
print('\n== a) Gauss-Newton ==')
# x[0] = a, x[1] = b, x[2] = c
F = lambda x: (x[0] + x[1]*np.sin(fi)) / (1 + x[2]*np.cos(fi)) - r
J = lambda x: np.column_stack((
    1 / (1 + x[2]*np.cos(fi)), # dF/da
    np.sin(fi) / (1 + x[2]*np.cos(fi)), # dF/db
    -(x[0] + x[1]*np.sin(fi)) / (1 + x[2]*np.cos(fi))**2 * np.cos(fi), # dF/dc
))
X = x # startgissning från linjäriserade problemet
tol = 1e-10
diff = np.full(X.shape, np.inf)
i = 0
print(i, X)
while np.linalg.norm(diff) > tol:
    diff = -np.linalg.lstsq(J(X), F(X))[0]
    X += diff
    i += 1
    print(i, X, diff)

# Rita ut modellen
a2, b2, c2 = X
R_gn = lambda fi: (a2 + b2*np.sin(fi)) / (1 + c2*np.cos(fi))
ax.plot(fif, R_gn(fif), '--', label='Gauss-Newton')
plt.legend()

if __name__ == '__main__':
    plt.show()
