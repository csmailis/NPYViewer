#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:13:19 2021

@author: user
"""
from PIL import Image
import numpy as np
heightmap = Image.open("Heightmap.png")

np.save("heightmap.npy",heightmap)