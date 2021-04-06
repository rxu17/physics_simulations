# Rixing Xu
# 
# This program implements a more physical distribution for Z and theta so that the emitted particle only takes a 
# small fraction of the original energy and the angle at which the particle is emitted favors small angles. 
#
# Now theta and Z take a 1/x distribution as their pdf(x). However, have to experiment with 1/x + const to get 
# rid of the singularity at x = 0

import numpy as np
import matplotlib.pyplot as plt
import math 
import random

dataZ = [] # holds the accepted energy percentage values 
dataTheta = [] # holds the accepted theta values

# This adds the Z values (percentage of original energy) 
while len(dataZ) < 2000:
    x = random.random()*(0.5) + 0.25
    y = random.random()
    
    pdZ = 1/(x + 0.00001)
    
    if y <= pdZ:
        dataZ.append(x)
        
# tThis adds the theta values between 0 and pi/2     
while len(dataTheta) < 2000:
    x = random.random()*(math.pi/2.00)
    y = random.random()
    
    pdT = 1/(x + 0.5)
    
    if y <= pdT:
        dataTheta.append(x)

plt.hist(dataZ, bins = 10, alpha = 0.5, label = 'Z', normed = True)
plt.hist(dataTheta, bins = 10, alpha = 0.5, label = 'theta', normed = True)
plt.xlabel("Z and theta values")
plt.ylabel("Density")
plt.title("Z and theta values (1/x distribution favoring smaller angles and Z")
plt.legend(loc = 'upper right')
plt.show()
