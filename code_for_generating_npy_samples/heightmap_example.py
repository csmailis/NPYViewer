
from PIL import Image
import numpy as np
heightmap = Image.open("Heightmap.png")

np.save("heightmap.npy",heightmap)
