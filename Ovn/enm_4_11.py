import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Datapunkter
v = np.array([2, 5, 8, 11, 14])
Thud = np.array([0, -7.5, -12, -14.5, -16.5])
plt.plot(v, Thud, 'k*')
plt.xlabel('Vindstyrka $v$ (m/s)')
plt.ylabel('Upplevd temperatur $T_\\text{hud}$ (°C)')
plt.grid(True)

# Sätt upp överbestämt system och lös med minstakvadratmetoden
y = (33 - Thud)/(33 - 0)
A = np.column_stack((np.ones(v.shape), v, np.sqrt(v)))
x = np.linalg.lstsq(A, y)[0] # funktionen returnerar flera saker,
                             # [0] är lösningen (x)
print('x =', x)

# Beräkna residualen
res = y - A @ x
print('res =', res)

# Formulera modellen
a, b, c = x
Thud = lambda v,T: 33 - (a + b*v + c*np.sqrt(v))*(33-T)

# Besvara frågan i uppgiften
Tu = Thud(v=7, T=-5)
print('Tu =', Tu)
plt.plot(7, Tu, 'ro', markerfacecolor='none')

# Rita ut några linjer
v = np.linspace(2, 14)
for T in range(-15, 20+1, 5):
    plt.plot(v, Thud(v, T))
    plt.text(12, Thud(12, T)+1, f'$T={T}$')

if __name__ == '__main__':
    plt.show()
