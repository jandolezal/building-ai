"""
Exercise 9: Block or not

https://buildingai.elementsofai.com/Dealing-with-Uncertainty/the-bayes-rule#9
"""

"""
Advanced

Write a program that takes as input the probability of a follower being a bot (pbot), the
probability of a bot having a username with 8 digits (p8_bot), and the probability of a human
having a username with 8 digits (p8_human). The values for these inputs are free for you to
choose, but they have to be probabilitites, so they have to be between 0 and 1.
"""

def bot8(pbot, p8_bot, p8_human):
    joint_p8_bot = p8_bot * pbot
    joint_p8_human = p8_human * (1 - pbot) # phuman
    pbot_8 = joint_p8_bot / (joint_p8_bot + joint_p8_human) # p8
    return pbot_8 # changed from print(pbot_8)

# testing with intermediate excercise values
pbot = 0.05
p8_bot = 0.8
p8_human = 0.01

print(bot8(pbot, p8_bot, p8_human))
assert bot8(pbot, p8_bot, p8_human) == 0.8080808080808081
