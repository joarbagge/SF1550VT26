import numpy as np

A = np.zeros((3, 4)) # Skapa matris med nollor
a = A[1,2] # Plocka ut enskilt element
B = A[1:,0] # Plocka ut delmatris
d = np.diag(A) # Plocka ut diagonalen
v = A[(0,1,2),(0,2,1)] # Plocka ut några element
At = A.T # Transponat
C = A.reshape((2, 6)) # Omforma matrisen
r = A.ravel() # Platta ut matrisen
print(A, a, B, d, v, At, C, r, sep='\n\n')

A[:] = np.arange(1, 13).reshape(A.shape) # Skriv talen 1, 2, ..., 12 till A
print('====')
print(A, a, B, d, v, At, C, r, sep='\n\n')

print('****')

A = np.zeros((3, 4)) # Skapa matris med nollor
At = A.T.copy()
A[:] = np.arange(1, 13).reshape(A.shape) # Skriv talen 1, 2, ..., 12 till A
print(A, At, sep='\n\n')
