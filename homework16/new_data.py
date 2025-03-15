import torch
import numpy as np

# Underlying Pattern we are trying to find 
x_data = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)

pattern = np.cos(X) +Y

# Actual data that we will be using
# Defining the dataset dimensions
N, D_in, H, D_out = 1000, 2, 50, 1

# Creating the input data
x = torch.randn(N, D_in) * 3.1415
y = (x[:, 0].cos() + x[:, 1]).unsqueeze(1)

obscure = torch.randn(N, D_out) * 0.3
y += obscure

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()