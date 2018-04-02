'''
problem:
Input Format

The first line contains an integer, n, denoting the size of the array. 
The second line contains n space-separated integers describing an array of numbers arr(a0, a1, a2,...,an-1).

Output Format

You must print the following 3 lines:

1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeros in the array compared to its size.

'''

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    pos, neg, zero = count(arr)
    print(pos/n)
    print(neg/n)
    print(zero/n)
    
    
def count(arr):
    pos, neg, zero = 0,0,0
    for i in arr:
        if i >0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1
    return pos, neg, zero

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
