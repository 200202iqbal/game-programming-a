count = 0
for intervar in [3.14,21,9,74,76]:
    count += 1
    print(count,intervar)
print(count)

total = 0
for intervar in [3,14,21,9,74,76]:
    total += intervar
    print("total", total)

def hitungtotal(a):
    total = 0
    for i in a:
        total += i
    return total

a = [1,2,14,15,13,22,90]
print(hitungtotal(a))