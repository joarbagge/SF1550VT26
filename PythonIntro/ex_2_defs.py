import numpy as np

x1 = np.linspace(0, 1, 11)
x2 = np.arange(0, 1+0.1, 0.1)

A = np.zeros((3, 3))
B = np.ones((3, 4))

x3 = np.ones(4) # 4 betyder samma sak som (4,) i detta fall

x4 = np.array([1., 2., 3., 4.])
C = np.array([[0, 1], [0.5, 0.5], [1, 0]])

D = np.ones(C.shape)
x5 = np.array([0., 1., 2.])

E = np.array([[1., 1., 2.], [0., 1., 1.]]) # Ny (2, 3)-matris
F = E @ C # Resultatet blir en (2, 2)-matris
x6 = B @ x4 # Resultatet blir en (3,)-vektor

b = np.array([1., 2.])
x7 = np.linalg.solve(F, b)

resnorm = np.linalg.norm(F @ x7 - b)

I = (x1 > 0.5) # Ger en vektor med boolska värden (True/False)
x1[I] = 0.25 # Element kan skrivas över

g = np.arange(9)
G = g.reshape((3, 3))

c = C.reshape(-1)

v = np.arange(5).reshape(1,-1)
H = v * v.T

x = np.array([1, 2, 3])
y = np.array([1., 2., 3.])

y /= 2

f = np.finfo(float)
