n = int(input())
rule = n >=1 and n<=6

if(rule):
    if(n == 3):
        print("4")
    elif(n == 1):
        print("6")
    elif(n == 2):
        print("5")
    elif(n == 4):
        print("3")
    elif(n == 6):
        print("1")
    elif(n == 5):
        print("2")