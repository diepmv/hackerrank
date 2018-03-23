"""
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.
"""

dice_max = 6
dice_min = 1
count = 0

for i in range(dice_min, dice_max+1):
  for j in range(dice_min, dice_max+1):
    if i != j and i+j==6:
      count += 1

print("count: ", count)
print("probability: ", '{0}/{1}'.format(count, '36'))
