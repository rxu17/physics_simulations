# Rixing Xu
#
# This program displays the accept and reject method - generate a value x with a pdf(x) as the gaussian distribution. 
# Then generate a y value where if it is greater than the pdf(x), we reject that x, otherwise we accept it  

# Physically, the gluon is emitted from the quark at an angle 
# Assumptions: the gluon is emitted between 0 and pi/2 radians, and its angle has a gaussian distribution 
import math
import random
import matplotlib.pyplot as plt

angles = [] 
mean = math.pi/2 # sets the mean and std for the gaussian function
std = 2

while len(angles) != 1000:
    x = random.random()*(math.pi/2.00) # our generated angle to accept or reject
    y = random.random() 
    g = math.exp((-(x-mean)**2)/(2*std))/(2*math.sqrt(std*math.pi)) # gaussian density distribution personalized for gluon angle
    
    if g >= y:
        angles.append(x)
    
plt.hist(angles, bins = 20, normed = True)
plt.title("Distribution of Gluon Angle")
plt.xlabel("Angle of emitted gluon")
plt.ylabel("Density")
plt.show()

