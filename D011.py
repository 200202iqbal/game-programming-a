words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inputWord = input()
count = 1

rule = inputWord in words
if(rule):
    for x in words:
        if(inputWord == x):
            print(count)
        count += 1
        