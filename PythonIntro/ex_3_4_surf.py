import numpy as np
import matplotlib.pyplot as plt

def main():
    # Skapa en figur med en 3D-axel
    fig = plt.figure(1)
    plt.clf()
    ax = fig.add_subplot(projection='3d') # viktigt

    # Plotta en funktionsgraf som en yta
    def f(x, y):
        r = np.sqrt(x**2 + y**2)
        return np.sin(r) / r

    x = np.linspace(-20, 20, 100)
    y = np.linspace(-20, 20, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    ax.plot_surface(X, Y, Z)
    plt.tight_layout() # utnyttja utrymmet bättre

if __name__ == '__main__':
    main()
    plt.show()
