number = int(input())
option= input().split()
option[0] = str(option[0])
option[1] = str(option[1])
option[2] = str(option[2])
rule = number,len(option[0]),len(option[1]),len(option[2]) >= 1 and number<=3 and len(option[0]),len(option[1]),len(option[2]) <=20
if(rule):
    number -= 1
    if(number == 0):
        print(option[0])
    elif(number == 1):
        print(option[1])
    else:
        print(option[2])