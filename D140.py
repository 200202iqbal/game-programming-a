n = int(input())
string1,string2,string3,string4,string5,string6,string7,string8,string9,string10 =input().split()
string1 = str(string1)
string2 = str(string2)
string3 = str(string3)
string4 = str(string4)
string5 = str(string5)
string6 = str(string6)
string7 = str(string7)
string8 = str(string8)
string9 = str(string9)
string10 = str(string10)

string = list((string1,string2,string3,string4,string5,string6,string7,string8,string9,string10))

rule = n>=1 and n<=10 and len(string1),len(string2),len(string3),len(string4),len(string5),len(string6),len(string7),len(string8),len(string9),len(string10)>=1 and len(string1),len(string2),len(string3),len(string4),len(string5),len(string6),len(string7),len(string8),len(string9),len(string10)<=20
if(rule):
    
    print(string[n-1])
        
    
    