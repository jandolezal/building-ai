"""
Exercise 12: Least squares

https://buildingai.elementsofai.com/Machine-Learning/linear-regression
"""


# Intermediate

import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        predicted = (xi @ c).sum()
        squared_error = (yi - predicted)**2
        sse += squared_error

    print(sse)

squared_error(X, y, c)

print('-' * 10)



# Advanced

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for i, coeff in enumerate(c):
        sse = 0.0
        for xi, yi in zip(X, y):
            predicted = (xi @ coeff).sum()
            squared_error = (yi - predicted)**2
            sse += squared_error
        if sse < smallest_error:
            smallest_error = sse
            best_index = i

    print("the best set is set %d" % best_index)


find_best(X, y, c)
