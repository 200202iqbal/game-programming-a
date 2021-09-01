cheeses = ["Cheddar","Edam","Gouda"]
for c in cheeses:
    print(c)

for i in range(len(cheeses)):
    cheeses[i] = cheeses[i] + "22"
    print(cheeses[i])

empty = []
for x in empty:
    print("This never happens.")

t = ["a","b","c"]
t.pop()
print(t)

total = 0
count = 0
while True:
    inp = input("Enter a number : ")
    if inp == "done" :break
    value = float(inp)
    total += value
    count += 1

average = total/count
print("Average : ",average)

numlist = list()
while True:
    inp = input("Enter a number : ")
    if inp == "done" :break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average : ",average)

#aliasing
a = [1,2,3]
b = a
print(a is b)