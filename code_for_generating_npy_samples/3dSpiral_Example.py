
import numpy as np
import matplotlib.pyplot as plt



ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 64, 64)
xline = np.sin(zline)
yline = np.cos(zline)

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
temp=np.array([xdata,ydata,zdata])
temp=temp.T
print(np.shape(temp))
np.save("3DSpiral.npy",temp)
ax.scatter3D(xdata,ydata,zdata, c='r');

