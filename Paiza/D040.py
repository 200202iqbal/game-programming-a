#連休の天気
count = 7
total = 0
listt =[]
for _ in range(count):
    t = int(input())
    total += t
    listt.append(t)
rainy = (total*30)/100
count = 0
for _ in listt:
    if(_ <= rainy or _ <= 30):
        count += 1
print(count)
