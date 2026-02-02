'''
Exempel - konditionstal från Frl 7 (2026-02-03)
'''

import numpy as np

A = np.array([
    [-1, 2, -0.74],
    [4, -4.98, 1],
    [0, 3, -1.95],
])
print('A =', A, sep='\n')

# 1. Experimentell uppskattning av konditionstalet genom att
# störa b = [1, 0, 0] med t.ex. 0.01 * [1, 0, -1].
b = np.array([1, 0, 0])
btilde = b + 0.01 * np.array([1, 0, -1])

x = np.linalg.solve(A, b)
xtilde = np.linalg.solve(A, btilde)

# Konditionstalet är den maximala felförstoringsfaktorn hos det
# relativa felet. Se slide 14 från Frl 7, till exempel.
relfel_x = np.linalg.norm(x - xtilde, np.inf) / np.linalg.norm(x, np.inf)
relfel_b = np.linalg.norm(b - btilde, np.inf) / np.linalg.norm(b, np.inf)
kond_est = relfel_x / relfel_b
print('kond_est =', kond_est)

# 2. Teoretisk uppskattning av cond(A) gav 19982.1778

# 3. NumPy:s inbyggda funktion
kond = np.linalg.cond(A, np.inf)
print('kond =', kond)

# Den experimentella uppskattningen ger (uppenbarligen) inte det
# värsta fallet. Som vi ser kan det finnas högerled där matrisen
# är betydligt mindre känslig för störningar. Testa om du kan
# hitta ett högerled som är mer känsligt!
print(np.linalg.eig(A))
