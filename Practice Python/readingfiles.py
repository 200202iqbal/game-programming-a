# Try read a file
fhand = open("file/mbox.txt")
openFiles = open("file/empty.txt")
print(fhand)
count = 0
for line in fhand:
    count +=1
count2 = 0
for line in openFiles:
    count2 +=1
print("Fhand lines ",count)
print("OpenFiles lines " ,count2)

fhand = open("file/mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])

str = "Hello, world. I'm Iqbal"
print(str[:2])
