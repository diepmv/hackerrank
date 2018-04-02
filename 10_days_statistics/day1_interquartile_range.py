"""
Generate S list from X and F
Calculate Q2 of S
calculate Q1 of left half, calculate Q2 of right half
*****************************************************
"""

n = int(input())
X = list(map(int, input().split()))
#X = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 10, 40, 30, 50, 20, 10, 40, 30, 50]

F = list(map(int, input().split()))
#F = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]


#calculate the S
S = list()

for i, j in zip(X, F):
    S.extend([i]*j)
S.sort()   


#define median function
def median(n, L):
    if n % 2 == 0:
        return (L[n//2 -1] + L[n//2])/2, n//2, n//2
    else:
        return L[n//2], n//2, n//2 + 1

Q2, k1, k2 = median(len(S), S)


S1 = S[:k1]
S2 = S[k2:]

Q1 = median(len(S1), S1)[0]
Q3 = median(len(S2), S2)[0]


interquartile_range = round(Q3-Q1, 1)

print("{0:.1f}".format(interquartile_range))
