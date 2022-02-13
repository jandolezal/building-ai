
"""
Exercise 4: Probabilities

https://buildingai.elementsofai.com/Getting-started-with-AI/hill-climbing
"""


# Intermediate

import random

def main():
    prob = 0.80
    if random.random() < prob:
        print('dog')
    else:
        print('cat')

main()


# Advanced

import random

def main():

    random_number = random.random()
    if random_number < 0.8:
        favourite = "dogs"
    elif random_number < 0.9:
        favourite = "cats"
    else:
        favourite = "bats"

    print("I love " + favourite) 


main()
