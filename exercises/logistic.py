"""
Exercise 20: Logistic regression

https://buildingai.elementsofai.com/Neural-Networks/logistic-regression
"""


# Advanced

import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z, c):
    # add your implementation of the sigmoid function here
    result = 1/(1 + math.exp(-(z * c).sum()))
    print(result)

# calculate the output of the sigmoid for x with all three coefficients
for c in [c1, c2, c3]:
    sigmoid(x, c)
