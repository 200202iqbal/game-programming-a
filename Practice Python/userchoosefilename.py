
# fname = input("Enter the file name :")
# file ="file/" + fname
# fhand = open(file)
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count += 1
# print("There were",count, "subject line in",fname)

fname = "file/" +input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened: ",fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count +=1
print("There were ",count, "subject lines in ",fname)

