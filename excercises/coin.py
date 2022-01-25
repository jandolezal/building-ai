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


