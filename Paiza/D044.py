name,gender = input().split()
name = str(name)
gender = str(gender)
rule = len(name) >= 1 and len(name)<=100 and gender == "M","F"
if(rule):
    if(gender =="M"):
        print("Hi, Mr.",name)
    else:
        print("Hi, Ms.",name)