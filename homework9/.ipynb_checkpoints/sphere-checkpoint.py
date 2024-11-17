import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits import mplot3d

def plot_sphere(r): 
    """
    This function will plot a sphere given a radius r :)
    """

    """creating a figure"""
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    """creates the data"""
    theta = np.linspace(0, 2 * np.pi, 20)
    phi = np.linspace(0, np.pi, 20)

    theta, phi = np.meshgrid(theta, phi)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    """plots the surface"""
    surf = ax.plot_surface(x, y, z, cmap='viridis', label = "sphere surface")

    """ labels axes, sets title, makes legend"""
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Sphere!!!')
    ax.legend(bbox_to_anchor=(1.5, 1))

    plt.show()
