#using os library
#show list directory in current directory
import os
listDir = os.listdir()
print(listDir)
for dir in listDir:
    print(dir)