# Rixing Xu
#
# Program generates random numbers distributed unifromly between [0.25,0.75] and plotted on a histogram, can only use random.random function. 
# Physically, in a high energy proton-proton collision, quarks are emitted. These quarks emitt a gluon and will lose part of its energy to that gluon. 

# Assumptions: The gluon takes 25% to 75% of the original particle's energy, and doesn't favor any energy percentage in between

import random
import math
import numpy as np
import matplotlib.pyplot as plt

Z = [] # stores percentage of original energy that the particle takes
for i in range(1000):
    Z.append(random.random()* 0.5 + 0.25)
    
plt.hist(Z, bins = 20, normed = True)
plt.title("Uniform distribution [0.25,0.75]")
plt.xlabel("Emitted Gluon Energy Percentage (of original)")
plt.ylabel("Density")
plt.show()
