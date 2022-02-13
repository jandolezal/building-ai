"""
Exercise 7: Flip the coin

https://buildingai.elementsofai.com/Dealing-with-Uncertainty/probability-fundamentals
"""

# Beginner

# What is the probability of getting two consecutive tails when tossing a coin?

print(1/2 * 1/2)

# What is the probability of getting four consecutive heads when tossing a coin?
print((1/2)**4)


# Intermediatet
"""
Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones.
The input of the program is just the sequence and it should return a single number, 
which is the number of occurrences of "11".
"""

def count11(seq):
   count = 0
   for i in range(len(seq)-1):
       if seq[i] == seq[i + 1] == 1:
           count += 1 
   return count

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2


# Advanced

"""
Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the
probability of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)),
counts the number of occurrences of 5 consecutive ones ("11111") in the sequence, and outputs this number
as a return value.
Check that for p1 = 2/3, the count is close to 10000 x (2/3)^5 ≈ 1316.9.
"""

import numpy as np

def generate(p1):
    """Generates 10000 random zeros and ones where the probability of one is p1"""
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    """Returns the number of occurrences of 11111 in the sequence"""
    count = 0
    for i in range(len(seq)-4):
        if all(seq[i:i+5]):
            count += 1
    return count


def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
