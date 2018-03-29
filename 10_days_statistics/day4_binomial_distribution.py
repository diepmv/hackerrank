'''
problem:
Task 
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).
'''

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(a, b):
    return factorial(b)/(factorial(a)*factorial(b-a))



boy, girl = 1.09, 1
p_boy = 1.09/(1+1.09)
p_girl = 1 - p_boy

total = 0
for i in range(3, 7):
    total += combination(i, 6)* (p_boy)**(i) * (p_girl)**(6-i)
print(round(total, 3))
