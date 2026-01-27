import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Plotta kurvor för lösningsförslaget
plt.subplot(2,1,1)
x = np.linspace(0, 25, 1000)
plt.plot(x, np.tan(x), linewidth=1)
plt.plot(x, x, '--', linewidth=1)
plt.title(r'Kurvorna $y=\tan(x)$ och $y=x$')
plt.xlim([0, 25])
plt.ylim([-10, 25])
plt.subplot(2,1,2)
x = np.linspace(0, 25, 200)
plt.plot(x, np.sin(x)-x*np.cos(x), linewidth=1)
plt.plot(x, 0*x, '--', linewidth=1, color='gray')
plt.title(r'Kurvan $y=\sin(x) - x \, \cos(x)$')
plt.xlim([0, 25])
plt.ylim([-40, 40])
plt.tight_layout()

# Newtons metod
xstart = 3*np.pi/2 - 0.1 # startgissning till rot nr 1
for nr in range(6):
    print()
    print('i  x                  dx')
    x = xstart
    dx = np.inf # stort tal för att komma in i slingan
    i = 0
    # Här cirka 12 siffrors noggrannhet
    while np.abs(dx/x) > 1e-12 and i < 8:
        f = np.sin(x) - x*np.cos(x)
        fprim = x*np.sin(x)
        dx = -f/fprim
        print(i, x, dx)
        x += dx
        i += 1
    xstart += np.pi # startgissning till nästa rot

if __name__ == '__main__':
    plt.show()
