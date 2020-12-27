''' Name:
    Description:
    Args:
    How to Run:
'''

import os
import sys
import math
import random
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


def random_num_gen(method : str, n : int, maxN : int = None, 
                   x0 : int = None, m :int = None, a : int = None, c : int = None) -> list:
    ''' Function that ultilizes various random number generating methods:
        Example: Linear Congruent Method (LCM) 
                 LCM background found:
                 http://sites.science.oregonstate.edu/~landaur/nacphy/ComPhys/MONTE/mc3/node2.html

        Args: method - method of random number generating: ['simple', 'lcm']
              n - number of random numbers to be generated
              maxN - maximum number allowed to be generated (simple)
              x0 - the initial number in the sequence (lcm)
              m - the modulus (lcm)
              a - multiplier (lcm)
              c - the increment/constant (lcm)

        Returns: list of randomnly generated numbers specified by n
    '''
    assert type(method) is str, "method needs to be string"
    if method == "simple":
        assert maxN > 0 and n > 0, "maxN and n should be greater than 0"
        num_seq = [0 for i in range(0, n)] # dummy list
        for i in range(0, n):
            num_seq[i] = random.randint(0, maxN)

    elif method == "lcm":
        # check that m (modulus) is greater than 0, and a, c, n, max are +
        assert a >= 0 and c >= 0 and n > 0 and m > 0 and x0 >= 0,\
            "Modulus(m), multiplier term(a), increment term(c), "\
            "max number, and number of terms (n) must be greater than 0"

        num_seq = [0] * n # dummy list

        # create the first initial random num
        num_seq[0] = x0
        # run the algorithm
        for i in range(1, n):
            num_seq[i] = ((a*num_seq[i-1]) + c) % m
    else:
        print("Please select a valid method.")
        sys.exit()
    return(num_seq)


def random_walk(method : str, n : int) -> dict:
    ''' Function

        Methods: 
            radian - pick x and y between 0 and 2pi
            directional - pick a random direction for a step of 1
            sqrt - pick a 
            normalize
            avg - 

        Args:  method - method in list 
               n - number of x,y pairs to generate

        Returns: 
    '''

    def generate_x_y(method : str, prev_x : int, prev_y : int):
        ''' Function that generates the next 2D x and y coordinate
            based on method for unit steps

            Args:  method - method in list 
                   prev_x -
                   prev_y - 

            Returns: list of x, y pair
        '''
        assert method is not None and type(method) is str, \
            "method is not defined or is not of string type"
        assert prev_x is not None and prev_y is not None,\
            "prev_x and prev_y are not defined or not of string type"

        if method == "radian":
            theta = random.uniform(a = 0, b = math.pi*2)
            deltaX = math.cos(theta)
            deltaY = math.sin(theta)

        elif method == "directional":
            direct_dict = {0: [1, 0],
                        1: [0, 1],
                        2: [-1, 0],
                        3: [0, -1]}
            direction = random.choice([0, 1, 2, 3])
            deltaX = direct_dict[direction][0]
            deltaY = direct_dict[direction][1]
            
        elif method == "sqrt":
            deltaX = random.uniform(a = -1, b = 1)
            sign = random.choice([1, -1])
            deltaY = sign * (math.sqrt(1 - deltaX**2))

        elif method == "normalize":
            deltaX = random.uniform(a = -1, b = 1)
            deltaY = random.uniform(a = -1, b = 1)

        elif method == "avg":
            deltaX = random.uniform(a = -(math.sqrt(2)), b = math.sqrt(2))
            deltaY = random.uniform(a = -(math.sqrt(2)), b = math.sqrt(2))
        return([prev_x + deltaX, prev_y + deltaY])

    coord = {'x':[0] * n,
             'y':[0] * n}
    r_list = [0] * n

    # start at origin always
    for i in range(1, n):
        x_y_pair = generate_x_y(method, prev_x = coord['x'][i-1], 
                                        prev_y = coord['y'][i-1])
        coord['x'][i] = x_y_pair[0]
        coord['y'][i] = x_y_pair[1]
        r_list[i] = math.sqrt(x_y_pair[0]**2 + x_y_pair[1]**2)
    return({"r_values" : r_list,
            "coordinates" : coord})


def vet_methods(typeRandom : str, method : str = None, rand_list : list = None,
                         xList : list = None, yList : list = None,
                         xList2 : list = None, yList2 : list = None,
                         xList3 : list = None, yList3 : list = None,
                         plot_R : bool = True):
    ''' Function that plots the random generators

        Args: typeRandom - ['random_generator', 'random_walk']
              method - method of random number generating: ['simple', 'lcm']
              rand_list - input list of random numbers
    '''
    if typeRandom == "random_generator":
        # split our list into two, (successive pairs) and plot
        assert rand_list is not None
        x = [rand_list[i] for i in range(1, len(rand_list)-1)]
        y = [rand_list[j] for j in range(2, len(rand_list))]
        plt.scatter(x, y)
        plt.title("{} Random Number Generator".format(method))

    elif typeRandom == "random_walk":
        assert xList is not None and yList is not None
        if plot_R:
            plt.plot(xList, yList, label = "avg")
            plt.plot(xList2, yList2, label = "radian")
            plt.plot(xList3, yList3, label = "sqrt")
            plt.legend()
        else:
            plt.plot(xList, yList, color = 'blue')
            plt.subplot(3, 1, 1)
            plt.plot(xList2, yList2, color = 'green')
            plt.subplot(3, 1, 2)
            plt.plot(xList3, yList3, color = 'red')
            plt.subplot(3, 1, 3)

        plt.title("Random Walk".format(method))
        
    if plot_R:
        plt.xlabel("sqrt(N)")
        plt.ylabel("R")
    else:
        plt.xlabel("X")
        plt.ylabel("Y")

    # plot
    plt.show()


def main():
    '''
    '''
    sim_list = random_num_gen(method = "simple", n = 1000, maxN = 1241)
    lcm_list = random_num_gen(method = "lcm", n = 1000, x0 = 2, m = 1241, a = 13, c = 12)
    vet_random_generator(typeRandom = "random_generator", method = "simple", rand_list = sim_list)
    vet_random_generator(typeRandom = "random_generator", method = "lcm", rand_list = lcm_list)

    walk_values = random_walk(method = "avg", n = 100000)
    walk_values2 = random_walk(method = "radian", n = 100000)
    walk_values3 = random_walk(method = "directional", n = 100000)

    vet_methods(typeRandom = "random_walk", 
                         xList = walk_values['coordinates']['x'],
                         yList = walk_values['coordinates']['y'],
                         xList2 = walk_values2['coordinates']['x'],
                         yList2 = walk_values2['coordinates']['y'],
                         xList3 = walk_values3['coordinates']['x'],
                         yList3 = walk_values3['coordinates']['y'],
                         plot_R = False)

    vet_method(typeRandom = "random_walk", 
                         xList = [math.sqrt(x) for x in range(1, len(walk_values['r_values'])+1)],
                         yList = walk_values['r_values'],
                         xList2 = [math.sqrt(x) for x in range(1, len(walk_values2['r_values'])+1)],
                         yList2 = walk_values2['r_values'],
                         xList3 = [math.sqrt(x) for x in range(1, len(walk_values3['r_values'])+1)],
                         yList3 = walk_values3['r_values'])

if __name__ == "__main__":
    main()

