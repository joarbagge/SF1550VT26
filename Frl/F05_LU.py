'''
Exempel från Föreläsning 5 (2026-01-29) och 6 (2026-02-02)
'''

import numpy as np
import scipy as sp

def main():
    np.set_printoptions(precision=16) # visa alla decimaler

    # Tre sätt att lösa ett linjärt ekvationssystem på
    A = np.array([[2, 2, 4],
                  [4, 3.99, 6],
                  [6, 12, 9]])
    b = np.array([6, 9, 3])

    # Standardmetod
    x1 = np.linalg.solve(A, b)
    print('x1 =', x1)

    # Att räkna ut inversen explicit som nedan är ofta onödigt,
    # och leder till fler beräkningar. Ibland blir även felet
    # större. (I detta fall fungerar det okej.)
    x2 = np.linalg.inv(A) @ b
    print('x2 =', x2)

    # LU-faktorisering med partiell pivotering
    Pt, L, U = sp.linalg.lu(A)
    # Utdata uppfyller: A = Pt @ L @ U

    # Det linjära ekvationssystemet
    #
    # A @ x = b
    #
    # blir alltså till Pt @ L @ U @ x = b,
    # vilket vi kan skriva om som:
    #
    # L @ (U @ x) = Pt.T @ b
    #
    # (Här betyder Pt.T transponatet av Pt, för
    # permutationsmatriser är inversen lika med transponatet.)
    #
    # Inför variabeln y = U @ x
    # så kan ovanstående skrivas som:
    #
    # L @ y = Pt.T @ b

    # Lös med hjälp av LU-faktoriseringen
    P = Pt.T
    y = sp.linalg.solve_triangular(L, P @ b, lower=True)
    x3 = sp.linalg.solve_triangular(U, y)
    print('x3 =', x3)

    # I detta fall borde alla tre metoder ge (nästan) exakt samma svar.
    return


if __name__ == '__main__':
    main()
