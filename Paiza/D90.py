#下一桁はいくつ
number = input().split()
total = 0
rule1 = len(number) == 5
if(rule1):
    for _ in number:
        if(int(_) >= 0 and int(_) <=100):
            total += int(_) 
total = str(total)
flag = True
for _ in reversed(total):
    if (flag):
        result = _
        flag = False
        
print(result)