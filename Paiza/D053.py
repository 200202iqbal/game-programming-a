words = input()
words = words.lower()
lenwords = len(words)
rule = lenwords >=1 and lenwords <=20
if(rule):
    if(words == "candy" or words =="chocolate"):
        print("Thanks!")
    else:
        print("No!") 