import numpy as np

# Create a random numpy array
arr = np.random.randint(low=0, high=2, size=(5, 5))

# Save the numpy array to an .npy file
np.save("graph.npy", arr)
