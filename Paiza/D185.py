numbern = int(input())
numberm = int(input())
rule = numbern >= 1100 and numbern <= 5000 and numberm >=1 and numberm <= 200
if(rule):
    result = numbern * numberm
    print(result)
