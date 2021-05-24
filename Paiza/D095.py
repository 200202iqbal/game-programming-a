import math
N = int(input())
M = int(input())
if( N,M >= 100 and N,M <= 2000):
    if(M<=N):
        result = math.floor(N/M)
        print(result)