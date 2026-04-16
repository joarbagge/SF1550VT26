'''
SF1550, Projekt, VT26

Given fil som löser ett uppvärmningsproblem.

Exempel:
>>> import heatsolver
>>> import matplotlib.pyplot as plt
>>> sol = heatsolver.solve()
>>> plt.figure()
>>> sol.plot()
>>> plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy as sp


def solve(N=14, temp_ute=10, temp_hus=20, Q=None):
    '''
    Lös uppvärmningsproblemet för ett rum.

    Indata:
    N -- antal delintervall i y-led (avrundas så att steglängden
         går jämnt upp med alla detaljer i geometrin, kommer bli
         en multipel av 7; antalet delintervall i x-led sätts
         automatiskt från värdet)
    temp_ute -- temperatur utomhus (grader Celsius)
    temp_hus -- temperatur i resten av huset, dvs trapphus och
                andra lägenheter (grader Celsius)
    Q -- en funktion som anropas som Q(x,y) och beskriver
         tillförd värmeeffekt per volymsenhet i rummet (W/m^3)

    Utdata:
    sol -- objekt med följande egenskaper och funktioner:
        sol.x -- matris med x-koordinater av gridpunkter;
                 sol.x[i,j] är j*sol.hx
        sol.y -- matris med y-koordinater av gridpunkter;
                 sol.y[i,j] är i*sol.hy
        sol.u -- matris med temperaturvärden, sol.u[i,j]
        sol.bound -- indexmatris som väljer de punkter som är på
                     randen; sol.u[sol.bound] är alla randvärden
        sol.inner -- indexmatris som väljer de punkter som är inre
                     punkter; sol.u[sol.inner] är alla inre punkter
        sol.count -- matris som innehåller antal delrektanglar som
                     gränsar till noden med index (i,j); sol.count[i,j]
                     är ett heltal mellan 0 och 4
        sol.border -- ordningsmatris för randpunkter
        sol.hx -- steglängd i x-led
        sol.hy -- steglängd i y-led
        sol.plot() -- plottar lösningen
        sol.plot_contours() -- plottar lösningens konturlinjer
        sol.plot_boundary() -- plottar randen till beräkningsområdet
        sol.plot_grid() -- plottar gridpunkterna
        sol.plot3d() -- plottar lösningen som en yta

    Längder mäts i meter, temperaturer mäts i grader Celsius.

    Obs: index `i` varierar i y-led och index `j` varierar i x-led.
    Detta är för kompatibilitet med PyPlots plottningsfunktioner.
    '''
    # Avrunda både Nx och Ny så att det blir ett helt antal steg
    # på intervallet 0.5 (reflen); i praktiken innebär detta att
    # N kommer vara en multipel av 7.
    reflen = 0.5
    xmax = 7.5
    ymax = 3.5
    Nref = max([int(round(N/ymax * reflen)), 1])
    Ny = int(round(Nref/reflen * ymax))
    Nx = int(round(Nref/reflen * xmax))
    hx = xmax / Nx
    hy = ymax / Ny

    # Skapa en domän baserad på en rektangel med delar utskurna
    x = np.linspace(0, xmax, Nx+1)
    y = np.linspace(0, ymax, Ny+1)
    X, Y = np.meshgrid(x, y)
    # count visar hur många rektanglar varje nod gränsar till,
    # värdet är 4 för interna noder
    count = np.full(X.shape, 4)
    # Södra väggen
    count[0,1:int(2//hx)] = 2
    count[1:int(1.5//hy),int(2//hx)] = 2
    count[int(1.5//hy),int(2//hx)+1:int(4//hx)] = 2
    count[1:int(1.5//hy),int(4//hx)] = 2
    count[0,int(4//hx)+1:-1] = 2
    # Östra väggen
    count[1:-1,-1] = 2
    # Norra väggen
    count[-1,int(1//hx)+1:-1] = 2
    count[int(3//hy)+1:-1,int(1//hx)] = 2
    count[int(3//hy),1:int(1//hx)] = 2
    # Västra väggen
    count[1:int(3//hy),0] = 2
    # Hörn
    # (Obs: hörn har 1 eller 3 rektanglar beroende på om de är
    # "yttre" eller "inre" hörn)
    count[0,0] = 1
    count[0,int(2//hx)] = 1
    count[int(1.5//hy),int(2//hx)] = 3
    count[int(1.5//hy),int(4//hx)] = 3
    count[0,int(4//hx)] = 1
    count[0,-1] = 1
    count[-1,-1] = 1
    count[-1,int(1//hx)] = 1
    count[int(3//hy),int(1//hx)] = 3
    count[int(3//hy),0] = 1
    # Punkter utanför domänen
    count[0:int(1.5//hy),int(2//hx)+1:int(4//hx)] = 0
    count[int(3//hy)+1:,0:int(1//hx)] = 0
    # Ordning av randpunkter
    border = np.full(X.shape, -1)
    def put(i,j,n):
        idx = n + np.arange(np.size(i)*np.size(j))
        if np.size(idx) == 1: idx = idx[0]
        border[i,j] = idx
        return n + idx.size
    n = 0
    # Södra väggen
    n = put(0, 0, n)
    n = put(0, np.arange(1, int(2//hx)), n)
    n = put(0, int(2//hx), n)
    n = put(np.arange(1, int(1.5//hy)), int(2//hx), n)
    n = put(int(1.5//hy), int(2//hx), n)
    n = put(int(1.5//hy), np.arange(int(2//hx)+1, int(4//hx)), n)
    n = put(int(1.5//hy), int(4//hx), n)
    n = put(np.arange(int(1.5//hy)-1, 0, -1), int(4//hx), n)
    n = put(0, int(4//hx), n)
    n = put(0, np.arange(int(4//hx)+1, Nx), n)
    n = put(0, Nx, n)
    out_start = n-1
    # Östra väggen
    n = put(np.arange(1, int(1//hy)+1), Nx, n)
    window1_start = n-1
    n = put(np.arange(int(1//hy)+1, int(2.5//hy)+1), Nx, n)
    window1_end = n-1
    n = put(np.arange(int(2.5//hy)+1, Ny), Nx, n)
    n = put(Ny, Nx, n)
    # Norra väggen
    n = put(Ny, np.arange(Nx-1, int(5.5//hx)-1, -1), n)
    window2_start = n-1
    n = put(Ny, np.arange(int(5.5//hx)-1, int(4//hx)-1, -1), n)
    window2_end = n-1
    n = put(Ny, np.arange(int(4//hx)-1, int(1//hx), -1), n)
    n = put(Ny, int(1//hx), n)
    out_end = n-1
    n = put(np.arange(Ny-1, int(3//hx), -1), int(1//hx), n)
    n = put(int(3//hy), int(1//hx), n)
    n = put(int(3//hy), np.arange(int(1//hx)-1, 0, -1), n)
    n = put(int(3//hy), 0, n)
    # Västra väggen
    n = put(np.arange(int(3//hy)-1, int(2.5//hy)-1, -1), 0, n)
    door_start = n-1
    n = put(np.arange(int(2.5//hy)-1, int(1.5//hy)-1, -1), 0, n)
    door_end = n-1
    n = put(np.arange(int(1.5//hy)-1, 0, -1), 0, n)

    # Hitta inre punkter och randpunkter
    inner = (count == 4)
    bound = (count > 0) & (count < 4)

    # Lös med finita differensmetoden
    hx2 = hx**2
    hy2 = hy**2
    hdiag = np.sqrt(hx2 + hy2)
    # Ganska stort värde på värmeledningskoefficienten k,
    # för att få rimliga resultat.
    k = 4 # [W/(m K)]
    # Ickelinjär modell av värmeövergångsresistansen
    factor = 1 / (1 + np.exp(5 - temp_ute/2))
    R_outerwall = 7 + 3*factor # [m^2 K/W]
    R_innerwall = 4 # [m^2 K/W]
    R_window = 0.9 + 0.5*factor # [m^2 K/W]
    R_door = 1.35 # [m^2 K/W]
    N = (Nx+1)*(Ny+1)
    # Bygg matris och högerled
    mat = sp.sparse.dok_array((N, N))
    rhs = np.zeros(N)
    I = lambda i,j: j + i*(Nx+1)
    for i in range(Ny+1):
        for j in range(Nx+1):
            if border[i,j] >= out_start and border[i,j] <= out_end:
                u_inf = temp_ute
            else:
                u_inf = temp_hus
            if ((border[i,j] >= window1_start and border[i,j] <= window1_end) or
                (border[i,j] >= window2_start and border[i,j] <= window2_end)):
                R = R_window
            elif (border[i,j] >= door_start and border[i,j] <= door_end):
                R = R_door
            elif border[i,j] >= out_start and border[i,j] <= out_end:
                R = R_outerwall
            else:
                R = R_innerwall
            if inner[i,j]:
                mat[I(i,j), I(i,j)] = k*2*(1/hx2 + 1/hy2)
                mat[I(i,j), I(i-1,j)] = -k/hy2
                mat[I(i,j), I(i+1,j)] = -k/hy2
                mat[I(i,j), I(i,j-1)] = -k/hx2
                mat[I(i,j), I(i,j+1)] = -k/hx2
                if Q is None:
                    rhs[I(i,j)] = 0
                else:
                    rhs[I(i,j)] = Q(x[j], y[i])
            elif (i == 0 or (i == int(1.5//hy) and j > 0 and j < Nx)) and count[i,j] == 2:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hy) + 1
                mat[I(i,j), I(i+1,j)] = -4*R*k/(2*hy)
                mat[I(i,j), I(i+2,j)] = R*k/(2*hy)
                rhs[I(i,j)] = u_inf
            elif (i == Ny or (i == int(3//hy) and j < int(1//hx))) and count[i,j] == 2:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hy) + 1
                mat[I(i,j), I(i-1,j)] = -4*R*k/(2*hy)
                mat[I(i,j), I(i-2,j)] = R*k/(2*hy)
                rhs[I(i,j)] = u_inf
            elif (j == 0 or (j == int(1//hx) and i > int(3//hy)) or
                  (j == int(4//hx) and i < int(1.5//hy))) and count[i,j] == 2:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hx) + 1
                mat[I(i,j), I(i,j+1)] = -4*R*k/(2*hx)
                mat[I(i,j), I(i,j+2)] = R*k/(2*hx)
                rhs[I(i,j)] = u_inf
            elif (j == Nx or (j == int(2//hx) and i < int(1.5//hy))) and count[i,j] == 2:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hx) + 1
                mat[I(i,j), I(i,j-1)] = -4*R*k/(2*hx)
                mat[I(i,j), I(i,j-2)] = R*k/(2*hx)
                rhs[I(i,j)] = u_inf
            elif (i,j) in {(0,0), (int(1.5//hy),int(4//hx)), (0,int(4//hx))}:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hdiag) + 1
                mat[I(i,j), I(i+1,j+1)] = -4*R*k/(2*hdiag)
                mat[I(i,j), I(i+2,j+2)] = R*k/(2*hdiag)
                rhs[I(i,j)] = u_inf
            elif (i,j) in {(0,Nx), (0,int(2//hx)), (int(1.5//hy),int(2//hx))}:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hdiag) + 1
                mat[I(i,j), I(i+1,j-1)] = -4*R*k/(2*hdiag)
                mat[I(i,j), I(i+2,j-2)] = R*k/(2*hdiag)
                rhs[I(i,j)] = u_inf
            elif (i,j) in {(int(3//hy),0), (int(3//hy),int(1//hx)), (Ny,int(1//hx))}:
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hdiag) + 1
                mat[I(i,j), I(i-1,j+1)] = -4*R*k/(2*hdiag)
                mat[I(i,j), I(i-2,j+2)] = R*k/(2*hdiag)
                rhs[I(i,j)] = u_inf
            elif (i,j) == (Ny,Nx):
                mat[I(i,j), I(i,j)] = 3*R*k/(2*hdiag) + 1
                mat[I(i,j), I(i-1,j-1)] = -4*R*k/(2*hdiag)
                mat[I(i,j), I(i-2,j-2)] = R*k/(2*hdiag)
                rhs[I(i,j)] = u_inf
            else:
                mat[I(i,j), I(i,j)] = 1
                rhs[I(i,j)] = np.nan
    mat = sp.sparse.csc_array(mat)

    # Lös för temperaturen
    u = sp.sparse.linalg.spsolve(mat, rhs)
    U = u.reshape(X.shape)

    idxs = {
        'out': [out_start, out_end],
        'window1': [window1_start, window1_end],
        'window2': [window2_start, window2_end],
        'door': [door_start, door_end],
    }

    # Paketera resultatet och returnera
    sol = HeatSolution(X, Y, hx, hy, bound, inner, count, border, U, idxs)
    return sol


class HeatSolution:
    '''
    Objekt med information om lösningen. Se dokumentationen till
    funktionen ``solve()`` ovan för en översikt av egenskaper och
    funktioner. (Detta objekt är utdata från ``solve()``.
    '''

    def __init__(self, x, y, hx, hy, bound, inner, count, border, u, idxs):
        self.x = x
        self.y = y
        self.hx = hx
        self.hy = hy
        self.bound = bound
        self.inner = inner
        self.count = count
        self.border = border
        self.u = u
        self._idxs = idxs
        return

    def plot(self, *args, **kwargs):
        if 'shading' not in kwargs:
            kwargs['shading'] = 'gouraud'
        plt.pcolormesh(self.x, self.y, self.u, *args, **kwargs)
        self.plot_boundary()
        return

    def plot_contours(self, *args, **kwargs):
        cs = plt.contour(self.x, self.y, self.u, *args, **kwargs)
        plt.clabel(cs)
        self.plot_boundary()
        return

    def plot_boundary(self, *args, **kwargs):
        x = self.x[self.bound]
        y = self.y[self.bound]
        t = self.border[self.bound]
        idx = np.argsort(t)
        x = x[idx]
        y = y[idx]
        x = np.concatenate((x, [x[0]]))
        y = np.concatenate((y, [y[0]]))
        if 'color' not in kwargs:
            kwargs['color'] = 'black'
        if 'linewidth' not in kwargs:
            kwargs['linewidth'] = 1
        plt.plot(x, y, *args, **kwargs)

        # Plot windows
        for win in ('window1', 'window2'):
            I = (self.border == self._idxs[win][0]) | (self.border == self._idxs[win][1])
            x = self.x[I]
            y = self.y[I]
            plt.plot(x, y, color='red', linewidth=2)

        # Plot door
        I = (self.border == self._idxs['door'][0]) | (self.border == self._idxs['door'][1])
        x = self.x[I]
        y = self.y[I]
        plt.plot(x, y, color='orange', linewidth=2)

        plt.axis('equal')
        return

    def plot_grid(self, *args, **kwargs):
        plt.plot(self.x[self.inner], self.y[self.inner], 'x', color='black')
        plt.plot(self.x[self.bound], self.y[self.bound], 'o', color='tab:red',
                 markerfacecolor='none')
        plt.axis('equal')
        return

    def plot3d(self, *args, **kwargs):
        ax = plt.subplot(projection='3d')
        if 'cmap' not in kwargs:
            kwargs['cmap'] = cm.viridis
        ax.plot_surface(self.x, self.y, self.u, *args, **kwargs)
        plt.axis('equal')
        return
