import random
import math
import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos = dataA
ypos = np.ones(len(dataA))
zpos = np.zeros(len(dataA))
dx = np.ones(len(dataA))
dy = np.ones(len(dataA))
dz = np.ones(len(dataA))
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()
