"""
Exercise 8: Fishing in the Nordics

https://buildingai.elementsofai.com/Dealing-with-Uncertainty/probability-fundamentals
"""

"""
Beginner

What is the probability that the winner is a fisher given that they are Norwegian?
Be mindful of the innocent sounding distinction between the probability of X given Y
and the probability of Y given X.
"""

# P(fisher | Norweigian) =   fisher / Norwegian = 11611 / 5080000 = 0.299%


"""
Intermediate

Write a program that uses statistics about the population and fishing industry employment
to print out conditional probabilities of each nationality given that the winner works in
the fishing industry.
"""

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    for country, fisher in zip(countries, fishers):
            share = fisher / total_fishers * 100
            print("%s %.2f%%" % (country, share))


main()
print('- ' * 10)

"""
Advanced

Write a function that uses the above numbers and tries to guess the nationality of the winner
when we know that the winner is a fisher and their gender (either female or male).

The argument of the function should be the gender of the winner ('female' or 'male'). The 
return value of the function should be a pair (country, probability) where country is the
most likely nationality of the winner and probability is the probability of the country being
the nationality of the winner.
"""


countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    total_fishers = sum(fishers)

    shares = [(country, fisher/total_fishers*100) for country, fisher in zip(countries, fishers)]
    sorted_shares = [(country, share) for country, share in sorted(shares, key=lambda x: x[1], reverse=True)]
    guess, biggest = sorted_shares[0]

    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
