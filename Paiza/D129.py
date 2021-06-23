#税率の変更
number = input().split()
z = int(number[0])
x = int(number[1])
y = int(number[2])

rule = z >= 100 and z<=2000 and z%100 == 0 and x,y >=1 and x,y<=100 and x < y
if(rule):
    z1 = (z * x)/100
    z2 = (z * y)/100
    result =int(abs(z1-z2))
    print(result)
