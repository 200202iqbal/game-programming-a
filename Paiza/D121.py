string = str(input())
first = string[0]
second = string[1:]
stringlen = len(string)
rule = stringlen == 3, string[0] == "H","S","T","A"
if(rule):
    if(first == "A"):
        first = "R"
        print(first+second)
    else:
        print(string)