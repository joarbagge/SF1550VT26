import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Funktion för trapetsregeln tillämpad på problemet
def trapz(x, n):
    h = x/n
    t = np.linspace(0, x, n+1)
    f = np.sin(3*t**2) / (t+1)
    val = (h/2) * (f[0] + 2*np.sum(f[1:-1]) + f[-1])
    return val

# Funktion för att beräkna energin med 1400 delintervall för att
# komma under felgränsen
def energy(x):
    return trapz(x, 1400)

# Generera startgissningar
plt.figure()
t = np.linspace(1, 3)
fvec = np.zeros(t.shape)
for i in range(t.size):
    fvec[i] = energy(t[i]) - 0.3
plt.plot(t, fvec)

# Sekantmetoden
x0 = 1.0
x1 = 1.5
tol = 1e-3

fx0 = energy(x0) - 0.3
itr = 0
while np.abs(x0-x1) > tol:
    itr += 1
    fx1 = energy(x1) - 0.3
    x_new = x1 - fx1*(x1 - x0)/(fx1 - fx0)
    x0 = x1
    x1 = x_new
    fx0 = fx1

root = x_new
print(root)

# I deluppgift c) byter vi ut funktionen energy() mot energy_c()
# som förfinar adaptivt:
def energy_c(x):
    # Trapetsregel med n=10
    E1 = trapz(x, 10)
    # Trapetsregel med n=20
    n = 20
    E2 = trapz(x, n)
    # Förfina adaptivt (vi väljer en något mer strikt tolerans än
    # vad som krävs för sekantmetoden så att inte felet från
    # trapetsregeln dominerar)
    while np.abs(E1-E2) > 1e-4:
        E1 = E2
        n *= 2
        E2 = trapz(x, n)
    return E2

if __name__ == '__main__':
    plt.show()
