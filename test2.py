'''Exercise 2: Randomness Test'''
import random as rd

# Lotery game
balls=[i for i in range(50)]
l=rd.sample(balls, 10)
l.sort()
print(l)

##unit test##

#test if output list is in ascending order:
print([l[i]<l[i+1] for i in range(9)])

#test if number of chosen balls is 10
print(len(l)==10)
