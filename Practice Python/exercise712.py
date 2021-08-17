"""Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

"""
#finput="mbox-short.txt"
#finput = input("Enter a file name: ")
finput = "mbox.txt"
floc = "file/" + finput
try:
    fopen = open(floc)
except:
    print("File not found")
value = 0
count = 0
for line in fopen:
    if line.startswith("X-DSPAM-Confidence:"):
        frontpos = line.find(":")
        backpos = line.find("\n")
        value += float(line[frontpos+1:backpos])
        count +=1
average = value/count
print("Average spam confidence: ",average, "\n")