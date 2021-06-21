word = input().split()
rule = len(word) >=1 and len(word)<=10
if(rule):
    cnt = 0
    for _ in word:
        word = _.upper()
        if(_ == "W"):
            cnt+=1
if(cnt >=5):
    print("OK")
else:
    print("NG")
    