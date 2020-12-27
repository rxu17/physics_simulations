''' Name: monte_carlo_simulator.py
    Description: Simulator script for Monte Carlo methods in Physics
        Methods: -random number generator using LCM
                 -random walk using various methods
                 -radioactive decay 
    Args: nCount
    How to Run: python monte_carlo_simulator.py -nCount <numbers to generate>
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
    ''' Function that generates x and y coordinates based on 
        method of creating 2D unit steps (deltaX, deltaY)
        as well as R values, where R is the distance from the 
        starting point origin (0,0)

        Methods: 
            radian - pick deltaX and deltaY between 0 and 2pi
            directional - pick a random direction for a step of 1 in that dir
            sqrt - deltaX is in range [-1. 1], deltaY is +/- (1- sqrt(deltaX^2))
            normalize - deltaX and deltaY are in range [-1, 1], not 0 and normalized
            avg - deltaX and deltaY are in range [-sqrt(2), sqrt(2)]

        Args:  method - method in list above
               n - number of x,y pairs to generate

        Returns: dictionary of R values and associated 
                x and y values
    '''

    def generate_x_y(method : str, prev_x : int, prev_y : int):
        ''' Function that generates the next 2D x and y coordinate
            based on method for unit steps

            Args:  method - method in list in random_walk function
                   prev_x - previous x coordinate
                   prev_y - previous y coordinate

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
            scaled_var = math.sqrt(deltaX**2 + deltaY**2)/1
            deltaX = deltaX/scaled_var
            deltaY = deltaY/scaled_var

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
                         xList4 : list = None, yList4 : list = None,
                         xList5 : list = None, yList5 : list = None,
                         plot_R : bool = True):
    ''' Function that plots the random generators and random walk
        methods

        Args: typeRandom - ['random_generator', 'random_walk']
              method - method of random number generating: ['simple', 'lcm']
              rand_list - input list of random numbers
              xList ... xList5 - input list(s) of x coordinates
              yList ... yList5 - input list(s) of y coordinates
              plot_R - bool, if we are plotting R values vs sqrt(N)
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
            plt.plot(xList4, yList4, label = "directional")
            plt.plot(xList5, yList5, label = "avg")
            plt.legend()
        else:
            plt.plot(xList, yList, color = 'blue')
            plt.subplot(5, 1, 1)
            plt.plot(xList2, yList2, color = 'green')
            plt.subplot(5, 1, 2)
            plt.plot(xList3, yList3, color = 'red')
            plt.subplot(5, 1, 3)
            plt.plot(xList4, yList4, color = 'yellow')
            plt.subplot(5, 1, 4)
            plt.plot(xList5, yList5, color = 'purple')
            plt.subplot(5, 1, 5)

        plt.title("Random Walk".format(method))
        
    if plot_R:
        plt.xlabel("sqrt(N)")
        plt.ylabel("R")
    else:
        plt.xlabel("X")
        plt.ylabel("Y")

    # plot
    plt.show()


def parse_args():
    ''' Parse the required args for running script which is 
        just number of numbers to generate for now

        Returns: parser object to select arguments of choice
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-nCount', '--num_of_numbers', type = int, 
                        default = 2, nargs='?',
                        help="Number of numbers or steps to generate")

    return(parser.parse_args())


def main():
    ''' Run all comparison plots for random walk generator and random
        number generators
    '''
    args = parse_args()
    # generate random values for each of the 5 methods and plot
    sim_list = random_num_gen(method = "simple", n = args.num_of_numbers, maxN = 1241)
    lcm_list = random_num_gen(method = "lcm", n = args.num_of_numbers, x0 = 2, m = 1241, a = 13, c = 12)
    vet_methods(typeRandom = "random_generator", method = "simple", rand_list = sim_list)
    vet_methods(typeRandom = "random_generator", method = "lcm", rand_list = lcm_list)

    # generate walk values for each of the 5 methods and plot
    walk_values = random_walk(method = "avg", n = args.num_of_numbers)
    walk_values2 = random_walk(method = "radian", n = args.num_of_numbers)
    walk_values3 = random_walk(method = "sqrt", n = args.num_of_numbers)
    walk_values4 = random_walk(method = "directional", n = args.num_of_numbers)
    walk_values5 = random_walk(method = "normalize", n = args.num_of_numbers)


    vet_methods(typeRandom = "random_walk", 
                         xList = walk_values['coordinates']['x'],
                         yList = walk_values['coordinates']['y'],
                         xList2 = walk_values2['coordinates']['x'],
                         yList2 = walk_values2['coordinates']['y'],
                         xList3 = walk_values3['coordinates']['x'],
                         yList3 = walk_values3['coordinates']['y'],
                         xList4 = walk_values4['coordinates']['x'],
                         yList4 = walk_values4['coordinates']['y'],
                         xList5 = walk_values5['coordinates']['x'],
                         yList5 = walk_values5['coordinates']['y'],
                         plot_R = False)

    vet_methods(typeRandom = "random_walk", 
                         xList = [math.sqrt(x) for x in range(1, len(walk_values['r_values'])+1)],
                         yList = walk_values['r_values'],
                         xList2 = [math.sqrt(x) for x in range(1, len(walk_values2['r_values'])+1)],
                         yList2 = walk_values2['r_values'],
                         xList3 = [math.sqrt(x) for x in range(1, len(walk_values3['r_values'])+1)],
                         yList3 = walk_values3['r_values'],
                         xList4 = [math.sqrt(x) for x in range(1, len(walk_values4['r_values'])+1)],
                         yList4 = walk_values4['r_values'],
                         xList5 = [math.sqrt(x) for x in range(1, len(walk_values5['r_values'])+1)],
                         yList5 = walk_values5['r_values'])

if __name__ == "__main__":
    main()

