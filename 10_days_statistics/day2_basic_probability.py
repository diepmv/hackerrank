"""
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
"""

dice_min = 1
dice_max = 6

count = 0 

for i in range(dice_min, dice_max+1):
  for j in range(dice_min, dice_max+1):
    if i+j <=9:
      count += 1

print(float(count)/36)
