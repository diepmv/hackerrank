'''
https://www.hackerrank.com/challenges/grading/problem
'''


import os
import sys

#
# Complete the gradingStudents function below.
#

def next_mul_of_5(grade):
    return ((grade // 5) + 1) * 5
    
def gradingStudents(grades):
    #
    # Write your code here.
    #
    lst = list()
    for grade in grades:
        if grade >= 38:
            next_grade = next_mul_of_5(grade)
            if next_grade - grade < 3:
                lst.append(next_grade)
            else:
                lst.append(grade)
        else:
            lst.append(grade)
    return lst 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

