"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math


# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

###

import statistics
import math

# How long to cook pasta 
print('Courtney Pigford 1/21/23:')

print('How long cooking pasta')

scores = [
    8,
    9,
    10,
    11,
    12,
    3,
    4,
    5,
    13,
    14,
    15,
    12, 
    12, 
    12, 
    12, 

]

X = statistics.mean(scores)
y = statistics.mode(scores)
z = statistics.median(scores)
a = (statistics.stdev(scores))
b = (statistics.variance(scores))

print('the average cooking time is: ', X)
print('the most common time to cook pasta is: ', y)
print('the best cooking time for all pasta is: ', z)
print('the variance of cooking times is:  ', b)
print('Standard Deviation of the cooking times is: ', a)


xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 35]

correlationxy = statistics.correlation(xtimes_list, yvalues_list)

print('Correlationxy is: ', correlationxy)

slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
print('Slope: ',slope)
print('Interncept: ', intercept)

x_max = max(xtimes_list)
newx = x_max * 1.5  

print('newx: ', newx)

# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

newy = slope * newx + intercept
print('newy: ', newy)

max = max(scores)
min = min(scores)
len = len(scores)
sum = sum(scores)

avg = sum / len

asc_scores = sorted(scores)

desc_scores = sorted(scores, reverse=True)

print('max: ',max)
print('min: ', min)
print('len: ',len) 
print('sum: ',sum) 
print('Average: ',avg)
print('asc scores: ', asc_scores)
print('desc scores: ', desc_scores)
