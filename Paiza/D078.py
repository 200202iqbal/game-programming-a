import statistics
a,b,c,d,e,f,g = input().split()
x = int(input())
a = int(a)
b = int(b)
c = int(c)
d = int(d)
f = int(f)
g = int(g)
average = 0
if(a,b,c,d,e,f,g>=0 and a,b,c,d,e,f,g<=100):
    i = 0
    for result in a,b,c,d,e,f,g:
        result = int(result)
        average += result
        i +=1
    average = average/i     
    if(average>=x):
        print("pass")
    else:
        print("failure")