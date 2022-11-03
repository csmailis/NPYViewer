
import numpy as np
import matplotlib.pyplot as plt
size = 24
sigma_x = 10.
sigma_y = 10.

x = np.linspace(-10, 10, size)
y = np.linspace(-10, 10, size)

x, y = np.meshgrid(x, y)
z = (1/(2*np.pi*sigma_x*sigma_y) * np.exp(-(x**2/(2*sigma_x**2)
     + y**2/(2*sigma_y**2))))
z *= (255.0/z.max()).astype(int)
np.save("gaussian.npy",z)
plt.imshow(z, cmap='gray')
plt.show()


