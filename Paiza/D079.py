word = str(input())
rule = len(word) >= 2 and len(word)<=100
if rule:
    if word[0] == word[1]:
        print("NG")
    else:
        print("OK")
            
    