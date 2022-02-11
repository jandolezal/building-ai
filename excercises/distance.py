"""
Exercise 15: Vector distances

https://buildingai.elementsofai.com/Machine-Learning/the-nearest-neighbor-method
"""


# Beginner

a = [14, 3, 0.8]
b = [2, 6, 0.8]

def distance(a, b):
    return (sum((r - s)**2 for r, s in zip(a, b)))**(1/2)

print(distance(a, b))


# Intermediate

import numpy as np

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


print(distance(a, b))


# Advanced

import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf

    for i, vector in enumerate(x_train):
        distance = dist(vector, x_test)
        if distance < min_distance:
            min_distance = distance
            nearest = i

    print(nearest)

nearest(x_train, x_test)
