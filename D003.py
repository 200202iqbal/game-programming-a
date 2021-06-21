n = int(input())
rule = n >=1 and n <=100
cnt=0
if(rule):
    for i in range(1,10):
        print(i*n,end="")
        if(cnt<8):
           print(end=" ")
        cnt+=1
        
        
