'''
problem:
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
'''
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = a+b, a
    return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
