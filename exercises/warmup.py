"""
Exercise 5: Warm-up Temperature

https://buildingai.elementsofai.com/Getting-started-with-AI/hill-climbing
"""

# Beginner

from math import exp

def beginner():
    S_old = 205
    S_new = 196
    T = 5

    prob = exp(-(S_old - S_new)/T)
    print(f'The probability that we choose the new score is {prob:.2f}')

beginner()


# Intermediate
def intermediate(T):
    S_old = 205
    S_new = 196

    prob = exp(-(S_old - S_new)/T)
    print(f'With T {T} the probability we choose new score is {prob:.2f}')
    return prob


T = 1
while True:
    prob = intermediate(T)
    if prob >= 0.5:
        break
    T += 1

# Advanced

import random


def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    if S_new > S_old:
        return 1.0
    else:
        return exp(-(S_old - S_new)/T)


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)
