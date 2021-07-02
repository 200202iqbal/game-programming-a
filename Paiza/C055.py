n = int(input())
g = str(input())
g = g.lower()
print(g)
text = []
check = n>= 0 and n<=100 and len(g) >= 1 and len(g)<=100
if(check):
    for _ in range(n):
        s = input()
        text.append(s)
    print(text)
count = 0
lentext = len(text)
for word in text:
    result = g in word
    print(word)
    if(not result):
        text.remove(word)
        count +=1
    print(lentext)
    print(count)
    if(count == lentext):
        text.clear()
        text = "None"
    print(text)
