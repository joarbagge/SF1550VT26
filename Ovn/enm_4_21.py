import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Datapunkter
T = np.arange(700, 1400+1, 100)
k = np.array([4.61, 5.59, 6.50, 7.34, 8.12, 8.83, 9.49, 10.10])
plt.figure(1)
plt.plot(T, k, 'k*')

# a) Lös logaritmerad (linjär) modell med minstakvadratmetoden
print('== a) Linjäriserad modell ==')
R = 1.98717
y = np.log(k)
A = np.column_stack((np.ones(T.shape), -1/(R*T)))
x = np.linalg.lstsq(A, y)[0] # funktionen returnerar flera saker,
                             # [0] är lösningen (x)
print('x =', x)

# Formulera modellen
c, E = x
a = np.exp(c)
print('a =', a)
k_lin = lambda T: a*np.exp(-E/(R*T))

# Beräkna residualens norm för den linjäriserade modellen,
# och motsvarande för den ursprungliga modellen
resnorm_lin = np.linalg.norm(y - A @ x)
resnorm_orig = np.linalg.norm(k - k_lin(T))
print('resnorm_lin =', resnorm_lin)
print('resnorm_orig =', resnorm_orig)

# Rita ut modellen
Tf = np.linspace(700, 1400)
plt.plot(Tf, k_lin(Tf), label='Linjäriserad')

# a) Gauss-Newton på den icke-linjära modellen
print('\n== a) Gauss-Newton ==')
F = lambda a, E: a*np.exp(-E/(R*T)) - k
J = lambda a, E: np.column_stack((
    np.exp(-E/(R*T)), # dF/da
    a*np.exp(-E/(R*T))*(-1/(R*T)) # dF/dE
))
X = np.array([a, E]) # startgissning från logaritmerade modellen
tol = 1e-10
diff = np.array([np.inf, np.inf])
i = 0
print(i, X)
while np.linalg.norm(diff) > tol:
    a2, E2 = X
    diff = -np.linalg.lstsq(J(a2,E2), F(a2,E2))[0]
    X += diff
    i += 1
    print(i, X, diff)

# Formulera modellen
a2, E2 = X
k_gn = lambda T: a2*np.exp(-E2/(R*T))

# Beräkna residualens norm
resnorm_gn = np.linalg.norm(k - k_gn(T))
print('resnorm_gn =', resnorm_gn, '=', np.linalg.norm(F(a2,E2)))

# Rita ut modellen
plt.plot(Tf, k_gn(Tf), '--', label='Gauss-Newton')
plt.legend()
plt.title('a) Data och modeller')

# Rita ut residualvektorn
plt.figure(2)
plt.plot(T, k - k_lin(T), label='Linjäriserad')
plt.plot(T, k - k_gn(T), '--', label='Gauss-Newton')
plt.legend()
plt.title('a) Residualer (data - modell)')

# b) Lös logaritmerad (linjär) treparametermodell
print('\n== b) Linjäriserad modell ==')
y = np.log(k)
A = np.column_stack((np.ones(T.shape), np.log(T), -1/(R*T)))
x = np.linalg.lstsq(A, y)[0]
c3, beta, E3 = x
a3 = np.exp(c3)
print('a =', a3, '| beta =', beta, '| E =', E3)
k_lin_b = lambda T: a3*(T**beta)*np.exp(-E3/(R*T))
resnorm_orig_b = np.linalg.norm(k - k_lin_b(T))
print('resnorm_orig_b =', resnorm_orig_b)

# b) Gauss-Newton på treparametermodellen
print('\n== b) Gauss-Newton ==')
F = lambda a, beta, E: a*(T**beta)*np.exp(-E/(R*T)) - k
J = lambda a, beta, E: np.column_stack((
    (T**beta)*np.exp(-E/(R*T)), # dF/da
    a*(T**beta)*np.log(T)*np.exp(-E/(R*T)), # dF/dbeta
    a*(T**beta)*np.exp(-E/(R*T))*(-1/(R*T)) # dF/dE
))
X = np.array([a3, beta, E3]) # startgissning från logaritmerade modellen
tol = 1e-10
diff = np.array([np.inf, np.inf, np.inf])
i = 0
print(i, X)
while np.linalg.norm(diff) > tol:
    a4, beta4, E4 = X
    diff = -np.linalg.lstsq(J(a4,beta4,E4), F(a4,beta4,E4))[0]
    X += diff
    i += 1
    print(i, X, diff)
a4, beta4, E4 = X
k_gn_b = lambda T: a4*(T**beta4)*np.exp(-E4/(R*T))
resnorm_gn_b = np.linalg.norm(k - k_gn_b(T))
print('resnorm_gn_b =', resnorm_gn_b)

# b) Rita ut data och kurvor
plt.figure(3)
plt.plot(T, k, 'k*')
plt.plot(Tf, k_lin_b(Tf), label='Linjäriserad')
plt.plot(Tf, k_gn_b(Tf), '--', label='Gauss-Newton')
plt.legend()
plt.title('b) Data och modeller')

plt.figure(4)
plt.plot(T, k - k_lin_b(T), label='Linjäriserad')
plt.plot(T, k - k_gn_b(T), '--', label='Gauss-Newton')
plt.legend()
plt.title('b) Residualer (data - modell)')

if __name__ == '__main__':
    plt.show()
