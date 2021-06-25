#D178:逆さにする 
n = int(input())
rule = n >= 1 and n <= 20
if(rule):
    s = input()
    if(len(s) == n):
        reversedS = s[::-1]
        print(reversedS)
