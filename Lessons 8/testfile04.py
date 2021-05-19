with open("workfile03.txt", "rb+") as f:
    f.write(b"01234567sdfsdfsdffsdfsdfsd89abcdef")
    f.seek(5)   #go to 6th byte in the file
    f.read(1)
    f.seek(-3,2) #go to the 3rd byte before the end
    f.read(1)