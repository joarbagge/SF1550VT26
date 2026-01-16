import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Beräkning med ostörda värden
a = 2000; d = 300; theta = 20*np.pi/180; t = 10
x = np.sqrt(a**2 + (a-d)**2 - 2*a*(a-d)*np.cos(theta))
print('x =', x)
v = x/t * 3.6
print('v =', v)
print()

# Alternativ 1: Test av kombinationer
a0 = 2000; d0 = 300; theta0 = 20
x0 = np.sqrt(a0**2 + (a0-d0)**2 - 2*a0*(a0-d0)*np.cos(theta0*np.pi/180))
X = [x0]
print(a0, d0, theta0, int(np.round(x0)))
for a in (a0-100, a0+100):
    for d in (d0-20, d0+20):
        for theta in (theta0-1, theta0+1):
            x = np.sqrt(a**2 + (a-d)**2 - 2*a*(a-d)*np.cos(theta*np.pi/180))
            X.append(x)
            print(a, d, theta, int(np.round(x)))
v0 = 3.6*x0/10
print('v0 =', v0)
print('vmin =', 3.6*min(X)/10.1)
print('vmax =', 3.6*max(X)/9.9)

vmin = 3.6*min(X)/10.1
vmax = 3.6*max(X)/9.9
print('Ev =', max([np.abs(vmin - v0), np.abs(vmax - v0)]))
print()

# Alternativ 2: Experimentell störningsräkning
def fufo(a,d,theta,t):
    x = np.sqrt(a**2 + (a-d)**2 - 2*a*(a-d)*np.cos(theta))
    v = x/t * 3.6
    return v
a = 2000; d = 300; theta = 20*np.pi/180; t = 10
v0 = fufo(a,d,theta,t)
erra = np.abs(fufo(a+100,d,theta,t) - v0)
errd = np.abs(fufo(a,d+20,theta,t) - v0)
errtheta = np.abs(fufo(a,d,theta+1*np.pi/180,t) - v0)
errt = np.abs(fufo(a,d,theta,t+0.1) - v0)
errtot = erra + errd + errtheta + errt
print('errtot =', errtot)
print()

# Alternativ 3: Felfortplantningsformeln
dzda = 2*a + 2*(a-d) - 2*(2*a-d)*np.cos(theta)
print('dzda =', dzda)
dzdd = -2*(a-d) + 2*a*np.cos(theta)
print('dzdd =', dzdd)
dzdtheta = 2*a*(a-d)*np.sin(theta)
print('dzdtheta =', dzdtheta)
Ez = np.abs(dzda)*100 + np.abs(dzdd)*20 + np.abs(dzdtheta)*1*np.pi/180
print('Ez =', Ez)
x = np.sqrt(a**2 + (a-d)**2 - 2*a*(a-d)*np.cos(theta))
Ex = Ez / (2*x)
print('Ex =', Ex)
Rv = Ex/x + 0.1/t
print('Rv =', Rv)
Ev = Rv*v0
print('Ev =', Ev)

if __name__ == '__main__':
    plt.show()
