"""
Generate S list from X and F
Calculate Q2 of S
calculate Q1 of left half, calculate Q2 of right half
*****************************************************
"""

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
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
print(interquartile_range)
