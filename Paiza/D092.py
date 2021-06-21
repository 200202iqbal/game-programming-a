x1,y1,price1 = input().split()
x2,y2,price2 = input().split()
x1 = int(x1)
y1 = int(y1)
price1 = int(price1)

x2 = int(x2)
y2 = int(y2)
price2 = int(price2)

rule = x1,x2,y1,y2 >= 1 and x1,x2,y1,y2 <= 30 and price1,price2 >= 1000 and price1,price2 <= 50000
if(rule):
    result1= price1 / (x1*y1)
    result2= price2 / (x2*y2)
    if(result1 > result2):
        print(x2,y2,price2,end="")
    elif(result1 == result2):
        print("DRAW")
    else:
        print(x1,y1,price1,end="")
    
    
    