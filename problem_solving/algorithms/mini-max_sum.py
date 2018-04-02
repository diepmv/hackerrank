'''
problem:

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

+Each integer is in the inclusive range [1...10**9].
Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)


'''

import os
import sys
def miniMaxSum(arr):
    lst = list()
    for i in range(len(arr)):
        temp = list()
        for j in range(len(arr)):
            if i != j:
                temp.append(arr[j])
        lst.append(sum(temp))
    print(min(lst), max(lst))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
