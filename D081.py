n = int(input())
h,w = input().split()
h = int(h)
w = int(w)

rule = n>= 2 and n <= 10 and h,w>= 1 and h,w <=50
if(rule):
    result = (h * w)%n
    print(result)
    