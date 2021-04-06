''' Name: toy_monte_carlo_methods.py
    Description: Script for producing 2D/3D Monte Carlo simulations in Physics
        Methods: random number generator
                 accept-reject method
    Args:
    How to Run: python toy_monte_carlo_methods.py

    Practice writing a program in Python that generates random numbers. 
    In the first case, write a program to generate 1000 random numbers 
    distributed uniformly between [0,1] and make a histogram of these numbers. 
    In the second case, write a program that distributes the random numbers 
    between [5,15] and makes a histogram. Remember, it is only allowed to use 
    the random.random() functionality in Python. As a hint, think about how to 
    make the minimum and maximum of the [0,1] distribution into the minimum and 
    maximum of the [5,15] distribution.

    Practice writing a program in Python that generates random numbers, 
    distributed according to a Gaussian distribution with a mean μ of 5 
    and a width σ of 2 in the range of [0,10].
'''

import os
import sys
import math
import random
import argparse
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

def generate_random_number(gen_type : str, mean : int, width : int):
    if gen_type == "uniform":
        x = random.random()
    y = random.random()

    elif gen_type == "gauss"