#D034:どれにしようかな
n = int(input())
rule = n>=2 and n<= 21
if(rule):
    result = 21%n
    if(result == 0):
        result=n
        print(result)
    else:
        print(result)