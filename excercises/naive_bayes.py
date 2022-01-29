"""
Exercise 10: Naive Bayes classifier

https://buildingai.elementsofai.com/Dealing-with-Uncertainty/naive-bayes-classifier
"""

# Beginner

def dice(odds, p1, p2):
    count = 0
    while odds[0] < 100:
        r = p2/p1 # likelihood ratio
        odds[0] = odds[0] * r
        count += 1
        print(f'Odds with {count} roll are {int(odds[0])}:{odds[1]}')
    return count

odds = [1, 1]
p1 = 1/6
p2 = 1/2

count = dice(odds, p1, p2)
print(count)
assert count == 5

print('- ' * 10)


# Intermediate

def flip(n):
    odds = 1.0 # start with 50% chance of the magic coin, which is the same as odds = 1:1
    p1 = 1/2
    p2 = 1/1
    for i in range(n):
        r = p2/p1
        odds = odds * r
        
    print(odds)

n = 1
flip(n)

print('- ' * 10)


# Advanced

import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1
    for roll in sequence:
        r = p2[roll - 1] / p1[roll - 1]
        odds = odds * r
    if odds > 1:
        return True
    else:
        return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
