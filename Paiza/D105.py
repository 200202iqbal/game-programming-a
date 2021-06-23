s1 = str(input())
s2 = str(input())

rule = len(s1),len(s2) >= 1 and len(s1),len(s2) <=100
if ( rule ):
    if (len(s1) == len(s2)) :
        print("Yes")
    else:
        print("No")