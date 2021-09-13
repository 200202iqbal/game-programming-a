#change working directory
import os
currentDirect = os.getcwd() #get current directory 
os.chdir(currentDirect+"/temp") #change the current directory
print(os.getcwd())

# os.chdir("..") #change to the parent directory