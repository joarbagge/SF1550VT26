import numpy as np
import matplotlib.pyplot as plt

def main():
    fig = plt.figure(1)
    plt.clf()

    # Plotta en cirkel
    R = 2
    c = (0, 1)
    t = np.linspace(0, 2*np.pi, 200)
    x = c[0] + R*np.cos(t)
    y = c[1] + R*np.sin(t)
    plt.plot(x, y, '--', color='black')

    # Plotta en fylld ellips
    a = 1.5
    b = 1
    c = (3, 0)
    x = c[0] + a*np.cos(t)
    y = c[1] + b*np.sin(t)
    plt.fill(x, y, color='tab:red')

    # Plotta en polygon
    c = (2, 3)
    x = c[0] + np.array([-0.6, 0.5, 0.45, -0.75, -1.25, -0.6])
    y = c[1] + np.array([-0.8, -0.35, 0.7, 1.0, 0.1, -0.8])
    plt.fill(x, y, color='tab:blue')
    plt.plot(x, y, color='tab:orange')

    plt.axis('equal') # riktiga x/y-proportioner
    plt.grid()
    plt.title('Diverse former')

if __name__ == '__main__':
    main()
    plt.show()
