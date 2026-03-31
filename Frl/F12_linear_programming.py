'''
Exempel: linjärprogrammering i 2 dimensioner. Frl 12
(2026-03-31).
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# Rita ut de linjer som begränsar området.
x1 = np.linspace(-0.5, 3.5)

plt.plot(x1, (12-x1)/3, color='blue')
plt.plot(x1, -(0-x1)/3, color='red')
plt.plot(x1, -(-3+10*x1), color='green')
plt.plot(x1, -(19-8*x1), color='orange')
plt.axis([-0.5, 3.5, -0.5, 4.5])
plt.grid(True)

# Rita ut isolinjer till funktionen f=(x1, x2)
# dvs linjer vinkelräta mot grad f = (1, 1)
# dvs x2 = -x1 + C
for C in [0, 1, 2, 3, 4, 5, 6]:
    plt.plot(x1, -x1 + C, '--', color='black', linewidth=1)

# Vi kan se från figuren att minimum antas i det nedre vänstra
# hörnet, vilket enligt uträkning för hand (se tavelanteckningar)
# är (9/31, 3/31) och där f alltså har värdet 12/31.

plt.show()
