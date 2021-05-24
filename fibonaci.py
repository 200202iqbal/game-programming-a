#Fibonacci series:
# the of two element defines the next
a,b = 0,1
while a < 10:
    print(a,end=",")
    a,b = b,a+b
#result = 0,1,1,2,3,5,8,