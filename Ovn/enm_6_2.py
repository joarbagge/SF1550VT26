import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# (a)
f = lambda x: np.exp(x) / (1 + 2*x**3)
a = 0
b = 3

# Plotta integranden för att se hur den ser ut
n = 30
x = np.linspace(a, b, n+1)
fx = f(x)
plt.figure(1)
plt.plot(x, fx)
plt.title('(a)')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

# Trapetsregeln med 30 delintervall, halvera sedan successivt
# (integranden beräknades ovan)
h = (b-a)/n
Tlist = []
T = h * (np.sum(fx) - 0.5*fx[0] - 0.5*fx[-1])
Tlist.append(T)
# Prova halvera steglängden tre gånger
for steghalvering in range(3):
    n *= 2
    x = np.linspace(a, b, n+1)
    fx = f(x)
    h = (b-a)/n
    T = h * (np.sum(fx) - 0.5*fx[0] - 0.5*fx[-1])
    Tlist.append(T)

print('(a)')
Tlist = np.array(Tlist)
print('Trapetsvärden:', Tlist)
# Uppskatta felet med skillnaden
Tdiff = np.abs(np.diff(Tlist))
print('Skillnader:', Tdiff)
# Se om kvoterna är nära 4
Tkvot = Tdiff[:-1] / Tdiff[1:]
print('Kvoter:', Tkvot)

Iref = sp.integrate.quad(f, a, b, epsrel=0.5e-5)[0]
print('Iref =', Iref)

# (b)
f = lambda x: np.sin(x) / x
a = 0
b = np.pi

# Plotta integranden
n = 30
x = np.linspace(a, b, n+1)
fx = f(x)
plt.figure(2)
plt.plot(x, fx)
plt.title('(b)')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

# Trapetsregeln med fyra delintervall
n = 4
Tlist = []
for k in range(3):
    x = np.linspace(a, b, n+1)
    fx = f(x)
    fx[0] = 1 # gränsvärde
    h = (b-a)/n
    T = h * (np.sum(fx) - 0.5*fx[0] - 0.5*fx[-1])
    Tlist.append(T)
    n *= 2

print('\n(b)')
Tlist = np.array(Tlist)
print('Trapetsvärden:', Tlist)
# Uppskatta felet med skillnaden
Tdiff = np.abs(np.diff(Tlist))
print('Skillnader:', Tdiff)
# Se om kvoterna är nära 4
Tkvot = Tdiff[:-1] / Tdiff[1:]
print('Kvoter:', Tkvot)

if __name__ == '__main__':
    plt.show()
