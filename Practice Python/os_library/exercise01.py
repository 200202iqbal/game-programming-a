#using os library
#change directory to temp 
#creating a folder in temp
import os
currentDirectory = os.getcwd()
targetDirectory = currentDirectory+"/temp"
os.chdir(targetDirectory) #change directory to targetDirectory
if (os.getcwd() == targetDirectory):
    print("OK")
else:
    print("Failed")

#print(os.getcwd())

reqFolder = ["sys","src","file"] #required Folder list
for folder in reqFolder:
    #create folder from list reqFolder in current working directory
    os.mkdir(folder) 

