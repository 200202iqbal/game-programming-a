#remove folder/directory
import os
os.mkdir("new")
if(os.getcwd()+"/new"):
    print("File Created")
else:
    print("Failed")
    

os.rmdir("new")
print("Error")