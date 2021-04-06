# Just a program to combine the random generators for the gluon emission angle and gluon energy

import random
import math
import numpy as np
import matplotlib.pyplot as plt

dataZ = []    
dataTheta = []


while len(dataA) != 1000:
    dataZ.append(random.random()*0.5 + 0.25)
    
    x = random.random()*(math.pi/2.00)
    y = random.random()
    # gaussian function with mean of 5 and standard deviation of 1
    g = math.exp((-(x-(math.pi/4.00))**2)/4)/(2*math.sqrt(2*math.pi))
    
    if g >= y:
        dataTheta.append(x)
    
plt.hist(dataA, bins = 20, normed = True)
plt.hist(data2, bins = 20, normed = True)
plt.xlabel("Z and theta values")
plt.ylabel("Frequency")
plt.show()


