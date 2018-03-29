'''
problem:
Task 
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?
'''


rejected_percentage = 12
batch = 10

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(a, b):
    return factorial(b)/(factorial(a)*factorial(b-a))

rejected_p = rejected_percentage/100
accept_p = 1 - rejected_p
#<=2 rejected
total = 0
for i in range(0, 3):
    total += combination(i, batch) * (rejected_p**i) * (accept_p**(batch-i))
print(round(total, 3))

total = 0
for i in range(2, batch+1):
    total += combination(i, batch) * (rejected_p**i) * (accept_p**(batch-i))
print(round(total, 3))    
