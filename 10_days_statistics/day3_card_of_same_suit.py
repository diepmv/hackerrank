'''
problem:

Objective 
In this challenge, we're getting started with combinations and permutations. Check out the Tutorial tab for learning materials! 


Task 
You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
'''


(4 * C[2, 13]) / (C[2, 52]) = 4*[13!/(2! * 11!)] / [52!/(2! * 50!)] = 4/17
