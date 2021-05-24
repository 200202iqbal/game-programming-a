h,m = input().split(":")
h = int(h)
m = int(m)
if(h>=0 and h<=12 or m>=0 and m<=59):
    if(h<=8):
        hour = 24 +(h-8)
        print(hour,end=":")
        print(m)
    else:
        h -= 8
        hour= h
        print(hour,end=":")
        print(m)
    
    