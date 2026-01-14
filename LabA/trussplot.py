'''
SF1550, Lab A, Uppgift 3, VT26

Given fil för funktionen trussplot.plot.

Exempel:
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import trussplot
>>> with np.load('eiffel1.npz') as data:
>>>     xnod = data['xnod']
>>>     ynod = data['ynod']
>>>     bars = data['bars']
>>>     A = data['A']
>>> plt.figure()
>>> trussplot.plot(xnod, ynod, bars, color='tab:red')
>>> plt.show()
'''

import matplotlib.pyplot as plt

def plot(x, y, br, *args, **kwargs):
    '''
    Plotta ett fackverk.

    Indata:
    x -- vektor med x-koordinater för noder
    y -- vektor med y-koordinater för noder
    br -- balkmatris med två kolumner

    Varje rad i balkmatrisen representerar en balk mellan nod
    br[k,0] och nod br[k,1]. Av kompatibilitetsskäl startar nodindexen
    som lagras i matrisen br från 1 (inte 0).

    Extra indata skickas vidare till plt.plot.
    '''
    if 'color' not in kwargs:
        kwargs['color'] = 'black'

    for k in range(br.shape[0]):
        i = br[k,:] - 1
        plt.plot(x[i], y[i], *args, **kwargs)

    plt.axis('equal')
