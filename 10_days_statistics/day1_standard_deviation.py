import math
n = int(input())
x = list(map(int,input().split()))

mean = sum(x)/n

tu = 0
for val in x:
    tu += (val - mean)**2

sd = round(math.sqrt(tu/n), 1)
print(sd)
