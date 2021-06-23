time = int(input())
rule = time >= 1 and time <= 100
x = time
count = 0
if(rule):
    while(x > 0):
        time -= 24
        x = time
        count +=1
    print(count)
        