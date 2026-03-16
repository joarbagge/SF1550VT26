'''
SF1550, Lab B, Uppgift 2, VT26
'''

# Skelettfil. Fyll i kod på platser märkta TODO och ta bort denna kommentar.

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def main():
    '''
    Uppgift 2 - interpolation
    '''
    # TODO: skriv kod här ...


def kastbana(h):
    '''
    Beräknar banan för ett kast med en liten boll.

    Bollens position (x,y) och hastighet (vx,vy) beräknas vid
    diskreta tidpunkter mellan t=0 och t=5 med steglängd h.

    Indata:
    h -- steglängd mellan tidpunkterna

    Utdata:
    t -- vektor med tidpunkter [s]
    x, y -- vektorer med bollens x- och y-koordinater vid tidpunkerna [m]
    vx, vy -- vektorer med bollens hastigheter i x- och y-led vid
              tidpunkterna [m/s]

    Exempel:
    >>> t, x, y, vx, vy = kastbana(0.25)

    Bollen kastas från (x,y)=(0,2) med hastigheten 31 m/s i
    40 graders vinkel mot horisontalplanet. Banan beskrivs av en
    ordinär differentialekvation

        r'' = -g*ey - sigma*r'*|r'|/m,      r=(x,y),

    som inkluderar effekten av luftmotståndet.
    '''
    ## Tennisboll, specifikationer
    m = 58e-3 # massa [kg] = 58 gram
    ra = 6.5e-2/2 # radie [m] -- 6.5 cm i diameter

    g = 9.82 # tyngdaccelerationen [m/s^2]
    rho = 1.2 # luftens densitet [kg/m^3]
    A = np.pi * ra**2 # bollens tvärsnittsarea [m^2]
    Cd = 0.47 # luftmotståndskoefficient ("drag coefficient")
    # Luftmotståndskoefficienten är dimensionslös.
    # Läs mer på http://en.wikipedia.org/wiki/Drag_coefficient

    sigma = rho * A * Cd/2 # totala luftmotståndet [kg/m]

    T = 5 # sluttid [s]
    v0 = 31 # utkasthastighet [m/s]
    al = 40*np.pi/180 # utkastvinkel [rad]

    # Begynnelsevärden
    R0 = np.array([0.0, 2.0]) # position
    V0 = np.array([v0*np.cos(al), v0*np.sin(al)]) # hastighet
    U0 = np.concatenate((R0, V0))

    # ODE:ns högerled
    # u = (x, y, vx, vy)
    # u[:2] = (x, y)
    # u[2:] = (vx, vy)
    # f(u) = du/dt
    ey = np.array([0, 1]) # enhetsvektor i y-led
    f = lambda u: np.concatenate((
        u[2:],
        -g*ey - sigma*u[2:]*np.linalg.norm(u[2:])/m
    ))

    N = int(np.round(T/h))
    t = np.linspace(0, T, N+1)
    U = np.zeros((N+1, U0.size))
    U[0,:] = U0

    # Runge-Kutta 4
    for i in range(N):
        u = U[i,:]
        s1 = f(u)
        s2 = f(u + h/2*s1)
        s3 = f(u + h/2*s2)
        s4 = f(u + h*s3)
        U[i+1,:] = u + h/6*(s1 + 2*s2 + 2*s3 + s4)

    x = U[:,0]
    y = U[:,1]
    vx = U[:,2]
    vy = U[:,3]
    return t, x, y, vx, vy


if __name__ == '__main__':
    main()
    plt.show()
