'''
Exempel från Föreläsning 2 (2026-01-20)
'''

import numpy as np

# Bästa gissningar
Pt = 8
Rt = 2
# Felgränser
EP = 0.1
ER = 0.025

# Funktion
I = lambda P,R: np.sqrt(P/R)

# Bästa gissning på I
It = I(Pt, Rt)
print('It=', It)

# Experimentell störningsanalys för EI:
IexpP = I(Pt+EP, Rt)
IexpR = I(Pt, Rt+ER)
DP = abs(IexpP - It)
DR = abs(IexpR - It)
print('DP=', DP)
print('DR=', DR)
EI = DP + DR
print('EI=', EI, '<- svar')
