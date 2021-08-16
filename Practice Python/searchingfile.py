#from python learn : Files

fhand = open("file/mbox-short.txt")
count = 0
for line in fhand:
    if line.startswith("From:"):
        print(line)
fhand.close()

#slicing new line
fhand = open("file/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
fhand.close()

# more structure
fhand = open("file/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #Skip "uninteresting lines"
    if not line.startswith("From :"):
        continue
    #process our interesting line
    print(line)
fhand.close()
fhand = open("file/mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1 :continue
    print(line)
