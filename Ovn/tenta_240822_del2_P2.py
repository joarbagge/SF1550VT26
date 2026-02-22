import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Testkod för att kunna köra programmet (antas givet i tentauppgiften)
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
y = np.array([1.19, 0.63, 0.48, 0.38, 0.33, 0.28, 0.27])
N = x.size
X0 = np.array([1, 0.3, 2])

# Antar att vektorerna x och y innehåller datapunkterna, samt att
# X0 innehåller en bra startgissning för C=np.array([a,b,c]).

# Definierar funktion och Jacobimatris
g = lambda c: (c[0] + c[1]*x) / (1 + c[2]*x) - y
J = lambda c: np.column_stack((
    1 / (1 + c[2]*x), # dg/da
    x / (1 + c[2]*x), # dg/db
    -x * (c[0] + c[1]*x) / (1 + c[2]*x)**2, # dg/dc
))

c = X0 # startgissning
d = [1] # dummy
tol = 1e-10 # tolerans
while np.linalg.norm(d, np.inf) > tol:
    d = -np.linalg.lstsq(J(c), g(c))[0]
    c += d

print(c) # koefficienterna a, b, c

# Linjär version av MKM-anpassningen

A = np.column_stack((np.ones(x.shape), x, -x*y))
c2 = np.linalg.lstsq(A, y)[0]
print(c2) # koefficienterna a, b, c

if __name__ == '__main__':
    plt.show()
