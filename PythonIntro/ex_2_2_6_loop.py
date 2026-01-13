'''
Jämför NumPys array-funktion med att anropa samma funktion på
varje element individuellt.
'''

import time
import numpy as np

N = 100000 # antal element
x = np.linspace(0, 1, N)

tic = time.time()
y1 = np.sin(x)
time1 = time.time() - tic
print(f'Array-funktion tog {time1} s.')

y2 = np.zeros(x.shape)
tic = time.time()
for i in range(x.size):
    y2[i] = np.sin(x[i])
time2 = time.time() - tic
print(f'Loop tog {time2} s.')

err = np.linalg.norm(y1 - y2)
print(f'Skillnad på funktionsvärden: {err}')
