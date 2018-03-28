'''
Task

You are given two values a and b. 
Perform integer division and print a/b.

Input Format

The first line contains T, the number of test cases. 
The next T lines each contain the space separated values of a and b.

Constraints
0 < T < 10
Output Format

Print the value of a/b . 
In the case of ZeroDivisionError or ValueError, print the error code.


'''

T = int(input())

for i in range(T):
    try:
        a, b = input().split()
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except BaseException as e:
        print('Error Code:', e)

