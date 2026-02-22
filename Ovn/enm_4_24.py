import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Datapunkter
fi = np.array([0, 90, 180, 270]) * np.pi/180 # radianer
r = np.array([58, 40, 22, 28])
fig = plt.figure(1)
ax = fig.add_subplot(projection='polar') # polär plot
ax.plot(fi, r, 'k*')

# Gauss-Newton
# x[0] = R, x[1] = E, x[2] = fi0
F = lambda x: x[0]/(1 - x[1]*np.cos(fi-x[2])) - r
J = lambda x: np.column_stack((
    1/(1 - x[1]*np.cos(fi-x[2])), # dF/dR
    -x[0]/(1 - x[1]*np.cos(fi-x[2]))**2 * (-np.cos(fi-x[2])), # dF/dE
    -x[0]/(1 - x[1]*np.cos(fi-x[2]))**2 * (-x[1]*np.sin(fi-x[2])), # dF/dfi0
))
X = np.array([30, 0.3, 45*np.pi/180]) # startgissningar
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
R, E, fi0 = X
r_gn = lambda fi: R / (1 - E*np.cos(fi - fi0))
fif = np.linspace(0, 2*np.pi, 200)
ax.plot(fif, r_gn(fif))

if __name__ == '__main__':
    plt.show()
