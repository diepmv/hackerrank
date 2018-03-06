#!/bin/python3

"""
Problem:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

url: https://www.hackerrank.com/challenges/diagonal-difference/problem
"""



import sys

def diagonalDifference(a):
    # Complete this function
    
    diag1 = sum([a[i][i] for i in range(len(a))])
    diag2 = sum([a[len(a) -i - 1][i] for i in range(len(a))])
    return abs(diag1 - diag2)



if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
