S = int(input())
A1,A2,A3,A4 = input().split()
A1 = int(A1)
A2 = int(A2)
A3 = int(A3)
A4 = int(A4)
rule = S,A1,A2,A3,A4 >= 1 and S <= 100 or A1,A2,A3,A4 <= 50
if rule:
    minvalue = min(A1,A2,A3,A4)
    print(minvalue * S)