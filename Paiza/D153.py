A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if (A,B,C >= 1 and A,B,C <= 1000):
    if(not(A==B or A==C or B==A or B==C or C==A or C==B)):
        x  = (A,B,C)
        x = sorted(x)
        if(x[1]):
            print(x[1])

