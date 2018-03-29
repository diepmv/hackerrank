'''
problem:
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.


'''
alpha = float(input())
k = int(input())
e = 2.71828


def fact(n):
    result = 1
    for i in range(1, n +1):
        result *= i
    return result
p = float((alpha**k) * (e**(-1*alpha))) / fact(k)

print(round(p, 3))
