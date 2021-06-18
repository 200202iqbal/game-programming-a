exam = input().split()
exam1  =int(exam[0])
exam2 = int(exam[1])
minscore = int(input())
rule = exam1,exam2 >=1 and exam1,exam2 <= 100 and minscore >=1 and minscore<=100
if(rule):
    if(minscore > exam1):
        print(exam1)
    elif(minscore<= exam1):
        print(exam1+exam2)
        