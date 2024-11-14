import numpy as np
import matplotlib.pyplot as plt

def subplots_side_by_side():
    x_data = np.linspace(0, 4 * np.pi, 1000)

    h_x = np.cos(x_data)
    k_x = np.sin(x_data)

    fig, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].plot(x_data, h_x, color = "red")
    ax[1].plot(x_data, k_x, color = "pink")

    for i, ax in enumerate(ax.flat):
        ax.set_title(f"Frame {i}")
        print(i)
    plt.show

def subplots_on_top_of_each_other():
    x_data = np.linspace(0, 4 * np.pi, 1000)

    h_x = np.cos(x_data)
    k_x = np.sin(x_data)
    
    fig, ax = plt.subplots(2, 1, figsize=(10,10))
    ax[0].plot(x_data, h_x, color = "red")
    ax[1].plot(x_data, k_x, color = "pink")

    for i, ax in enumerate(ax.flat):
        ax.set_title(f"Frame {i}")
        print(i)
    plt.show