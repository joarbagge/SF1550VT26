'''
Enkel tidtagning av matrix-vektor-multiplikation. Frl 6 (2026-02-02).
'''

import numpy as np
import time

n = 1000

A = np.random.randn(n, n)
x = np.random.randn(n)

tic = time.time()
b = A @ x
toc = time.time() - tic
print(f'Det tog {toc} s.')

# När man dubblerar n borde tiden öka med en faktor
# fyra! Testa att det stämmer.
