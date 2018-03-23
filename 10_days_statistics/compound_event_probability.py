"""
In this challenge, we practice calculating the probability of a compound event. We recommend you review today's Probability Tutorial before attempting this challenge. 

Task**
There are 3 urns labeled X, Y, and Z.

Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
ref url: https://www.hackerrank.com/challenges/s10-mcq-3/problem
"""

from fractions import Fraction

x = [4, 3]
y = [5, 4]
z = [4, 4]

# The probabilities of pulling red form each urn
xr = x[0] / sum(x)
yr = y[0] / sum(y)
zr = z[0] / sum(z)

p = (xr * yr * (1 - zr)) + (xr * (1 - yr) * zr) + ((1 - xr) * yr * zr)
p_frac = Fraction(p).limit_denominator() # Fraction form

print(f"The probability of drawing 2 reds and one black is {p}, or {p_frac}.")
