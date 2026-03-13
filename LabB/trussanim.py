'''
SF1550, Lab B, Uppgift 1, VT26

Given fil för funktionen trussanim.anim.

Exempel:
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import trussanim
>>> with np.load('eiffel1.npz') as data:
>>>     xnod = data['xnod']
>>>     ynod = data['ynod']
>>>     bars = data['bars']
>>>     A = data['A']
>>> plt.figure()
>>> v = np.zeros(A.shape[0])
>>> v[0::2] = ynod/5
>>> trussanim.anim(xnod, ynod, bars, v, color='tab:red')
>>> plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import trussplot

def anim(xnod, ynod, bars, v, *args, **kwargs):
    '''
    Animera svängningar i ett fackverk.

    Indata:
    xnod -- vektor med x-koordinater för noder
    ynod -- vektor med y-koordinater för noder
    bars -- balkmatris med två kolumner
    v -- amplituder för svängningarna (egenvektor)

    Varje rad i balkmatrisen representerar en balk mellan nod
    br[k,0] och nod br[k,1]. Av kompatibilitetsskäl startar nodindexen
    som lagras i matrisen br från 1 (inte 0).

    Extra indata skickas vidare till trussplot.plot.
    '''
    n = 10
    dt = 2*np.pi/n

    def animfun(j):
        xny = xnod + np.sin(j*dt)*v[0::2]
        yny = ynod + np.sin(j*dt)*v[1::2]
        plt.clf()
        trussplot.plot(xny, yny, bars, *args, **kwargs)
        plt.ylim([0, np.max(ynod)+0.5])
        return

    global __anim1
    __anim1 = matplotlib.animation.FuncAnimation(plt.gcf(), animfun, n,
                                                 interval=500//n)
